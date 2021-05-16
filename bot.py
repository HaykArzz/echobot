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
    error_message = 'Did not found capital: /info country name'
    try:
      city = dictionary.thisdict[(data[1])]
      if not city:
        reply = "Did not find, please try again"
      else:
        reply = "Your capital is :  " + str(city)
        bot.send_message(message.chat.id, reply)
    except:
       print("Error happened")
       bot.send_message(message.chat.id, error_message)


bot.polling(none_stop=True)








