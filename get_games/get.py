from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import datetime


def get_name(line) -> str:
    tableau = line.split("\n")
    return f"{tableau[0]} par '{tableau[1]}'"


def say_ok(line) -> bool:
    # tableau = line.split("\n")
    return "Gratuit" in line


def in_done(name):
    with open("../data/DoneDiscord.txt", "r", encoding="utf8", errors='ignore') as f:
        return name in f.read().split("\n")


def in_todo(name):
    with open("../data/TodoDiscord.txt", "r", encoding="utf8", errors='ignore') as f:
        return name in f.read().split("\n")


def get_games(bw):
    print(f"Starting test on {datetime.now()}")
    bw.get('https://www.epicgames.com/store/fr/browse?sortBy=currentPrice&sortDir=ASC&priceTier=tierDiscouted&pageSize=30')
    sleep(2)
    bw.execute_script("window.scrollTo(0, 450)")
    target = bw.find_element_by_xpath("/html/body/div[1]/div/div[4]/main/div/div/div[3]/div/div/section/div/div/aside/div/div[3]/div[2]/div[6]/div/div")
    target.click()
    sleep(2)
    print("On the discount page, checking games.")
    first_col = True
    for col in range(1, 31):
        print(f"Game {col} of 30")
        if first_col:
            first_col=False
            xpath = f"/html/body/div[1]/div/div[4]/main/div/div/div[3]/div/div/section/div/div/div/section/div/section/section/ul/li[{col}]"
        else:
            xpath = f"/html/body/div[1]/div/div[4]/main/div/div/div[3]/div/div/section/div/div/div/section/div/section/section/ul/li[{col}]"
        txt = bw.find_element_by_xpath(xpath).text
        print(txt)
        if say_ok(txt):
            name = get_name(txt)
            print(f"Ok for {name}")
            if not in_done(name) and not in_todo(name):
                with open("../data/TodoDiscord.txt", "a", encoding="utf8", errors='ignore') as f:
                    f.write(name + "\n")


def main(bw):
    get_games(bw)


if __name__ == "__main__":
    def selenium_init():
        o = Options()
        o.add_argument("--headless")
        o.add_argument("--no-sandbox")
        o.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Firefox(executable_path="./geckodriver", options=o)
        return browser


    browser = selenium_init()
    main(browser)
    browser.quit()
