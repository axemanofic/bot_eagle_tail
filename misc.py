from telebot import TeleBot
from settings.config import TOKEN, WEBHOOK_HOST

bot = TeleBot(token=TOKEN, parse_mode='html')
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_HOST.format(TOKEN))