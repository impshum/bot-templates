import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import configparser


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read('conf.ini')
telegram_api_key = config['TELEGRAM']['telegram_api_key']
telegram_admin = config['TELEGRAM']['telegram_admin']
telegram_admin = '@{}'.format(telegram_admin)


def error(update, context):
    logger.warning('{}\n{}'.format(update, context.error))
    msg = context.error
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    print(msg)


def help(update, context):
    msg = 'Need help?'
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    print(msg)
    

def main():
    updater = Updater(telegram_api_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler(
        'help', help, Filters.user(username=telegram_admin)))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
