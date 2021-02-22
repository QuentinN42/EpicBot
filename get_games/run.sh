#!/usr/bin/env bash

source venv/bin/activate

python3 get.py >> ./logs 2>&1

deactivate
