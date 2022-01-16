print("importing lib")
# Librairie
import discord
from discord.ext import tasks
from datetime import datetime
# ressource
import secrets
import testmsg
import time
import os

print("Démarrage du bot le : ",datetime.now().day, "/", datetime.now().month, "/", datetime.now().year, 'à', datetime.now().hour, "h",datetime.now().minute)

global loopS
loopS = -1

# définition du bot
intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)

#emote
EpicEmote = str('<:epic:583548368626647040>')

#role
Giveaway = str("<@&" + str(secrets.ROLE_ID) + ">")

# event quand le bot est lancé
@bot.event
async def on_ready():
    print("Le bot est connecté")  # affiche dans la console que le bot est démarré
    logchannel = bot.get_channel(secrets.LOG_CHANNEL_ID)
    await logchannel.send("Bot en ligne")
    loop.start()


#Quand message
@bot.event
async def on_message(message):

    logchannel = bot.get_channel(secrets.LOG_CHANNEL_ID)
    print(message.author, ":", message.content)  # affiche le message dans la console
    if message.channel == logchannel:
        test = testmsg.mots(message.content, "loop")
        if test != -1:
            global loopS
            if loopS < 00:
                loop.start()
                reponse = ":white_check_mark: Redémarage des évènements répétitifs"
            else:
                reponse = ":x: Les évènements répétitifs sont déjà lancé et executé a " + str(loopS) + "h, " + str(loopS + 6) + "h, " + str(loopS + 12) + "h, "  + str(loopS+ 18) + "h"
            await message.channel.send(reponse)  # envoie un message
        
        test = testmsg.mots(message.content, "stop")
        if test != -1:
            print("Arret du bot manuel le : ", datetime.now().day, "/", datetime.now().month, "/", datetime.now().year, 'à', datetime.now().hour, "h",datetime.now().minute, "par", message.author)
            loop.cancel()
            await logchannel.send("Arret du Bot")
            await bot.logout()
        test = testmsg.mots(message.content, "update")
        if test != -1:
            await logchannel.send("Ajout des messages")
            await Epic()

# toutes les heures, execute :
@tasks.loop(hours=6.0)
async def loop():
    global loopS
    day = datetime.now().weekday()  # recupère le numéro du jour de la semaine
    hour = datetime.now().hour  # recupère l'heure du système
    loopS = hour % 6
    if 9 < hour < 22:
        await Epic()


async def Epic():
    channel = bot.get_channel(secrets.CHANNEL_ID)

    os.system("./../get_games/get_games.sh")

    with open("epic.txt", "r") as entree:
        contenue = entree.read()
    c = list(contenue)

    if c[len(c) - 1] != '\n':       # verifie que le document finisse par un '\n' et en rajoute si besoin
        c.append('\n')

    E = 0
    Name = ""
    Link = ""
    Date = ""
    Done = False
    i = 0

    while i < len(c):
        # print(c[i], end="")

        if c[i] == '\n':

            #recuperation des date
            EDayS = Date
            EDay = datetime.strptime(EDayS, '%Y-%m-%d').date()
            day = datetime.now().date()

            #si la date est passé supprime la ligne
            if EDay < day:
                Done = True
                while c[i - 1] != '\n':
                    del c[i - 1]
                    i = i - 1
                del c[i]

            if Done == False:
                # print("Name : ", Name, "\nLink : ", Link, "\nDate : ", Date, "\nDone : ", str(Done), "\n")
                await message("Epic", Name, Link, EDayS)

                c.insert(i, ";V")
                Done = True
                while c[i] != '\n':
                    i = i + 1

            E = 0
            Name = ""
            Link = ""
            Date = ""
            Done = False

        elif c[i] == ';':
            E = E + 1
        elif E == 0:
            Name = Name + c[i]
        elif E == 1:
            Link = Link + c[i]
        elif E == 2:
            Date = Date + c[i]
        elif E == 3:
            Done = True

        i = i + 1

    contenue = ''.join(c)
    with open("epic.txt", "w") as sortie:
        sortie.write(contenue)


async def message(Plateforme, Nom, Link, Espiration):
    channel = bot.get_channel(secrets.CHANNEL_ID)
    if Plateforme == "Epic":
        msg = str(Giveaway) + " " + str(Nom) + " est gratuit sur l'EpicGames Store " + str(EpicEmote) + " jusqu'au " + Espiration + ", profitez-en : " + Link
        await channel.send(msg)


# si la boucle est fini
@loop.after_loop
async def Erreur():
    print(datetime.now().day, "/", datetime.now().month, "/", datetime.now().year, 'à', datetime.now().hour, "h",datetime.now().minute)
    print("/!\\ Erreur de tache")  # envoie un message dans la console
    logchannel = bot.get_channel(secrets.LOG_CHANNEL_ID)
    global loopS
    loopS = -1
    await logchannel.send("Les évènements répétitifs se sont arrété")
    

# affiche le démarage du bot
print("Démarrage du bot")
bot.run(secrets.BOT_TOKEN)  # démarre le bot