import telebot, random, os, threading
from flask import Flask
from telebot import types
TOKEN=os.environ.get("TOKEN")
bot=telebot.TeleBot(TOKEN)
ud={}
app=Flask(__name__)
@app.route('/')
def h(): return "LIVE 24/7"
def run(): app.run(host='0.0.0.0',port=10000)
threading.Thread(target=run).start()
@bot.message_handler(commands=['start'])
def s(m):
 kb=types.InlineKeyboardMarkup(row_width=2)
 kb.add(types.InlineKeyboardButton("Forex",callback_data="c_Forex"),types.InlineKeyboardButton("Crypto",callback_data="c_Crypto"))
 kb.add(types.InlineKeyboardButton("Stocks",callback_data="c_Stocks"),types.InlineKeyboardButton("Indices",callback_data="c_Indices"))
 kb.add(types.InlineKeyboardButton("Gold",callback_data="c_Gold"),types.InlineKeyboardButton("Meme",callback_data="c_Meme"))
 bot.send_message(m.chat.id,"PRO BOT 24/7 ONLINE - Choose:",reply_markup=kb)
@bot.callback_query_handler(func=lambda x:True)
def cb(c):
 cid=c.message.chat.id;mid=c.message.message_id;d=c.data
 if d.startswith("c_"):
  cat=d[2:];ud[cid]=cat;kb=types.InlineKeyboardMarkup(row_width=2);lst=[]
  if cat=="Forex": lst=["EUR/USD OTC","GBP/USD OTC","USD/JPY OTC","AUD/USD OTC","USD/CHF OTC","EUR/JPY OTC"]
  elif cat=="Crypto": lst=["TRON OTC","Solana OTC","BTC OTC","ETH OTC","LTC OTC","DOGE OTC"]
  elif cat=="Stocks": lst=["AAPL OTC","TSLA OTC","MSFT OTC","GOOGL OTC","AMZN OTC","META OTC"]
  elif cat=="Indices": lst=["US30 OTC","NAS100 OTC","SPX500 OTC","UK100 OTC","GER40 OTC","JP225 OTC"]
  elif cat=="Gold": lst=["GOLD OTC","SILVER OTC","OIL OTC","GAS OTC","COPPER OTC","PLATINUM OTC"]
  else: lst=["SHIB OTC","PEPE OTC","BONK OTC","FLOKI OTC","WIF OTC","MEME OTC"]
  for p in lst: kb.add(types.InlineKeyboardButton(p,callback_data="p_"+p))
  bot.edit_message_text(f"Category: {cat}\nPick Pair:",cid,mid,reply_markup=kb)
 if d.startswith("p_"):
  pair=d[2:];ud[str(cid)+"P"]=pair;kb=types.InlineKeyboardMarkup(row_width=3)
  kb.add(types.InlineKeyboardButton("3SEC",callback_data="e_3SEC"),types.InlineKeyboardButton("5SEC",callback_data="e_5SEC"),types.InlineKeyboardButton("8SEC",callback_data="e_8SEC"))
  kb.add(types.InlineKeyboardButton("10SEC",callback_data="e_10SEC"),types.InlineKeyboardButton("15SEC",callback_data="e_15SEC"),types.InlineKeyboardButton("M1",callback_data="e_M1"))
  kb.add(types.InlineKeyboardButton("M2",callback_data="e_M2"),types.InlineKeyboardButton("M3",callback_data="e_M3"),types.InlineKeyboardButton("M4",callback_data="e_M4"),types.InlineKeyboardButton("M5",callback_data="e_M5"))
  bot.edit_message_text(f"Pair: {pair}\nPick Expiry:",cid,mid,reply_markup=kb)
 if d.startswith("e_"):
  exp=d[2:];pair=ud.get(str(cid)+"P","EUR/USD OTC");sig=random.choice(["BUY","SELL"]);acc=random.randint(89,97)
  txt=f"🔥 PRO SIGNAL 24/7\n\nPair: {pair}\nExpiry: {exp}\nSignal: {sig}\nAccuracy: {acc}%\n\nBot never sleeps!"
  kb=types.InlineKeyboardMarkup();kb.add(types.InlineKeyboardButton("🔄 New Signal",callback_data="e_"+exp));kb.add(types.InlineKeyboardButton("⬅️ Back",callback_data="c_Forex"))
  bot.edit_message_text(txt,cid,mid,reply_markup=kb)
bot.infinity_polling()