from discord.ext.commands import Bot
from discord.ext import tasks
from datetime import datetime
import asyncio

import secrets


def read_todo():
    with open("../data/TodoDiscord.txt", "r") as f:
        return f.read().split("\n")


def clear_todo():
    with open("../data/TodoDiscord.txt", "w") as f:
        f.write("")


def add_done(todo):
    with open("../data/DoneDiscord.txt", "a") as f:
        f.write(todo + "\n")


def create_message(game):
    return f"<@&{secrets.role}> voici un nouveau jeu gratuit sur l'epic games store : {game}"


def clear_done():
    print(datetime.now())
    
    def jour(line):
        t = line.split(" ")
        t = t[0]
        t = t.split("-")
        jour = t[2]
        print(jour, type(jour))

    d = str(datetime.now())
    jour(d)

    jv = str("15")
    print(jv, type(jv))
    if jv == jour:
        print("debut du clear de donediscord.txt")
        with open("../data/DoneDiscord.txt", "w") as f:
            f.write("")
        print("fichier clear")


bot = Bot("!")


@tasks.loop(seconds=6*60*60)
async def loop():
    print("test" + str(datetime.now()))
    for todo in read_todo():
        if todo != "":
            await bot.get_channel(secrets.channel).send(create_message(todo))
            add_done(todo)
    clear_todo()


@bot.event
async def on_ready():
    print("Logged in !")
    loop.start()


bot.run(secrets.BOT_TOKEN)
