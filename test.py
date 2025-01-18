import telebot

# قم باستبدال "YOUR_BOT_TOKEN" بالتوكن الذي حصلت عليه من BotFather
bot = telebot.TeleBot("7729550329:AAHSBYDdMJejeooBkzKXUSgavT-kzL9Za3U")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "DAM")

bot.polling()