from aiogram import Bot, Dispatcher, executor, types
import pyqrcode
bot=Bot(token='your bot token')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply('Salom menga url yoki text yuboring')
@dp.message_handler(commands=['help'])
async def start_message(message: types.Message):
    await message.reply('Menga url manzili yoki text yuboring men uni qr code qilib beraman')

@dp.message_handler()
async def qrcode(message):
    text=pyqrcode.create(message.text)
    text.png('code.png',scale=15)
    await bot.send_photo(chat_id=message.chat.id,photo=open('code.png', 'rb'), caption=f"{message.text}\n\n@scan_qr_bot orqali yasaldi")
executor.start_polling(dp) 
