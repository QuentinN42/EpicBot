#!/usr/bin/env bash

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" && \
source venv/bin/activate && \
python3 bot.py >> ./logs 2>&1 && \
deactivate
