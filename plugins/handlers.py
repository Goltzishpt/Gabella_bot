from pyrogram import Client, filters


@Client.on_message(filters=filters.text)
async def text_handler(client, message):
    print(f'Користувач відпрвив текст: {message.text}')
    print('Відповідаємо користувачу...')
    await message.reply('hello')

@Client.on_message(filters=filters.sticker)
async def sticker_handler(client, message):
    print(f'Користувач відпрвив текст: {message.text}')
    print('Відповідаємо користувачу...')
    await message.reply('sticker')