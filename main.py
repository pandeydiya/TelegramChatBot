import logging
# to visualise error or message data.
from telegram.ext import *
import Responses

API_KEY = '1951922754:AAFmKaEbTn9FhysyzmqrgTbcECZvfNdDIjY'

# set up the logging !!! >_<
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')
    # what happens when the user types /start.
    # context is used for backward compatibility into the documentation.


def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')
    # what happens when the user types /help.
    # context is used for backward compatibility into the documentation.


def custom_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot.')
    # what happens when the user types /start.
    # context is used for backward compatibility into the documentation.


# we will create a message handler. What happens when user sends messages to the chatbot.
def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = Responses.get_response(text)
    update.message.reply_text(response)
    # so that bot can give us the expected response!


# function that handles the errors.
def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    # dispatcher used to register the handler + usable.
    dp = updater.dispatcher

    # commands for dispatcher:
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))


    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # commands to start our bot and it runs continuously:
    # Run the bot
    updater.start_polling(1.0)  # new updates every 1.0 sec.
    updater.idle()  # runs continuously!!
