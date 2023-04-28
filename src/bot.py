import os

import telebot
from loguru import logger
from telebot import types
import emoji


from src.constants import keyboards


class bot:
    """
    template for bot.
    
    """
    def __init__(self):
    	self.bot = telebot.TeleBot(os.environ["template_bot_token"])
    	self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)

    def run(self):
    	logger.info("bot is running...")
    	self.bot.infinity_polling()
    def echo_all(self, message):
        #write_json(message.json, 'message.json')
        print(emoji.demojize(message.text))
        self.bot.send_message(message.chat.id,
                              message.text,
                              reply_markup=keyboards.main
        )
        
if __name__ == '__main__':
    logger.info('bot started')
    bot = bot()
    bot.run()







