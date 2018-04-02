#!/bin/bash


echo "contenttypes.json"
python3 manage.py loaddata fixtures/contenttypes.json 
echo "auth.json"
python3 manage.py loaddata fixtures/auth.json 
echo "protolib.json"
python3 manage.py loaddata fixtures/protolib.json 
echo "protoExt.json"
python3 manage.py loaddata fixtures/protoExt.json 
echo "prototype.json"
python3 manage.py loaddata fixtures/prototype.json 
echo "rai01ref.json"
python3 manage.py loaddata fixtures/rai01ref.json 


