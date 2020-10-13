# libs import
import telebot
import datetime

from functions import (
    check_weekend,
    get_closest_salary_date,
    get_prize_date
)
    

# token of bot
TOKEN="1113559467:AAHCHxrL39NR2cMqvfxi02GsrgUVdG7JHOU"
bot = telebot.TeleBot(TOKEN)

# keyboard
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row(
    'Когда ЗП?', 
    'Когда премия?'
)
keyboard1.row('О боте')

# start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я могу подсказать когда придет следующая ЗП или премия.', reply_markup=keyboard1)

date = datetime.date.today()

# easter egg
gus = """
ЗАПУСКАЕМ
░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
▄███▀░◐░░░▌░░░░░░░
░░░░▌░░░░░▐░░░░░░░
░░░░▐░░░░░▐░░░░░░░
░░░░▌░░░░░▐▄▄░░░░░
░░░░▌░░░░▄▀▒▒▀▀▀▀▄
░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
░░░░░░░░░░░▌▌▌▌░░░░░
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░▄▄▌▌▄▌▌░░░░░
"""
    
# response to buttons 
@bot.message_handler(content_types=['text'])
def send_text(message):
    
    if message.text == 'Когда ЗП?':
        bot.send_message(message.chat.id, get_closest_salary_date(date))
        
    elif message.text == 'Когда премия?':
        bot.send_message(message.chat.id, get_prize_date(date))
        
    elif message.text == 'О боте':
        bot.send_message(message.chat.id, 'Этот бот существует только потому, что @dimanoga не может запомнить когда приходит ЗП. \nСоздтаель - @Cormac117')
        
    elif message.text.lower() == 'запусти гуся':
        bot.send_message(message.chat.id, gus)


    else:
        bot.send_message(message.chat.id, 'Используй кнопки!')
        
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
    
if __name__ == '__main__':
    bot.polling()