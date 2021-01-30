import handlers
import callback
from misc import bot
from telebot import types
from flask import Flask, request
from flask_sslify import SSLify
from settings.config import TOKEN

app = Flask(__name__)
sslify = SSLify(app)


@app.route('/()'.format(TOKEN), methods=['post'])
def index():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode('utf-8'))])
    return "ok", 200


if __name__ == '__main__':
    app.run()
