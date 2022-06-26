from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from telegram.ext.dispatcher import run_async
from telegram import Update, Bot
import requests
import re
import json
import logging

def selectnft(update: Update, context: CallbackContext):
    update.message.reply_text(text='Please state the project name in OpenSea:')

def getnft(update: Update, context: CallbackContext):
    book_name = update.message.text
    book_name = str.lower(book_name)
    answer = f'You have wrote me {book_name}'  
    update.message.reply_text(answer)
    text = get_url(book_name)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def get_url(nftname):
    contents = requests.get('https://api.opensea.io/collection/'+nftname).json()
    # print(contents)
    url = contents['collection']['stats']['floor_price']
    result = json.dumps(url)
    print(result)
    return "The floor price is: " + result

# def telegram_bot_sendtext(bot_message):

#    bot_token = '5102417025:AAFlzOfYv9F5Y0EwfMXerwXWckRZ17D7kw0'
#    bot_chatID = '3560469'
#    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

#    response = requests.get(send_text)

#    return response.json()

# text = get_url()
# test = telegram_bot_sendtext(text)
# print(test)

# def bop(update: Update, context: CallbackContext):
#     url = get_url()
#     # chat_id = update.message.chat_id
#     # bot.send_photo(chat_id=chat_id, photo=url)1
#     update.message.reply_text(url)

def main():
    updater = Updater('5102417025:AAF-A8OAkPxJDzFwV8JrZzCXhicbe_0RAI8', use_context=True)
    dp = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    # dp.add_handler(CommandHandler('bop',bop))
    start_handler = CommandHandler('selectnft', selectnft)
    dp.add_handler(start_handler)
    dp.add_handler(MessageHandler(Filters.text, getnft))
    updater.start_polling()
    # updater.idle()

if __name__ == '__main__':
    main()