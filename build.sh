#!/usr/bin/env bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pyinstaller
DIST_PATH="./dist/macos"

pyinstaller todo.py --onefile --distpath $DIST_PATH