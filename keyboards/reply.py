from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def getStartMenu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    buttonStart = KeyboardButton('Подбросить монетку 👋')
    buttonDelay = KeyboardButton('Установить задержку ⏲')

    keyboard.add(buttonStart)
    keyboard.add(buttonDelay)

    return keyboard

def getFinalMenu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    buttonStart = KeyboardButton('Еще раз 🔄')
    buttonDelay = KeyboardButton('Поменять задержку ⏲')

    keyboard.add(buttonStart)
    keyboard.add(buttonDelay)

    return keyboard
