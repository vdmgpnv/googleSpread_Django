import telebot
from config import TG_TOKKEN


class Bot:
    def __init__(self, TG_TOKKEN = TG_TOKKEN): 
        self.bot = telebot.TeleBot(TG_TOKKEN)


    def send_message(self, msg):
        self.bot.send_message(-789643448, msg, parse_mode="Markdown")