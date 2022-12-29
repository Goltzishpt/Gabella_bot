import asyncio
from pyrogram import filters
import pyrogram
from bot import app
from pyrogram import enums


async def message_handler(message_obj, type_message):
    print('get message from user, wait 5 sec')
    print('read the message from user')
    print('imitation typing...')
    await asyncio.sleep(2)
    print(type(message_obj))
    await app.send_chat_action(message_obj.chat.id, type_message)
    await asyncio.sleep(5)
    if type_message == enums.ChatAction.TYPING:
        await app.send_message(message_obj.chat.id, 'Привет \nЯ пока занята(или сплю) и не могу ответить. Напишу позже(c) Gabella-bot')
    if type_message == enums.ChatAction.CHOOSE_STICKER:
        await app.send_sticker(chat_id=message_obj.chat.id,
                               sticker='CAACAgIAAxkBAAJrHmOtv3SnmTOTMRJPAAH46RvVjmdtQwACgxYAAlPr2EukI39bWKGsqR4E')



@app.on_message(filters=filters.text & filters.private)
async def text_handler(client, message):
    print(f'Користувач відправив текст: {message.text}')
    await message_handler(message, enums.ChatAction.TYPING)



@app.on_message(filters=filters.sticker & filters.private)
async def sticker_handler(client, message):
    print(f'Користувач відпрвив текст: {message.text}')
    print('Відповідаємо користувачу...')
    await message_handler(message, enums.ChatAction.CHOOSE_STICKER)

