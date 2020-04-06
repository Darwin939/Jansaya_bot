import telebot
from time import sleep
from os import walk
import os
from random import randint
token = "1176509668:AAGekk7qHlqvRYuor-ONPkGsUF3fgmWXPZk"
bot = telebot.TeleBot(token)

base_dir = os.path.abspath(os.path.dirname(__file__))
picture_file = os.path.join(base_dir, 'pictures')

folder = []
w = walk(picture_file)
for i in w:
    folder.append(i)

images = folder[0][2]

while True:
    file_name = open('text.txt','r')
    users = []
    for line in file_name:
        users.append(line)
    for user in users:
        tmp  = images[randint(0,(len(images)-1))]
        image = os.path.join(picture_file, tmp)
        photo = open(image,'rb')
        
        bot.send_photo(user,photo)
        photo.close()
        
        sleep(1000)
