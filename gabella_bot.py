import telebot

bot = telebot.TeleBot('2053487792:AAFTYMh-i1y55lJkNd1Y8VxSTFduMLSS4WE')


@bot.message_handler(content_types=['text'])
def start(message):
    mess = f'Слава Україні, воїне {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)


if __name__ == '__main__':
    pass
