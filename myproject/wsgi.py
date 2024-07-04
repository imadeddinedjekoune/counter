"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import json

from django.core.wsgi import get_wsgi_application

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Load Firebase credentials and database URL from environment variables
firebase_cred_json = os.environ.get('FIREBASE_CREDENTIALS_JSON')
firebase_database_url = os.environ.get('FIREBASE_DATABASE_URL')

if not firebase_admin._apps:
    cred = credentials.Certificate(json.loads(firebase_cred_json))
    firebase_admin.initialize_app(cred, {
        'databaseURL': firebase_database_url
    })

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

app = application
