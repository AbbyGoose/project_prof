import telebot
from telebot import types
from config import *
from logic import *
bot = telebot.TeleBot(token)
manager = DatabaseManager(database)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот, который поможет тебе в выборе профессии, если ты не знаешь, что делать, или устал от нынешней. Я тебе помогу с пмощью теста на профориентацию!".format(message.from_user))
    bot.register_next_step_handler(message, func)
    
@bot.message_handler(commands=['test'])
def func(message, context):
    user_id = message.from_user.id
    user_name = message.from_user.username
    manager.add_user(user_id, user_name)
    bot.register_next_step_handler(message, show)

def show(message, context):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(tuple(que.items())[n][n])
    btn2 = types.KeyboardButton(tuple(que.items())[n+1][n+1])
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Ты бы предпочёл: ", reply_markup=markup)
    bot.register_next_step_handler(message, ques)
    
def ques(message, context):
    user_id = message.from_user.id
    user_name = message.from_user.username
    text = message.text
    if(text == tuple(que.items())[n][n]):
        res = que.get(tuple(que.items())[n][n])
        n += 2               
        manager.add_res(user_id, user_name, res)
    else:
        print('')
    m += 1
    if m < 41:
        bot.register_next_step_handler(message, show)
bot.polling(none_stop=True)
