import os
import handlers
import callback
from misc import bot
from telebot import types
from flask import Flask, request
from settings.config import TOKEN, WEBHOOK_HOST

app = Flask(__name__)


@app.route('/' + TOKEN, methods=['POST'])
def index():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode('utf-8'))])
    return "ok", 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_HOST + TOKEN)
    return "ok", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
