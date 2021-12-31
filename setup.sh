#!/usr/bin/env bash

# set up data
mkdir data
touch data/DoneDiscord.txt
touch data/TodoDiscord.txt

# set up discord
(
    cd display_games || exit 1
    python3 -m virtualenv venv || exit 1

    source venv/bin/activate && \
    python3 -m pip install -r requirements.txt && \
    deactivate || exit 1
)


cat << EOF
All done,
You must add a python file named secrets.py in the display_games folder with :
BOT_TOKEN -> the token for the discord bot
channel   -> the channel id where the bot speak
role      -> the role id to ping

And add this lines to your crontab :
EOF
envsubst < crontab
