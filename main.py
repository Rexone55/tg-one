import os
import telebot


bot = telebot.TeleBot("5006654263:AAFW5XLeGj_qXjLb8u7dUSAmP1FgLDyHWdw")
PM_START_TEXT = f"""
*Hellow There,මම තමා රෙක්සොගෙ බොටා ප#ද බලන්නෙ
ක්ක්ක් නමස්කාරම් කියලා පටන් ගන්නම් දුවන්න නම් ලාස්ති වෙන්න එපා...../start ඕක ඔබපන්
"""

buttons = [
    [
        InlineKeyboardButton(text="බොසාගෙ ඇක", url="https://t.me/Rexi_55"),
        InlineKeyboardButton(text="බොසාගෙ චැම්නල් එක", url="https://t.me/ReXoNe404"),
    ],
    [
        InlineKeyboardButton(text="මේ බටන් එකේ මුකුත් නෑ", url="#"),
        InlineKeyboardButton(text="මේක කැඩිලා", callback_data="#"),
 ),
    ],
]




@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "අමෝ අමෝ ලොකු බොසා මෙන්න කමාන්ඩ්  /සාත්තර බලන්න ,/ෂැපක් ,/ඉගෙන ගන්න, /ඉවර කරන්න")


@bot.message_handler(commands=["සාත්තර බලන්න"])
def send_message(message):
  bot.send_message(message.chat.id, "උබ දැන් පෝන් එකේ ඉන්නෙ ඕක තියලා වැඩක් කරපන්කො කාලකන්නියා....")

@bot.message_handler(commands=["/ෂැපක්"])
def send_message(message):
  bot.send_message(message.chat.id, "තාම අයිඩීවත් නෑ නේද පොඩි එකෝ")

@bot.message_handler(commands=["/ඉගෙන ගන්න"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/ReXoNe404 ඕකට ජොයින් වෙයම් කිරි පුතේ")

  @bot.message_handler(commands=["/ඉවර කරන්න"])
  def send_message(message):
      bot.send_message(message.chat.id, "ආසාවෙන් හදපු පලවෙනි බොට් ඉස්සරහට් හොද එකක් දාන්නම් ම්න් යනෝ බායි බොක්ක")

bot.polling()
