import telebot
import config
import dictionary
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def info(message):
    print("Received chat id ", message.chat.id)
    reply = "Please type /info country name :  "
    bot.send_message(message.chat.id, reply)

@bot.message_handler(commands=['info'])
def info(message):
    print("Received chat id ", message.chat.id)
    data = message.text.split(' ', 2)
    city = dictionary.thisdict[(data[1])]
    if city != 'null':
      reply = "Your capital is :  " + str(city)
    else:
        reply = "Did not find"
    bot.send_message(message.chat.id, reply)

bot.polling(none_stop=True)








