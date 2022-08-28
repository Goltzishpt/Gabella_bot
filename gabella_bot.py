import telebot
from telebot import types
import config
from gabella_db import BotDB


BotDB = BotDB('gabella_db')
bot = telebot.TeleBot(config.BOT_TOKEN)



@bot.message_handler(commands='start')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mess = 'Welcome to Gabella-bot.'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    btn1 = types.KeyboardButton('Go')
    markup.add(btn1)
    bot.send_message(message.chat.id, text='Start now?', parse_mode='html', reply_markup=markup)
    print(message.chat.id)


@bot.message_handler(commands='Go')
def begin(message):
    test = BotDB.user_exists(message.chat.id)
    print(test)
    if test == True:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mess = 'Ah, shit. Here we go again'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        btn1 = types.KeyboardButton('Come back')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Would you like to continue?', parse_mode='html', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mess = 'Welcome to the world of love'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        btn1 = types.KeyboardButton('Registation')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Would you like to join?', parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)

