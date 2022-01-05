from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import logging
import datetime

from base.models import Event, Telegram


#serve para enviar os erros que o bot cometeu
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, Welcome to calendrive!\nPlease /login before continue")


def login(update, context):
    # passes text_login as an argument
    text_login = ' '.join(context.args)
    chat_id = update.message.chat_id
    if Telegram.objects.filter(token=text_login):

        obj = Telegram.objects.get(token=text_login)
        date_time = obj.created
        time_add = datetime.timedelta(minutes=5)
        new_time = date_time + time_add
        obj.save()

        keyboard = []
        # saves the telegram_id of the telegram_user
        if Telegram.objects.filter(updated__lte=new_time):
            obj.telegram_id = chat_id
            obj.save()
        
            keyboard = [
            ['Disponibilidade'],
            ]

            username = obj.user
            reply_text = f'Welcome {username}, please select to continue!'

        else:
            reply_text = 'expired token time'
        
        reply_markup = ReplyKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text, reply_markup=reply_markup)
     
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'invalid token for {text_login}')
    

def echo(update, context):
    text = update.message.text
    chat_id = update.message.chat_id
    
    
    if Telegram.objects.filter(telegram_id=chat_id):
        obj = Telegram.objects.get(telegram_id=chat_id)
        username = obj.user
        
        event_pretext = 'event_type'
        
        keyboard = [
        ['Disponibilidade'],
        ]


        if text == 'Disponibilidade':

            eventos = Event.objects.filter(user=username)
            reply_text = 'Select one event type\n'
            keyboard = [
            [event_pretext + evento.name] for evento in eventos
            ]

        elif text.startswith(event_pretext):
            evento_name = text.replace(event_pretext,'')

            reply_text = f'There is your data for {evento_name}:\n'
            evento = Event.objects.filter(name__startswith=evento_name)
            for e in evento:
                reply_text += f'Duration:{e.duration}\nDescription:{e.description}' 

        else:
            reply_text = f'Welcome back {username}!\nPlease select to continue'


        reply_markup = ReplyKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text, reply_markup=reply_markup)

    else:
        reply_text = 'Please /login before you continue'
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def main() -> None:
    updater = Updater(token = '2058897666:AAG67ewdPuakUffXbAMeLBwf8hlR7KlBDXk')

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    

    login_handler = CommandHandler('login', login)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    
    unknown_handler = MessageHandler(Filters.command, unknown)
    
    dispatcher.add_handler(start_handler)

    
    dispatcher.add_handler(login_handler)
    dispatcher.add_handler(echo_handler)
    
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()