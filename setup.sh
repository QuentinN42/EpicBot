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


# set up selenium
(
    cd get_games || exit 1
    python3 -m virtualenv venv || exit 1

    source venv/bin/activate && \
    python3 -m pip install -r requirements.txt && \
    deactivate || exit 1

    wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz
    tar -xvf geckodriver-v0.29.0-linux64.tar.gz
    rm geckodriver-v0.29.0-linux64.tar.gz
)
