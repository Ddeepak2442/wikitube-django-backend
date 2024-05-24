# build_files.sh

#!/bin/bash
# Ensure pip is available
/usr/bin/python3.9 -m ensurepip --upgrade
# Upgrade pip
/usr/bin/python3.9 -m pip install --upgrade pip
# Install dependencies from requirements.txt
/usr/bin/python3.9 -m pip install -r requirements.txt
# Add other necessary build steps below
python3.9 manage.py collectstatic --noinput

python3.9 manage.py makemigrations
python3.9 manage.py migrate