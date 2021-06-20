import telebot
import requests
import json

url = 'https://api.openweathermap.org/data/2.5/weather'
api_weather = '2bf27388ecf4f3c8900e6ed4d1b2b18a'

bot = telebot.TeleBot('1689677574:AAEByo9Ho2QmVdWJkEl7YjkCFU-BcjQzuRI')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
	try:		
		params = {'APPID': api_weather,'q': message.text, 'units': 'metric'}
		result = requests.get(url, params=params)
		weather = result.json()
		bot.send_message(message.from_user.id, "\nShahar nomi: " + str(weather['name']) + "\nTemperatura: " + str(weather['main']['temp']) + " C\n"
		+ "Maksimal temperatura: " + str(weather['main']['temp_max']) + " C\n"
		+ "Minimal temperatura: " + str(weather['main']['temp_min']) + " C\n"
		+ "Shamol tezligi: " + str(weather['wind']['speed']) + " m/s\n"
		+ "Bosim: " + str(weather['main']['pressure']) + " Pa\n"
		+ "Namlik: " + str(weather['main']['humidity'])+ " %\n"
		+ "Ko'rinish : " + str(weather['visibility']) + "\n"
		+ "Tavsiflar: " + str(weather['weather'][0]['description']) + "\n")

	except:
		bot.send_message(message.from_user.id, "Bunday shahar mavjud emas")

@bot.message_handler(content_types=['sticker'])

def handle_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

bot.polling(none_stop=True,interval=0)
