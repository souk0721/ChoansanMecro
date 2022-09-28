
import telegram
import config

bot = telegram.Bot(token=config.telegram_token)
chat_id = config.telegram_channel


def telegram_send_message(messange):
    bot.sendMessage(chat_id=chat_id, text=messange)
    
    
    