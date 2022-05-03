#!/bin/bash
python3 -m virtualenv final_proyect
source ./final_proyect/bin/activate
pip3 install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:$PWD/preprocessino

