import telebot

#token = '5771511493:AAGH9dp6FDBn4E4wOpXoCoEzcdF5w8MAoac'
import telepot
from telepot.loop import MessageLoop

TOKEN = '5771511493:AAGH9dp6FDBn4E4wOpXoCoEzcdF5w8MAoac'
bot = telepot.Bot(TOKEN)

def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"]
    try:
        answer = eval(text)
    except:
        answer = "Can't calculate :("
    bot.sendMessage(chat_id, "answer: {}".format(answer))


MessageLoop(bot, handle).run_as_thread()

while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break