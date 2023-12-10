#!/bin/bash

# name of the venv folder
VENV_NAME="venv"

# create the venv
python3 -m venv $VENV_NAME

# activate it
source $VENV_NAME/bin/activate

# install dependencies from requirements.txt
pip install -r setup/requirements.txt

# display end of processes
echo "Virtual environment created and dependencies installed"
