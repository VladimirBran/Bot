import telebot


TOKEN = '5427589232:AAGPStNNg2-S4-_sSyxV6O0xqUp9CRIt86o'


bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Hello')

bot.polling()
