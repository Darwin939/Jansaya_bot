import telebot

token = "1176509668:AAGekk7qHlqvRYuor-ONPkGsUF3fgmWXPZk"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi Zhansaya! every day (at regular intervals) I will send you pictures from LOVE IS  ')
    f = open('text.txt', 'w')
    f.write(str(message.chat.id) + '\n')
    f.close()
    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, "Жди , я сам напишу ...")



if __name__ == '__main__':
     bot.polling()