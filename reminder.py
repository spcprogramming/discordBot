'''
Reminder fields:
    - Title
    - Date
    - Time
    - Description
    - Roles that should be notified, if left blank will default to all
    - Notes (Optional)
'''

import discord
import json

client = discord.Client()

class Reminder:
    def __init__(self, title=None, date=None, time=None, description=None, notes=None, roles="all"):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.notes = notes
        self.roles = roles

# converts object to json
def convert(reminder):
    return json.dumps(reminder.__dict__)

def save(reminder):
    file = open("reminders", "w")
    file.write(reminder)

def pred(m):
    return m.author == message.author and m.channel == message.channel
