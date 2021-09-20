"""
Github : @TNAlotaibi ...
i hope u don't clear my rights
All you have to do..
step 1 : get token for the bot From @BotFather in Telegram.

step 2 : Get ID for the channel .. Something Wrong in this step
you need to send test message and to add the bot in channel to get id for send on POST method

Use this url -->  https://api.telegram.org/bot<token>/getUpdates

And Get the ID, i think is begin with ( - )
if u got it, put it in line 44

Note !!

Put it between the --> ''
Example :
            'chat_id': '-12345', 'text': message

if You don't install requests package do it before run this script
"""

from threading import Thread
import random
import requests
import time

file_text = open("a4kar.txt", 'r', encoding='UTF-8').read().splitlines()
num = 0
url_tele = 'https://api.telegram.org/bot<token>/sendMessage'


def send(message):
    global num
    data = {
            'chat_id': 'ID Channel ', 'text': message
        }
    if requests.post(url_tele, data=data).text:
            num += 1
            print("Message --> [ ", num, " ]", end="\r")


def main():
    # 3600 sec = 1hour
    # 3600 * 2 = 2hours   ---> [ 2 ]  = num of hours
    sleep = 3600 * 2
    sleep2 = 3600 * 5
    while True:
        for msg in file_text:
            send(msg)
            time.sleep(random.randint(sleep, sleep2))


Thread(target=main).start()
