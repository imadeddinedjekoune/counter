import threading
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

class CounterThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.daemon = True
        self.running = True

    def run(self):
        while self.running:
            time.sleep(1)
            ref = db.reference('/')

            new_data = {
                'name': '{0}'.format(datetime.now()),
            }
            ref.push(new_data)
            self.counter += 1

    def stop(self):
        self.running = False
