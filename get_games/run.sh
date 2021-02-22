#!/usr/bin/env bash

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" && \
source venv/bin/activate && \
python3 get.py >> ./logs 2>&1 && \
deactivate
