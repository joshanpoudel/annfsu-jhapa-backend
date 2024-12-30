import firebase_admin
from firebase_admin import credentials

creds = credentials.Certificate("config/firebase/serviceAccountKey.json")

firebase_admin.initialize_app(creds)