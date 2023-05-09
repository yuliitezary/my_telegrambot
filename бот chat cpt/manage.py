import openai
import telebot
#можете изменить api ключ, но можете оставить этот просто вставив токен бота.
openai.api_key = "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"
bot = telebot.TeleBot("6028225386:AAGnM2iWr76I9fSkyRV4pRFJ1Gbi_bSlKXk")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Как я могу Вам помочь?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Расскажи мне о ' + message.text + '?',
        max_tokens=2048,
        n = 1,
        stop=None,
        temperature=0.5,
    )
    bot.reply_to(message, response["choices"][0]["text"])

bot.polling()