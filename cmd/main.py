#6814411666:AAHOJaQomEB7fx8AvE6lOyAYADSv-g4-5GI
import logging

from handlers import start
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6814411666:AAHOJaQomEB7fx8AvE6lOyAYADSv-g4-5GI').build()

    start_handler = CommandHandler('menu', start.but)

    application.add_handler(CallbackQueryHandler(start.button))
    application.add_handler(start_handler)

    application.run_polling()

