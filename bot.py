import telegram
# importe suas chaves de acesso do arquivo credentials.py
from credentials import *
import logging
# para logar erros
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
# crie o bot
bot = telegram.Bot(token=telegram_token)
# mande uma mensagem
bot.sendMessage(chat_id=chat_id, text='cantadas')
você come rato? porque você é um gato
você não é ladrão, mas roubou meu coração
sua mãe é uma ostra? porque você é uma pérola
seu pai é padeiro? porque você é um pão
não sou manu gavassi, mas eu te quero
