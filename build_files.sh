#!/bin/bash

apt-get install -y libpq-dev
pip install -r requirements.txt 
python3.9 manage.py collectstatic