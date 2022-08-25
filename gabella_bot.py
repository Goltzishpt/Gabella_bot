import telebot
from telebot import types

bot = telebot.TeleBot('2053487792:AAFTYMh-i1y55lJkNd1Y8VxSTFduMLSS4WE')



@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mess = f'Добро пожаловать в Габелла-бот, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    mess2 = f'Габелла поможет тебе что-то там сделать, правда пока хз что, бот недоработан'
    bot.send_message(message.chat.id, mess2, parse_mode='html')
    btn1 = types.KeyboardButton('Поехали')
    markup.add(btn1)
    bot.send_message(message.chat.id, text=('Начнем?'), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Поехали':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Русский')
        btn2 = types.KeyboardButton('Українська')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text=('Выбери язык'), parse_mode='html', reply_markup=markup)
    elif message.text == 'Русский':
        bot.send_message(message.chat.id, text=('Пока мы только начинаем и ты будешь одним из первых пользователей. Давай знакомиться'), parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Давай начнем')
        markup.add(btn1)
        bot.send_message(message.chat.id, text=('Сколько тебе лет?'), parse_mode='html', reply_markup=markup)
    elif message.text == int:
        print(message.text)
        if type(message.text) == int:
            x = message.text
            print(x)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Я девушка')
        btn2 = types.KeyboardButton('Я парень')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text=('Теперь выберем пол:'), parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)


if __name__ == '__main__':
    pass


#        btn1 = types.KeyboardButton('1')
#        btn2 = types.KeyboardButton('2')
#        btn3 = types.KeyboardButton('3')
#        btn4 = types.KeyboardButton('4')
#        btn5 = types.KeyboardButton('5')
#        markup.add(btn1, btn2, btn3, btn4, btn5)
#        bot.send_message(message.chat.id, text=('1. \n2. \n3. \n4. \n5.'), parse_mode='html', reply_markup=markup)
