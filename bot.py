import telebot
import CONFIG

from telebot import types

bot = telebot.TeleBot(CONFIG.TOKEN)


@bot.message_handler(commands=['ping'])
def welcome(message):
    print("Received chat id ", message.chat.id)
    reply = str(message.text) + " and " + " pong to you => " + str(message.from_user.username)
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['info'])
def info(message):
	print("Received chat id ", message.chat.id)
	reply = "You are :  " + str(message.from_user.username) + " " + str(message.from_user.first_name)
	bot.send_message(message.chat.id, reply)



bot.polling(none_stop=True)
