from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
from datetime import datetime


def selenium_init():
    binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    browser = webdriver.Firefox(firefox_binary=binary)
    browser.get('https://www.epicgames.com/store/fr/browse?sortBy=currentPrice&sortDir=ASC&priceTier=tierDiscouted&pageSize=30')
    return browser


def get_name(line) -> str:
    tableau = line.split("\n")
    return f"{tableau[0]} par '{tableau[1]}'"


def say_ok(line) -> bool:
    tableau = line.split("\n")
    return "Gratuit" in tableau[2]


def in_done(name):
    with open("../data/DoneDiscord.txt", "r") as f:
        return name in f.read().split("\n")

def in_todo(name):
    with open("../data/TodoDiscord.txt", "r") as f:
        return name in f.read().split("\n")

def main():
    bw = selenium_init()
    sleep(2)
    target = bw.find_element_by_xpath("/html/body/div[1]/div/div[4]/main/div/div/div[3]/div/div/section/div/div/aside/div/div[3]/div[2]/div[6]/div/div")
    bw.execute_script("window.scrollTo(0, 450)") 
    target.click()
    sleep(2)
    for col in range(1,31):
        xpath = "/html/body/div[1]/div/div[4]/main/div/div/div[3]/div/div/section/div/div/div/section/div/section/section/ul/li[" + str(col) + "]/a/div/div\n"
        txt = bw.find_element_by_xpath(xpath).text
        if say_ok(txt):
            name = get_name(txt)
            if not in_done(name) and not in_todo(name):
                with open("../data/TodoDiscord.txt", "a") as f:
                    f.write(name + "\n")


if __name__ == "__main__":
    while True:
        print("test" + str(datetime.now()))
        main()
        sleep(600)
