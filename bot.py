import telebot
from telebot import types
from config import *
from logic import *

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Я передумал, пока.")
    btn2 = types.KeyboardButton("Давай пройдём этот тест!")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот, который поможет тебе в выборе профессии, если ты не знаешь, что делать, или устал от нынешней. Я тебе помогу с пмощью теста на профориентацию!".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Я передумал, пока."):
        bot.send_message(message.chat.id, text="пока(")
    elif(message.text == "Давай пройдём этот тест!"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(que[0])
        btn2 = types.KeyboardButton(que[1])
        bot.send_message(message.chat.id, text="Ты бы предпочёл: ", reply_markup=markup)
        if(message.text == que[0]):
            bot.send_message(message.chat.id, "У меня нет имени..")
        elif message.text == que[1]:
            bot.send_message(message.chat.id, text="Поздороваться с читателями")
        else:
            bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)
