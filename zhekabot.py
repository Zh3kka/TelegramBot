import telebot

BOT_TOKEN = '5285105897:AAGgC3XX6Hr_EDGa7JmaauIxZTUlA4-SSYM' #токен телеграмма
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет<b>', parse_mode='html')




bot.polling(none_stop=True)