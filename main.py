# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess

import telebot

TOKEN = '2025832214:AAHEk3ZFcxsh1PQ4B_BbZkPsDE41KIhQhOg'
PATH_TO_CALCULATOR = '/home/denis/Repos/MyRepo/TelBot/Calculator'''
PATH_TO_CALCULATOR = "E:\Programming\MyPythonRepo\TelegramBot\Calculator.exe"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    name = message.text
    #list = PATH_TO_CALCULATOR + name
    process = subprocess.run([PATH_TO_CALCULATOR, name], capture_output=True, text=True)
    print(process.stdout)
    #bot.send_message(message.chat.id, f'Привет, {name}. Рад тебя видеть.')
    bot.send_message(message.chat.id, process.stdout)

@bot.message_handler()
def start(message):
    name = message.text
    process = subprocess.run([PATH_TO_CALCULATOR, name], capture_output=True, text=True)
    bot.send_message(message.chat.id, process.stdout)

def print_hi(name):
    #subprocess.call([PATH_TO_CALCULATOR])
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


bot.polling()

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #process = subprocess.([PATH_TO_CALCULATOR])
#    process = subprocess.run(PATH_TO_CALCULATOR, capture_output=True, text=True)
#    print(process.stdout)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
