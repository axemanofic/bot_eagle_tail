from misc import bot
from telebot.types import CallbackQuery
from utils import dataBase, template_text


@bot.callback_query_handler(func=lambda callback: True)
def set_delay(callback: CallbackQuery):
    dataBase.update_delay(callback.from_user.id, int(callback.data))
    delay = dataBase.get_delay(callback.from_user.id)

    bot.edit_message_text(template_text.TEMPLATE_TEXT['delay'][delay].format(delay),
                          message_id=callback.message.id, chat_id=callback.message.chat.id)

    bot.answer_callback_query(callback.id, text='Установлена задежка {} сек.'.format(callback.data))
