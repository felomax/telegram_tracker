from telethon import TelegramClient, events, sync
import json
from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector


# api_id y api_hash.
api_id = 14251256
api_hash = '31c9395f4965436ab03f5a355cce15a4'

client = TelegramClient('anon', api_id, api_hash)

# group = 'Desarrolladores NodeJS'
group = ['Desarrolladores NodeJS']

#username = events.username


@client.on(events.NewMessage(chats=group))

async def my_event_handler(event):


    sender = await event.get_sender()

    chat = await event.get_chat()
    sender = await event.get_sender()


    
    print ("{'texto':'",event.raw_text,"','nombre_chat':'", chat.title,"','usuario':'", sender.username,"','nombre':'", sender.first_name,"','apellido':'", sender.last_name,"'},") 

client.start()

client.run_until_disconnected()