from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def getInlineMenu():
    keyboard = InlineKeyboardMarkup()

    button1 = InlineKeyboardButton('3 sec.', callback_data='3')
    button2 = InlineKeyboardButton('5 sec.', callback_data='5')

    keyboard.row(button1, button2)

    return keyboard

def getInlineBtnWrite():
    keyboard = InlineKeyboardMarkup()
    write = InlineKeyboardButton('Написать', url='t.me/axemanofic')
    keyboard.add(write)
    return keyboard

