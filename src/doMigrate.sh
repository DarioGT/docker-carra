#!/bin/bash

# python manage.py makemigrations $1
python3 manage.py makemigrations protoLib
python3 manage.py makemigrations protoExt
python3 manage.py makemigrations prototype
python3 manage.py makemigrations rai01ref
python3 manage.py migrate 


