from misc import bot
from utils import dataBase
from utils import functions
from telebot.types import Message
from utils.global_var import STICKERS
from keyboards.reply import getFinalMenu
from keyboards.inline import getInlineMenu
from utils import template_text


@bot.message_handler(content_types=['text'])
def start(message: Message):
    if message.text in ['Подбросить монетку 👋', 'Еще раз 🔄']:
        delay = dataBase.get_delay(message.from_user.id)
        functions.loopTossing(message, delay)
        sticker, num = functions.getSticker()
        bot.send_sticker(message.from_user.id, sticker, reply_markup=getFinalMenu())
        dataBase.update_score(message.from_user.id, STICKERS[num][1])
    elif message.text in ['Установить задержку ⏲', 'Поменять задержку ⏲']:
        delay = dataBase.get_delay(message.from_user.id)
        bot.send_message(message.from_user.id, template_text.TEMPLATE_TEXT['delay'][delay].format(delay),
                         reply_markup=getInlineMenu())
    else:
        bot.send_message(message.from_user.id, 'Простите, но я Вас не понимаю')
