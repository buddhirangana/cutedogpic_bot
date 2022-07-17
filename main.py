from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "This bot will send you a random dog image when you type /dog command.")

def dog(update, context: CallbackContext):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    TOKEN = 'BOT_TOKEN'
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('dog', dog))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
