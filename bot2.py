import telebot
import config
import dictionary1
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['Start'])
def info(message):
    print("Received chat id ", message.chat.id)
    reply = "Please type /Contact Contact name :  "
    bot.send_message(message.chat.id, reply)

@bot.message_handler(commands=['Contact'])
def info(message):
    print("Received chat id ", message.chat.id)
    data = message.text.split(' ', 2)
    error_message = 'Did not found contact: /Contact Contact name'
    try:
        Contact = dictionary1.thisdict1[(data[1])]
        if not Contact:
            reply = "Did not find, please try again"
        else:
            reply = "Your Contact number is is :  " + str(Contact)
            bot.send_message(message.chat.id, reply)
    except:
        print("Error happened")
        bot.send_message(message.chat.id, error_message)


bot.polling(none_stop=True)






