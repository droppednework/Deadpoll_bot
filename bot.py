# 1523900337:AAHKqm8Y6y2yjXQ0NRaMIIq6LFr5zJLAWoU
#@bot.message_handler(content_types=['text','start', 'help']) пример для работы с сообшениями

import telebot
from telebot import types
from telebot.apihelper import send_message

bot = telebot.TeleBot('1710481509:AAGgrt_QmJWOXJzZM9digQ4ttnyofvLFW38')

@bot.message_handler(content_types=['text'])
def menu(message): # Тут стартовое меню
    start_menu = types.ReplyKeyboardMarkup(True,True)
    start_menu.row('Проблема с пк','Проблема с оп','Проблема с телефонией')
    start_menu.row('Проблем нет')
    bot.send_message(message.chat.id, 'Привет, что у тебя за проблема', reply_markur=start_menu)

@bot.message_handler(content_types=['text'])
def menu_problem(message): # Тут перебираються все проблемы
    if message.text == 'Проблема с пк':
        bot.send_message(message.chat.id, 'У тебя проблема с пк', reply_markur=problem_PC_list)# поискать как сделать переход с сообщения на функцию
    elif message.text == 'Проблема с оп':
        bot.send_message(message.chat.id, 'У тебя проблема с оп')
    elif message.text == 'Проблема с телефонией':
        bot.send_message(message.chat.id, 'У тебя проблема с телефонией')
    elif message.text == 'Проблем нет':
        menu(message)

@bot.message_handler(content_types=['text'])
def problem_PC_list (message = ['text']): # Тут перебираються проблемы с пк
    start_menu = types.ReplyKeyboardMarkup(True,True)
    start_menu.row('Проблема с включение','Включен, но не грузит')
    start_menu.row('Проблема иного рода', 'Проблемы нет')
    bot.send_message(message.chat.id, reply_markur=start_menu)


@bot.message_handler(content_types=['text'])
def problem_on(message = ['text']):
    if message.text == 'Проблема с включение':
        return 1
#Сюда будет помещаться алгоритм с перебором решения проблемы


#@bot.message_handler(content_types=['text'])
#def problem_OP (content_types = ['text']): # Тут перебираються проблемы с ПО

#@bot.message_handler(content_types=['text'])
#def problem_telefonia (content_types = ['text']): # Тут перебираються проблемы с телефонией
if __name__ == '__main__':
    bot.infinity_polling()

    



