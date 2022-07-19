import time 
from colorama import init
from termcolor import colored
import os

init()


commandopen = "("
commandclose = ")"
commandpoint = "."
commandpoint2 = ","

create_t = ["{c = telebot.python}", "c = telebot.python"]
ccs = ["{ccs = help}", "ccs = help", "$ccs"]
files1 = ["{del.file = w.name}", "del.file = w.name"]
files2 = ["{rename.file = w.input}", "rename.file = w.input"]
commands = ["{s = commands}", "s = commands"]
write2 = ["{*write}", "*write"]
class1 = ["{c = class}", "c = class"]
func1 = ["{c = func}", "c = func"]
variable1 = ["{c = variable}", "c = variable"]
i_time = ["{i = time}", "i = time"]
t_sleep = ["{t = sleep}", "t = sleep"]
change_c = ["{change = color}", "change = color"]
reply1 = ["{bot = w.reply}", "bot = w.reply"]
message_t = ['{bot = message["text"]}', 'bot = message["text"]']
new_chat = ['{bot = message.new.member["chat"]}', 'bot = message.new.member["chat"]']
left_chat = ['{bot = message.left.member["chat"]}', 'bot = message.left.member["chat"]']
message_photo = ['{bot = message["photo"]}', 'bot = message["photo"]']
message_audio = ['{bot = message["audio"]}', 'bot = message["audio"]']
bot_if = ['{bot == if}', 'bot == if']
bot_start_if = ['{bot.start = if}', 'bot.start = if']
bot_start_elif = ["{bot.start == elif}", "bot.start == elif"]
delete_message1 = ["{bot.delete.message == w.id}", "bot.delete.message == w.id"]
bot_send = ["{bot == send}", "bot == send"]
bot_elif = ["{bot == elif}", "bot == elif"]
run = ["{bot.run = True}", "bot.run = True"]
bot_if_message = ["{bot == if.message}", "bot == if.message"]
bot_elif_message = ["{bot == elif.message}", "bot == elif.message"]
bot_else = ["{bot == else}", "bot == else"]
bot_ban = ['{bot == ban.user["id = w.reply"]}', 'bot == ban.user["id = w.reply"]']
bot_mute = ['{bot == mute.user["id = w.reply"]}', 'bot == mute.user["id = w.reply"]']
bot_kick = ['{bot == kick.user["id = w.reply", to]}', 'bot == kick.user["id = w.reply", to]']
bot_mute_to = ['{bot == mute.user["id = w.reply", to]}', 'bot == mute.user["id = w.reply", to]']
bot_unmute = ['{bot == unmute.user["id = w.reply"]}', 'bot == unmute.user["id = w.reply"]']
bot_unban = ['{bot == unban.user["id = w.reply"]}', 'bot == unban.user["id = w.reply"]']
reg_hand = ["{bot == reg.hand}", "bot == reg.hand"]
text_bot_send = ["{text = bot.send}", "text = bot.send"]
button = ['{bot = keyboard.button["True"]}', 'bot = keyboard.button["True"]']
button_name = ["{bot.button = name}", "bot.button = name"]
button_add = ["{bot.button.add = text}", "bot.button.add = text"]
reply_button = ["{bot.replybutton = send}", "bot.replybutton = send"]
send_photo = ["{bot == send.photo}", "bot == send.photo"]
send_audio = ["{bot == send.audio}", "bot == send.audio"]
send_animation = ["{bot == send.animation}", "bot == send.animation"]
bot_pin = ["{bot.message.pin == w.id}", "bot.message.pin == w.id"]
bot_unpin = ["{bot.message.unpin == w.id}", "bot.message.unpin == w.id"]
bot_custom_admin = ["{bot.s.custom.admin = name.admin}", "bot.s.custom.admin = name.admin"]
bot_admin = ['{bot = l.admin["w.reply"]}', 'bot = l.admin["w.reply"]']
bot_description = ['{bot = s.description["chat"]}', 'bot = s.description["chat"]']
bot_title = ['{bot = s.title["chat"]}', 'bot = s.title["chat"]']
bot_useful = ["{#useful}", "#useful"]
bot_send_id = ["{bot == send.id}", "bot == send.id"]
bot_poll_answer = ["{bot == send.poll}", "bot == send.poll"]
bot_comment = ["{#comment}", "#comment"]
bot_clear = ["{ccs = clear}", "ccs = clear"]
bot_open1 = ["{bot == w.open > write}", "bot == w.open > write"]
bot_open2 = ["{bot == a.open > write}", "bot == a.open > write"]
ccs_read = ["{ccs = read}", "ccs = read"]
bot_bold = ["{bot == send.bold}", "bot == send.bold"]
bot_mono = ["{bot == send.monospace}", "bot == send.monospace"]
bot_link = ["{bot == send.link}", "bot == send.link"]

