import telebot
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Bot's token here (get it from Telegram's @BotFather bot)
TOKEN = 'TOKEN HERE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start_message(message):
  bot.reply_to(message, "SOME TEXT HERE 0. FOR START: /newstory")

@bot.message_handler(commands = ['newstory'])
def email_message(message):
  bot.reply_to(message, "SOME TEXT HERE 1")

@bot.message_handler(content_types = ['text'])
def send_email(message):
  try:
  username = "{0.username}".format(message.from_user, bot.get_me())
fromaddr = "example@gmail.com" #Sender Gmail
mypass = "example@gmail.com's password" #Sender Gmail's password 
toaddr = "example@mail.com" #Recipient
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Отправитель: " + str(message.chat.id)
body = "Сообщение от: https://t.me/" + username + "\n\n" + message.text
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
bot.reply_to(message, "SOME TEXT HERE 2 (SUCCESS)")
except Exception:
  bot.reply_to(message, "SOME TEXT HERE 3 (ERROR)")

bot.polling()
