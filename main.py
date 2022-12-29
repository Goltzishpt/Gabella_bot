from pyrogram import Client
import config


api_id = config.API_ID
api_hash = config.API_HASH
group = 'gabellastest'
channel = 'gabellachannel'

plugins = dict(
    root='plugins',
    include=[
        'handlers'
    ]
)

Client('my_account', api_id, api_hash, plugins=plugins).run()


