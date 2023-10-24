# shifarbot.py 
# author: KE
# Version: 0.0.1

# imports
import os
import random
import discord
import shifarbot_responses
from dotenv import load_dotenv # used to load the token

# function for sending a reply message based off detected inputs
async def send_message(message, user_message, is_private):
	# read in user message and determine if it is a private message or channel message.  send response (if applicable) in the appropriate channel
	try:
		response = shifarbot_responses.handle_response(user_message)
		# if message in DM, reply in DM.  Else reply in channel
		await message.author.send(response) if is_private else await message.channel.send(response)
	except Exception as e:
		print(e)

def run_discord_bot():
	load_dotenv()
	# get token
	TOKEN = os.getenv('DISCORD_TOKEN')
	# intents=discord.Intents.all() used for admin privs, intents=discord.Intents.default() for normal privs
	client = discord.Client(intents=discord.Intents.all())

    # client event to let us know the bot is running
	@client.event
	async def on_ready():
		print(f'{client.user} is now running!')

	# client event: 
	#	- avoid replying to our own messages
	#	- store username, message content, and channel name
	#	- '?' preceeding command to force DM, otherwise send message in channel
	@client.event
	async def on_message(message):
		if message.author == client.user:
			return

		username = str(message.author)
		user_message = str(message.content)
		channel = str(message.channel)

		# print(f"{username} said: '{user_message}' ({channel})")

		if user_message[0] == '?':
			user_message = user_message[1:]
			await send_message(message, user_message, is_private=True)
		else:
			await send_message(message, user_message, is_private=False)

	client.run(TOKEN)
