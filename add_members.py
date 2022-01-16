from telethon import TelegramClient, events, sync
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
import sys
import csv
import traceback
import time
import random

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = "13055145"
api_hash = "a81413f7622ea1b0333bf1775e31f502"
phone = "+923369961618"
client = TelegramClient(phone, api_id, api_hash)
client.start()

users = []
with open('users.csv', encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(float(row[2]))
        user['name'] = row[3]
        users.append(user)

channel = client.get_input_entity('https://t.me/pythonlearning777')

mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
for user in users:
    try:    
        print ("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        # InviteToChannelRequest(target_group_entity,[user_to_add])
        client(InviteToChannelRequest(channel,[user_to_add]), aggressive=True)
        print("Waiting for 60 Seconds...")
        time.sleep(60)
    except Exception as e:
        print(str(e))
        continue
