
import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🎧 مرحبا كليـﭙسو! بوت Sonickly جاهز 🎶")

@bot.message_handler(commands=['جلسة'])
def send_session(message):
    bot.send_message(message.chat.id, "🔊 جلستك قادمة برابط FLAC قريباً...")

bot.polling()
