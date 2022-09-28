
import telegram
import config

bot = telegram.Bot(token=config.telegram_token)
chat_id = config.telegram_channel

bot.sendMessage(chat_id=chat_id, text="테스트 완료")