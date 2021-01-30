from telebot.types import Message
from misc import bot
from utils.global_var import STICKERS
from random import randint
from utils import dataBase


def getNum():
    num = randint(0, 1)
    return num


def getSticker():
    num = getNum()
    sticker = open(STICKERS[num][0], 'rb')
    return sticker, num


def loopTossing(message: Message, delay):
    while delay != 0:
        bot.send_message(message.chat.id, "Осталось {} ...".format(delay))
        delay -= 1

      
def getRatingInfo():
    rating = "\n<u>Топ 5 на сегодня:</u>\n"
    top = dataBase.get_rating()
    for i in range(len(top)):
        name, score, eagle, tail = top[i]
        rating += str(name) + " " + str(score) + " " + str(eagle) + " " + str(tail) + "\n\n"
    return rating
