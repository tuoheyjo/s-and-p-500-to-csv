#!/usr/bin/python
import pyrebase
import sys
import json
from os.path import join, exists, dirname
from os import environ

# user login for firebase
try:
    email = environ["USER_EMAIL"]
    pw = environ["USER_PW"]
except:
    print("Could not access environmental variables")

# firebase app configuration values
config = {
        "apiKey": environ["FIREBASE_API_KEY"],
        "authDomain": environ["FIREBASE_AUTHDOMAIN"],
        "databaseURL": environ["FIREBASE_DATABASE_URL"],
        "storageBucket": environ["FIREBASE_STORAGE_BUCKET"],
}

# Initialize firebase app object
firebase = pyrebase.initialize_app(config)
# Initialize firebase authorization object
auth = firebase.auth()
# Sign in as User
user = auth.sign_in_with_email_and_password(email, pw)
# refresh the token (expires after 1 hr)
user = auth.refresh(user['refreshToken'])
# Initialize database object
db = firebase.database()

# Open JSON file with data
dirpath = dirname(sys.path[0])
datadir = join(dirpath, 'data')
fpathjson = join(datadir, 'sp500.json')

if (exists(datadir)):
    
    try:
        with open(fpathjson, 'r') as f:
            data = json.loads(f.read())
            # Add data to database using the user id token
            data = db.child("s-and-p-500").update(data, user['idToken'])
    
    except Exception as e:
        print(e)
