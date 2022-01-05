from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update


def start(update: Update, context: CallbackContext):
    # print('json file update : ' ,update)
    # print("json file bot : ', bot)
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    print("chat_id : {} and firstname : {} lastname : {}  username {}". format(chat_id, first_name, last_name , username))
    context.bot.sendMessage(chat_id, f'telegram_id:{chat_id}\nfirst_name:{first_name}')

def main():
    updater = Updater(token = '2058897666:AAG67ewdPuakUffXbAMeLBwf8hlR7KlBDXk')
    start_command = CommandHandler('start',start)
    updater.dispatcher.add_handler(start_command)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()