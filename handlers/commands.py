from misc import bot
from telebot.types import Message
from keyboards.reply import getStartMenu
from keyboards.inline import getInlineBtnWrite
from utils import dataBase, template_text


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
    stat = dataBase.get_statistic(message.from_user.id)

    name = stat[0][0]
    score = stat[0][1]
    eagle = stat[0][2]
    tail = stat[0][3]

    bot.send_message(message.from_user.id, template_text.TEMPLATE_TEXT['show'].format(name, score, eagle, tail))


@bot.message_handler(commands=['about'])
def about(message: Message):
    bot.send_message(message.from_user.id, template_text.TEMPLATE_TEXT['about'],
                     reply_markup=getInlineBtnWrite(), disable_web_page_preview=True)
