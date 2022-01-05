import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, 
CommandHandler, CallbackContext, CallbackQueryHandler,
ConversationHandler)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND, THIRD = range(3)
# Callback data
ONE, TWO, THREE, FOUR, FIVE = range(5)

def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("Disponibilidade", callback_data=str(ONE)),
        ],
        [
            InlineKeyboardButton("Web", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text(f"Hi {user.first_name}, what can i do for you?", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST

def one(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Python Class", callback_data=str(THREE)),
        ],
        [
            InlineKeyboardButton("Django Class", callback_data=str(FOUR)),
        ],
        [
            InlineKeyboardButton("Business Meeting", callback_data=str(FIVE)),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text='Please choose an Event type:', reply_markup=reply_markup)

    return SECOND

def two(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    
    query.edit_message_text(text='http://127.0.0.1:8000/')

def three(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    
    query.edit_message_text(text='Python Class \n Time: 60 minuts \n Description: Some description')

def four(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    
    query.edit_message_text(text='Django Class \n Time: 60 minuts \n Description: Some description')

def five(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    
    query.edit_message_text(text='Business Meeting \n Time: 30 minuts \n Description: Some')


def web_command(update: Update, context: CallbackContext) -> None:
    """Returns the webadmin."""
    update.message.reply_text('http://127.0.0.1:8000/')

def disponibilidade_command(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Python Class", callback_data='Python Class \n Time: 60 minuts \n Description: Some description'),
        ],
        [
            InlineKeyboardButton("Django Class", callback_data='Django Class \n Time: 60 minuts \n Description: Some description'),
        ],
        [
            InlineKeyboardButton("Business Meeting", callback_data='Business Meeting \n Time: 30 minuts \n Description: Some')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose an Event type:', reply_markup=reply_markup)

    return THIRD


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"Selected Event type: {query.data}")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    token = '2058897666:AAG67ewdPuakUffXbAMeLBwf8hlR7KlBDXk'
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram

    # dispatcher.add_handler(CommandHandler("web", web_command))
    # dispatcher.add_handler(CommandHandler('disponibilidade', disponibilidade_command))
    # dispatcher.add_handler(CallbackQueryHandler(button))

     # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            ],
        states={
            FIRST: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(five, pattern='^' + str(FIVE) + '$'),
            ],
            THIRD: [
                CallbackQueryHandler(button),
            ],
        },
        fallbacks=[
            CommandHandler('start', start),
            CommandHandler('web', web_command),
            CommandHandler('disponibilidade', disponibilidade_command),
            CallbackQueryHandler(button),            
            ],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)



    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()