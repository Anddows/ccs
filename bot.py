import time 
from colorama import init
from termcolor import colored
import os
import colors

init()

print(colored("\n\nTelegram bot creator\nClassic Code Script 1.4.0\nby Anddows\n\n", colors.name))
while True:
            inpt = input('*>_ ')
            inpt = inpt.strip()
            if inpt == '{c = telebot.python}':
              try:
                os.mkdir("files")
              except:
                print("opened")
              token = input("{*>_} your token > ")    
              print(colored('{*>_} Scanning...', colors.name))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"import telebot\n\nbot = telebot.TeleBot('{token}')")
              # print(colored('{*>_} successfully', "green"))
              # command1 = input("{*>_} your command > " )
              # print(colored('{*>_} Scanning...', 'red'))
              # time.sleep(3)
              # with open('bot1.py', 'a') as f:
              #    f.write(f"\n\n@bot.message_handler(commands = ['{command1}'])\ndef {command1}_message(message):")
              # print(colored('{*>_} successfully', 'green'))

            elif inpt == "{ccs = help}":
              print(colored("\n\n{*>_} Classic Code Script\nHelp\n\nRename file: {rename.file = w.input}\nDelete file: {del.file = w.name}\n\n", "green"))

            elif inpt == "{del.file = w.name}":
              commanddelete = input("{*>_} your filename for delete > ")
              os.remove(f"{commanddelete}.py")
              print(colored('{*>_} successfully', 'green'))

            elif inpt == "{rename.file = w.input}":
              commandrename = input("{*>_} name for rename file > ")
              os.rename('bot1.py', f'{commandrename}.py')
              print(colored('{*>_} successfully', 'green'))




            elif inpt == '{s = commands}':
              command2 = input("{*>_} your command > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(commands = ['{command2}'])\ndef {command2}_message(message):")

            elif inpt == '{change = color}':
              print(colored("colors see this,\n\n"))
              print(colored("color red", "red"))
              print(colored("color blue", "blue"))
              print(colored("color green", "green"))

              commandchange = input("{*>_} your color for change > ")
              with open("colors.py", "w") as f:
                 f.write(f'name = "{commandchange}"')
              # print(colored('{*>_} successfully', 'green'))
              print(colored('{*>_} Changed!', colors.name))

            elif inpt == '{bot = w.reply}':
              commandreply = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', colors.name))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.reply_to(message, "{commandreply}")')
              # print(colored('{*>_} successfully', 'green'))
              #function 
            elif inpt == '{bot = message["text"]}':
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(content_types = ['text'])\ndef send_message(message):")
              # print(colored('{*>_} successfully', 'green'))

            elif inpt == '{bot = message["photo"]}':
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(content_types = ['photo'])\ndef photo_message(message):")

            elif inpt == '{bot = message["audio"]}':
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(content_types = ['audio'])\ndef audio_message(message):")

              #if 
            elif inpt == "{bot == if}":
              commandif = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   if message.text.lower() == "{commandif}":')
              # print(colored('{*>_} successfully', 'green'))


            elif inpt == "{bot.start == if}":
              commandstart = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   if message.text.lower().startwith("{commandstart}"):')
              # print(colored('{*>_} successfully', 'green'))

            elif inpt == "{bot.start == elif}":
              commandstart2 = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   elif message.text.lower().startwith("{commandstart2}"):')
              # print(colored('{*>_} successfully', 'green'))

            elif inpt == "{bot.delete.message == w.id}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.delete_message(message.chat.id, message.message_id)')
              # print(colored('{*>_} successfully', 'green'))

            elif inpt == "{bot == send}":
              commandsend = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_message(message.chat.id, "{commandsend}")')
              # print(colored('{*>_} successfully', 'green'))

            elif inpt == "{bot == elif}":
              commandif2 = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   elif message.text.lower() == "{commandif2}":')
              print(colored('{*>_} successfully', 'green'))

            elif inpt == "{bot.run = True}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\nbot.polling(none_stop = True)")
              print(colored('{*>_} creating...', 'green'))
              time.sleep(3)
              print(colored('{*>_} successfully created', 'green'))

            elif inpt == "{bot.print == True}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\nprint(message)")

            elif inpt == '{bot == func}':
              commandfunc = input("{*>_} your function name > ")
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\ndef {commandfunc}(message):")

            elif inpt == "{bot == if.message}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n   if message.text:")

            elif inpt == "{bot == else}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n   else:")

            elif inpt == '{bot == ban.user["id = w.reply"]}':
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)")

            elif inpt == '{bot == unban.user["id = w.reply"]}':
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)")

            elif inpt == '{bot == unmute.user["id = w.reply"]}':
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)")


            elif inpt == '{bot == kick.user["id = w.reply", to]}':
              commandban2 = input("{*>_} ban to >")
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, message.date + {commandban2})")


            elif inpt == '{bot == mute.user["id = w.reply"]}':
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.restric_chat_member(message.chat.id, message.reply_to_message.from_user.id)")

            elif inpt == '{bot == ban.user["id = w.reply", to]}':
              commandmute2 = input("{*>_} mute to >")
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n            bot.restric_chat_member(message.chat.id, message.reply_to_message.from_user.id, message.date + {commandmute2})")



            elif inpt == "{bot == elif.message}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n   elif message.text:")

            elif inpt == "{bot == reg.hand}":
              commandhand = input("{*>_} your command > ")
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n         bot.register_next_step_handler(text, {commandhand})")

            elif inpt == "{text = bot.send}":
              commandtext = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n         text = bot.send_message(message.chat.id, "{commandtext}")')

            elif inpt == '{bot = keyboard.button["True"]}':
              commandbutton = input('{*>_} your button name > ')
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n{commandbutton} = telebot.types.ReplyKeyboardMarkup(True)')

            elif inpt == "{bot.button = name}":
              commandkey = input('{*>_} your button name > ')
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n{commandkey}.row(')
              print(colored("{*>_} Scanning...", 'red'))
              # time.sleep(3)
              # with open('bot1.py', 'a') as f:
              #    f.write(f'{commandkey2}"')

            elif inpt == "{bot.button.add = text}":
              commandkey3 = input("{*>_} your button text > ")
              print(colored("{*>_} Scanning...", 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f' "{commandkey3}"')

            elif inpt == ",":
              print(colored("Scanning...", 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f',')


            elif inpt == ")":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f')')

            elif inpt == "{bot.replybutton = send}":
              commandsendbutton = input('{*>_} your text > ')
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_message(message.chat.id, "{commandsendbutton}",')
              commandreplybutton = input('{*>_} your button name reply > ')
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f' reply_markup = {commandreplybutton})')

            elif inpt == "{bot == send.photo}":
              commandphoto = input('{*>_} your photo name > ')
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_photo(message.chat.id, photo = open("files/{commandphoto}", "rb"))')

            elif inpt == "{bot == send.audio}":
              commandaudio = input('{*>_} your audio name > ')
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_audio(message.chat.id, audo = open("files/{commandaudio}", "rb"))')

            elif inpt == "{bot == send.animation}":
              commandaudio = input('{*>_} your animation name > ')
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_audio(message.chat.id, animation = open("files/{commandaudio}", "rb"))')

            elif inpt == "{bot.message.pin == w.id}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.pin_message(message.chat.id, message.message_id')

            elif inpt == "{bot.message.unpin == w.id}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(3)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.unpin_message(message.chat.id, message.message_id')
              # print(colored('{*>_} successfully', 'green'))

            else:
              print(colored(f'*>_ CommandError: command <{inpt}> not defined', colors.name))
            
           
