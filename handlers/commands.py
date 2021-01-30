from misc import bot
from telebot.types import Message
from keyboards.reply import getStartMenu
from keyboards.inline import getInlineBtnWrite
from utils import dataBase, template_text
from settings.config import ID


@bot.message_handler(commands=['start'])
def start(message: Message):
    dataBase.insert_user(message.from_user.id, message.from_user.first_name)
    delay = dataBase.get_delay(message.from_user.id)
    bot.send_message(message.from_user.id,
                     template_text.TEMPLATE_TEXT['start'].format(message.from_user.first_name, delay),
                     reply_markup=getStartMenu())


@bot.message_handler(commands=['help'])
def help(message: Message):
    bot.send_message(message.from_user.id, template_text.TEMPLATE_TEXT['help'])


@bot.message_handler(commands=['show'])
def show(message: Message):
    stat = dataBase.get_statistic_user(message.from_user.id)
    name, score, eagle, tail = stat[0]
    bot.send_message(message.from_user.id, template_text.TEMPLATE_TEXT['show'].format(name, score, eagle, tail))


@bot.message_handler(commands=['about'])
def about(message: Message):
    bot.send_message(message.from_user.id, template_text.TEMPLATE_TEXT['about'],
                     reply_markup=getInlineBtnWrite(), disable_web_page_preview=True)
    bot.send_message(message.from_user.id, ID)


@bot.message_handler(commands=['god'])
def god_mode(message: Message):
    if message.from_user.id == ID:
        start_users = dataBase.get_start_users()
        active_users = dataBase.get_active_users()
        bot.send_message(message.from_user.id, template_text.TEMPLATE_TEXT['god'].format(start, active_users))

    rating = '''<u>Топ 5 на сегодня:</u>\n'''
    top = dataBase.get_rating()

    for i in range(len(top)):
        name, score, eagle, tail = top[i]
        rating += str(name) + " " + str(score) + " " + str(eagle) + " " + str(tail) + "\n\n"

    bot.send_message(message.from_user.id, rating)