with open("colors.txt", "w") as f:
  f.write('green')
with open("colors.txt", "r+") as f:
  list = f.read()
print(colored("\n\nTelegram bot creator\nClassic Code Script 1.11\nby Code Idea\n\n", list))
while True:
            inpt = input('*>_ ')
            inpt = inpt.strip()
            if inpt in create_t:
              try:
                os.mkdir("files")
              except:
                with open("colors.txt", "r+") as f:
                 list = f.read()
                print(colored('{*>_} Scanning...', list))
                with open("colors.txt", "r+") as f:
                 list = f.read()
              token = input("{*>_} your token > ")    
              print(colored('{*>_} Scanning...', list))
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

            elif inpt in ccs:
              with open("colors.txt", "r+") as f:
                 list = f.read()
              print(colored("\n\n{*>_} Classic Code Script\nHelp\n\nRename file: {rename.file = w.input}\nDelete file: {del.file = w.name}\n\n", list))

            elif inpt in files1:
              commanddelete = input("{*>_} your filename for delete > ")
              os.remove(f"{commanddelete}.py")
              print(colored('{*>_} successfully', 'green'))

            elif inpt in files2:
              commandrename = input("{*>_} name for rename file > ")
              os.rename('bot1.py', f'{commandrename}.py')
              print(colored('{*>_} successfully', 'green'))


            elif inpt in bot_clear:
              clear = lambda: os.system('clear')
              clear()


            elif inpt in commands:
              command2 = input("{*>_} your command > " )
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(commands = ['{command2}'])\ndef {command2}_message(message):")

            elif inpt in write2:
              commandwrite = input('{*>_} your text > ')
              with open("colors.txt", "r+") as f:
                 list = f.read()
              print(colored(f'*>_ {commandwrite}', list))

            elif inpt in class1:
              commandclass = input('{*>_} input name > ')
              with open("colors.py", "w") as f:
                f.write(f'class {commandclass}\n')

            elif inpt in func1:
              commandfunc2 = input("{*>_} input name > ")
              with open('bot1.py', 'a') as f:
                 f.write(f"def {commandfunc2}\n")

            elif inpt in variable1:
              commandvariables = input("{*>_} your variable name >")
              with open('bot1.py', 'a') as f:
                 f.write(f"\n{commandvariables} = ")
              commandvariables2 = input("your variable > ")
              with open('bot1.py', 'a') as f:
                 f.write(f"\n{commandvariables2}")

            elif inpt in i_time:
              with open('bot1.py', 'a') as f:
                f.write('\nimport time\n')

            elif inpt in t_sleep:
              commandtime = input("{*>_} input time > ")
              with open('bot1.py', 'a') as f:
                f.write(f'\ntime.sleep({commandtime})\n')


              


            elif inpt in change_c:
              print(colored("colors see this,\n\n"))
              print(colored("color red", "red"))
              print(colored("color blue", "blue"))
              print(colored("color green", "green"))

              commandchange = input("{*>_} your color for change > ")
              with open("colors.txt", "w") as f:
                 f.write(commandchange)
              with open("colors.txt", "r+") as f:
                 list = f.read()
              # print(colored('{*>_} successfully', 'green'))
              print(colored('{*>_} Changed!', list))

            elif inpt in reply1:
              commandreply = input("{*>_} your text > " )
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.reply_to(message, "{commandreply}")')
              # print(colored('{*>_} successfully', 'green'))
              #function 
            elif inpt in message_t:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(content_types = ['text'])\ndef send_message(message):")


            elif inpt in new_chat:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(content_types = ['new_chat_members'])\ndef new_member_message(message):")
              # print(colored('{*>_} successfully', 'green'))

            elif inpt in left_chat:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(content_types = ['left_chat_member'])\ndef left_member_message(message):")

            elif inpt in message_photo:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(content_types = ['photo'])\ndef photo_message(message):")

            elif inpt in message_audio:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(content_types = ['audio'])\ndef audio_message(message):")

              #if 
            elif inpt in bot_if:
              commandif = input("{*>_} your text > " )
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   if message.text.lower() == "{commandif}":')
              # print(colored('{*>_} successfully', 'green'))


            elif inpt in bot_start_if:
              commandstart = input("{*>_} your text > " )
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   if message.text.lower().startwith("{commandstart}"):')
              # print(colored('{*>_} successfully', 'green'))

            elif inpt in bot_start_elif:
              commandstart2 = input("{*>_} your text > " )
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   elif message.text.lower().startwith("{commandstart2}"):')
              # print(colored('{*>_} successfully', 'green'))

            elif inpt in delete_message1:
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.delete_message(message.chat.id, message.message_id)')
              # print(colored('{*>_} successfully', 'green'))

            elif inpt in bot_send:
              commandsend = input("{*>_} your text > " )
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_message(message.chat.id, "{commandsend}")')
              # print(colored('{*>_} successfully', 'green'))

            elif inpt in bot_elif:
              commandif2 = input("{*>_} your text > " )
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   elif message.text.lower() == "{commandif2}":')
              print(colored('{*>_} successfully', 'green'))

            elif inpt in run:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\nbot.polling(none_stop = True)")
              print(colored('{*>_} creating...', 'green'))
              time.sleep(3)
              print(colored('{*>_} successfully created', 'green'))

            elif inpt == "{\n         bot.print == True}":
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\nprint(message)")

            # elif inpt == '{bot == func}':
            #   commandfunc = input("{*>_} your function name > ")
            #   with open('bot1.py', 'a') as f:
            #      f.write(f"\n\ndef {commandfunc}(message):")

            elif inpt in bot_if_message:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n   if message.text:")

            elif inpt in bot_else:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n   else:")

            elif inpt in bot_ban:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)")

            elif inpt in bot_unban:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)")

            elif inpt in bot_unmute:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)")


            elif inpt in bot_kick:
              commandban2 = input("{*>_} ban to > ")
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, message.date + {commandban2})")


            elif inpt in bot_mute:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n        bot.restric_chat_member(message.chat.id, message.reply_to_message.from_user.id)")

            elif inpt in bot_mute_to:
              commandmute2 = input("{*>_} mute to > ")
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n            bot.restric_chat_member(message.chat.id, message.reply_to_message.from_user.id, message.date + {commandmute2})")


 
            elif inpt in bot_elif_message:
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n   elif message.text:")

            elif inpt in reg_hand:
              commandhand = input("{*>_} your command > ")
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n         bot.register_next_step_handler(text, {commandhand})")

            elif inpt in text_bot_send:
              commandtext = input("{*>_} your text > " )
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        text = bot.send_message(message.chat.id, "{commandtext}")')

            elif inpt in bot_poll_answer:
              commandpollanswer = input("*>_ . > " )
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_poll(message.chat.id, "{commandpollanswer}",')

            elif inpt in bot_bold:
              commandsendbold = input("*>_ your text > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_message(message.chat.id, "<b>{commandsendbold}</b>", parse_mode = "HTML")')


            elif inpt in bot_mono:
              commandsendmono = input("*>_ your text > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_message(message.chat.id, "<code>{commandsendmono}</code>", parse_mode = "HTML")')

#========================== send poll 


            elif inpt == "{*":
              with open('bot1.py', 'a') as f:
                 f.write(f'[')

            elif inpt == "add answ":     
              commandanswer = input("*>_ ")
              with open('bot1.py', 'a') as f:
                 f.write(f'"{commandanswer}",')                            

            elif inpt == "add answ end":
              commandanswer2 = input("*>_ ")
              with open('bot1.py', 'a') as f:
                 f.write(f'"{commandanswer2}"')

            elif inpt == "*}":
              with open('bot1.py', 'a') as f:
                 f.write(f'])')        

#======================================== 
# 

            elif inpt == ":$":
              with open('bot1.py', 'a') as f:
                 f.write(f'(')

            elif inpt == "add rows":     
              commandaddrows = input("*>_ ")
              with open('bot1.py', 'a') as f:
                 f.write(f'"{commandaddrows}",')                            

            elif inpt == "add rows end":
              commandanswer2 = input("*>_ ")
              with open('bot1.py', 'a') as f:
                 f.write(f'"{commandanswer2}"')

            elif inpt == "$:":
              with open('bot1.py', 'a') as f:
                 f.write(f')')     

#=========================================

            elif inpt in button:
              commandbutton = input('{*>_} your button name > ')
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n{commandbutton} = telebot.types.ReplyKeyboardMarkup(True)')

            elif inpt in "bot == row":
              commandnamebutton = input('{*>_} name > ')
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n{commandnamebutton}.row')


            elif inpt in reply_button:
              commandsendbutton = input('{*>_} your text > ')
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_message(message.chat.id, "{commandsendbutton}",')
              commandreplybutton = input('{*>_} your button name reply > ')
              with open('bot1.py', 'a') as f:
                 f.write(f' reply_markup = {commandreplybutton})')

            elif inpt in send_photo:
              commandphoto = input('{*>_} your photo name > ')
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_photo(message.chat.id, photo = open("files/{commandphoto}", "rb"))')

            elif inpt in send_audio:
              commandaudio = input('{*>_} your audio name > ')
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_audio(message.chat.id, audo = open("files/{commandaudio}", "rb"))')

            elif inpt in send_animation:
              commandaudio = input('{*>_} your animation name > ')
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_animation(message.chat.id, animation = open("files/{commandaudio}", "rb"))')

            elif inpt in bot_pin:
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.pin_message(message.chat.id, message.message_id)')

            elif inpt in bot_unpin:
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.unpin_message(message.chat.id, message.message_id)')

            elif inpt in bot_custom_admin:
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n         bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "admin")')

            elif inpt in bot_admin:
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n         bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id,can_delete_messages=True, can_pin_messages=True, can_restrict_members=True,  can_promote_members=True, can_change_info=True, can_invite_users = True)')

            elif inpt in bot_description:
              commanddesc = input("{*>_} your description > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.set_chat_description(message.chat.id, "{commanddesc}")')

            elif inpt in bot_title:
              commandtitle = input("{*>_} your title > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.set_chat_title(message.chat.id, "{commandtitle}")')

            elif inpt in bot_useful:
              print(colored("\n{ccs = help}"))
              print(colored("{change = color}"))

            elif inpt in bot_send_id:
              commandid2 = input("{*>_} input id > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n         bot.send_message({commandid2},')
              commandsend2 = input("{*>_} input text > ")
              with open('bot.py', 'a') as f:
                f.write(f'{commandsend2})')

            #comments
            elif inpt in bot_comment:
              commandcom = input("{*>_} input comment > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n #{commandcom}')

            elif inpt in bot_open1:
              commandopen2 = input("{*>_} your filename > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n         with open("{commandopen2}", "w") as f:')
              commandwrite2 = input("{*>_} input text > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n              f.write("{commandwrite2}")')

            elif inpt in bot_open2:
              commandopen3 = input("{*>_} your filename > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n         with open("{commandopen3}", "a") as f:')
              commandwrite3 = input("{*>_} input text > ")
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n              f.write("{commandwrite3}")')









            # elif inpt == "{bot == send.from.user.id}":
            #   commandid = input("{*>_} your text > ")
            #   with open('bot1.py', 'a') as f:
            #      f.write(f'\n\n         bot.send_message(message.chat.id, f"{commandid} {message.from_user.id}")')

            # elif inpt == "{bot == send.from.user.first.name}":
            #   commandfirstname = input("{*>_} your text > ")
            #   with open('bot1.py', 'a') as f:
            #      f.write(f'\n\n         bot.send_message(message.chat.id, f"{commandfirstname} {message.from_user.first_name}")')






              # print(colored('{*>_} successfully', 'green'))



            else:
              with open("colors.txt", "r+") as f:
                list = f.read()
              print(colored(f'*>_ CommandError: command <{inpt}> not defined', list))
           
