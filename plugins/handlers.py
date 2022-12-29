import asyncio
from pyrogram import Client, filters


async def message_handler(client_obj, message_obj):
    print('get message from user, wait 5 sec')
    await asyncio.sleep(5)
    await client_obj.read_history(message_obj.chat.id)
    print('read the message from user')
    await client_obj.send_chat_active(message_obj.chat.id, 'typing')


@Client.on_message(filters=filters.text)
async def text_handler(client, message):
    print(f'Користувач відправив текст: {message.text}')
    await message_handler(client, message)


@Client.on_message(filters=filters.sticker)
async def sticker_handler(client, message):
    print(f'Користувач відпрвив текст: {message.text}')
    print('Відповідаємо користувачу...')
    await message.reply('sticker')
