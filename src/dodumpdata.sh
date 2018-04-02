#!/bin/bash

mkdir fixtures 

python3 manage.py dumpdata --indent 2 contenttypes 	> fixtures/contenttypes.json 
python3 manage.py dumpdata --indent 2 auth 			> fixtures/auth.json 
python3 manage.py dumpdata --indent 2 protoLib 		> fixtures/protolib.json 
python3 manage.py dumpdata --indent 2 protoExt 		> fixtures/protoExt.json 
python3 manage.py dumpdata --indent 2 prototype 	> fixtures/prototype.json 
python3 manage.py dumpdata --indent 2 rai01ref 		> fixtures/rai01ref.json 

# python3 manage.py dumpdata --natural-foreign --natural-primary --indent 2 contenttypes > fixtures/contenttypes.json 

# mkdir datascripts

# python3 manage.py dumpscript  auth 			> datascripts/auth.py
# python3 manage.py dumpscript  protoLib 		> datascripts/protolib.py
# python3 manage.py dumpscript  protoExt 		> datascripts/protoExt.py
# python3 manage.py dumpscript  prototype 	> datascripts/prototype.py
# python3 manage.py dumpscript  rai01ref 		> datascripts/rai01ref.py

#  Db 
tar -zcvf "db/db-$(date +"%Y%m%d_%H%M%S").tar.gz" db/db.sqlite3

