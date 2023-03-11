import os
import requests
import json
import discord
token_discord = 'INSIRA UM TOKEN DE ALGUMA CONTA BOT DO DISCORD'
token_open_ai = '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'

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_message(message):
	if message.author.id == bot.user.id:
		pass
	else:
		try:
			headers = {
			    'Content-Type': 'application/json',
			    'Authorization': f'Bearer {token_open_ai}',
			}

			json_data = {
			    'model': 'text-davinci-003',
			    'prompt': message.content,
			    'temperature': 0.5,
			    'max_tokens': 60,
			    'top_p': 0.3,
			    'frequency_penalty': 0.5,
			    'presence_penalty': 0.0,
			}


			response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
			await message.reply((json.loads(response.text)['choices'][0]['text']))
		except Exception as e:
			print(str(e))

bot.run(token_discord)