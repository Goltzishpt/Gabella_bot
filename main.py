import time
from pyrogram import Client, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import config
from plugins import handlers

api_id = config.API_ID
api_hash = config.API_HASH
group = 'gabellastest'
channel = 'gabellachannel'


app = Client('account', api_id, api_hash)



app.run()
