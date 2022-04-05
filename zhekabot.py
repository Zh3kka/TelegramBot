import telebot
import random
from telebot import types

BOT_TOKEN = '5285105897:AAGgC3XX6Hr_EDGa7JmaauIxZTUlA4-SSYM'  # токен телеграмма
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🎲 Рандомное число')
    item2 = types.KeyboardButton('😊 Как дела?')
    item3 = types.KeyboardButton('⛽️ Калькулятор топлива')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный Господином.\nВот кстати его страничка ВК - https://vk.com/za1kano'.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text__message(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Хорошо', callback_data='good')
            item2 = types.InlineKeyboardButton('Не очень', callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(
                message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == '⛽️ Калькулятор топлива':
            bot.send_message(message.chat.id, 'Данный функционал находится в разработке')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить(')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'good':
            bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
        elif call.data == 'bad':
            bot.send_message(call.message.chat.id, 'Бывает 😢')

        # удаление инлайн кнопок
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='😊 Как дела?',
                              reply_markup=None)


# запуск бота
bot.polling(none_stop=True)
