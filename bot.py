from pyrogram import Client
import config

api_id = config.API_ID
api_hash = config.API_HASH
group = 'gabellastest'
channel = 'gabellachannel'

app = Client('my_account', api_id, api_hash)
