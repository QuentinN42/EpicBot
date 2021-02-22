import sys
from datetime import datetime

from discord.ext.commands import Bot

import secrets


def read_todo():
    with open("../data/TodoDiscord.txt", "r", encoding="utf8", errors='ignore') as f:
        return f.read().split("\n")


def clear_todo():
    with open("../data/TodoDiscord.txt", "w", encoding="utf8", errors='ignore') as f:
        f.write("")


def add_done(todo):
    with open("../data/DoneDiscord.txt", "a", encoding="utf8", errors='ignore') as f:
        f.write(todo + "\n")


def create_message(game):
    return f"<@&{secrets.role}> voici un nouveau jeu gratuit sur l'epic games store : {game}"


bot = Bot("!")


@bot.event
async def on_ready():
    print("Logged in !")
    print("test" + str(datetime.now()))
    for todo in read_todo():
        if todo != "":
            await bot.get_channel(secrets.channel).send(create_message(todo))
            add_done(todo)
    clear_todo()
    sys.exit(0)


print("Starting bot.")
bot.run(secrets.BOT_TOKEN)
