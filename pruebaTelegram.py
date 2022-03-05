from telethon import TelegramClient, events, sync
import json
#from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

# api_id y api_hash.
api_id = 14251256
api_hash = '31c9395f4965436ab03f5a355cce15a4'

client = TelegramClient('anon', api_id, api_hash)

# group = 'Desarrolladores NodeJS'
#group = ['Desarrolladores NodeJS']
group = 'fuerteyderecho'


#username = events.username


@client.on(events.NewMessage(chats=group))

async def my_event_handler(event):

    cnx = mysql.connector.connect(user='root', database='telegram')
    cursor = cnx.cursor()
    today = str(datetime.now().date())
    sender = await event.get_sender()

    chat = await event.get_chat()
    sender = await event.get_sender()
 
    #print ("{'texto':'",event.raw_text,"','nombre_chat':'", chat.title,"','usuario':'", sender.username,"','nombre':'", sender.first_name,"','apellido':'", sender.last_name,"'},") 
    
    add_message = ("INSERT INTO mensajes (username, mensaje, grupo, hora, first_name,last_name) VALUES (%s, %s, %s, %s, %s, %s)")

    data_message = (sender.username , event.raw_text, chat.title, today, sender.first_name, sender.last_name)
    print('resultado mensaje: ', data_message)


    cursor.execute(add_message, data_message)

    cnx.commit()
    cursor.close()
    cnx.close()

client.start()

client.run_until_disconnected()