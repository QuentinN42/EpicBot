import sys
from datetime import datetime

import discord
from discord import TextChannel
from discord.ext.commands import Bot
from discord.ext import tasks
import secrets


async def log(txt):
    print(txt)
    await bot.get_channel(int(secrets.log)).send(txt)

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
    await log("Logged in !")
    await log(str(datetime.now()))
    loop.start()


@tasks.loop(hours=10.0)
async def loop():
    for todo in read_todo():
        if todo != "":
            channel = bot.get_channel(int(secrets.channel))
            msg = create_message(todo)
            await channel.send(msg)
            add_done(todo)

    clear_todo()
    await log("Done")
    await bot.close()


print("Starting bot.")
bot.run(secrets.BOT_TOKEN)
