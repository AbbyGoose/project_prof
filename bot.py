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
def func(message):
    global n, m
    n = 0
    m = 0
    user_id = message.from_user.id
    user_name = message.from_user.username
    manager.add_user(user_id, user_name)
    bot.register_next_step_handler(message, show)

@bot.message_handler()
def show(message):
    global n, m
    user_id = message.from_user.id
    user_name = message.from_user.username
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(tuple(que.items())[n][0])
    btn2 = types.KeyboardButton(tuple(que.items())[n+1][0])
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Ты бы предпочёл: ", reply_markup=markup)
    text = message.text
    if(text == tuple(que.items())[n][0]):
        res = que.get(tuple(que.items())[n][0])                  
    else:
        res = que.get(tuple(que.items())[n+1][0])                  
    manager.add_res(user_id, user_name, res)
    n += 2
    m += 1
    print(m)
    if m < 40:
        bot.register_next_step_handler(message, show)
    else:
        bot.register_next_step_handler(message, results)

def results(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    res = manager.results(user_id, user_name)
    if res == 'h':
        bot.send_message(message.chat.id, text="Профессии типа «Человек-Человек». К данному типу относятся профессии, основное направление которых связано с общением между людьми и их взаимном влиянии. Такие как, доктор, преподаватель, менеджер, учитель, психолог, продавец, тренер. Важным качеством в данных профессиях является не только желание, но и умение активного взаимодействия с людьми и продуктивного общения. Важно спецификой при подготовке являются хорошее знание профессиональной сферы и развитые коммуникативные навыки.".format(message.from_user))
    elif res == 's':
        bot.send_message(message.chat.id, text="Профессии типа «Человек-Знаковая система». Основным направление деятельности данного типа профессий является работа с цифрами, формулами, расчетами, текстами, базами данных. Это такие профессии как программист, экономист, редактор, аналитик, переводчик, датасайнтист, бухгалтер. Профессионально важные качества данного типа профессий: точность и аналитический склад ума, внимательность, логическое мышление. Для успешной деятельности важно иметь интерес к различным формулам, таблицам, картам, схемам, базам данных.".format(message.from_user))
    elif res == 't':
        bot.send_message(message.chat.id, text="Профессии типа «Человек-Техника». Профессии данного типа направлены на эксплуатацию различных технических устройств и приборов, их обслуживание и создание. К таким профессиям относятся: металлург, водители различного транспорта, пилоты, слесари, технологи на предприятиях, строители, автомеханики и т.д. Для их успешной деятельности крайне важны технический склад ума, внимательность, склонность к действиям, а не размышлениям.".format(message.from_user))
    elif res == 'n':
        bot.send_message(message.chat.id, text="Профессии типа «Человек-Природа». Сфера деятельности данного типа направлена на окружающую нас природу. Это такие профессии как ветеринар, эколог, агроном, геолог, микробиолог. Профессионально важными качествами данных профессий являются: интуиция, эмпатия, умение заботиться о ком-либо кроме себя. Такие люди обычно трепетно относятся к представителям живой природы. Для успешной деятельности в профессиях этого типа недостаточно просто быть любителем отдыха на природе, важно еще защищать природу, стремиться позитивно взаимодействовать с ней.".format(message.from_user))
    elif res == 'p':
        bot.send_message(message.chat.id, text="Профессии типа «Человек-Художественные образы». Профессии этого типа направлены на создание, восстановление и модернизацию различных произведений культуры и искусства: дизайнер, художник, архитектор, стилист, фотограф, режиссер, реставратор. Профессионально важными качествами являются хорошее воображение, творческое нестандартное мышление, креативность.".format(message.from_user))

bot.polling(none_stop=True)
