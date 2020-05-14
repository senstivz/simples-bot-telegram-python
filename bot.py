import telegram
# credentials.py.sample *
import logging
# para logar erros
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
# crie o bot
bot = telegram.Bot(token=telegram_token)
# mande uma mensagem
bot.sendMessage(chat_id=chat_id, text='O bot diz oi!')
