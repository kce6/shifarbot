# shifarbot_responses.py 
# author: KE
# Version: 0.0.1

# imports
import random
import os

# shifar quotes
shifar_quotes = [
	'How many times do I have to tell you, I can\'t run an ethernet cable to my computer.',
	'Look its not that simple, we\'ve been over this before.',
	'You\'ve been to my house, you understand why I can\'t just run a cable.',
	'I\'ve only disconnected 4 times this game, is it really that big of a deal?',
	'Just because I disconnected doesn\'t mean we lost the round, you\'re being dramatic.',
	'I don\'t hear you bitching about (insert team member that is definitely playing better than he is).',
	'I might have given myself a ban on draft kings but that won\'t stop me from playing blackjack on Caesar\'s.',
	'Grinding Brotha.',
	'Hoboken tonight?',
    'What do you mean the US lost the Vietname War?  We killed more of them!',
    'I\'m actually Persian, NOT a dirty arab.  Get it right.',
    'Actually that\'s not what I\'m seeing as the first result on Google.',
    'So..............Hoboken tonight?',
    'Why does Tony hate me so much? (10 seconds after saying Tony has an almond peen)',
    '(Shifar has been forcefully disconnected from the chat)',
    'Persia was the only country to never be colonized, if that doesn\'t scream \"I\'m better than you\", I don\'t know what does.',
    'Persia was a global superpower before the Muslims ruined it.'
]

# get current working directory
#__location__ = os.path.realpath(
#        os.path.join(os.getcwd(), os.path.dirname(__file__))
#)


# function for getting current disconnect count
def get_total_dc() -> int:
	f = open("/opt/bots/shifarbot/shifarbot_dccount.txt", "r")
	total_dc = f.read()
	f.close()
	return total_dc

# function for updating disconnect count and writing to file
def update_total_dc() -> int:
	f = open("/opt/bots/shifarbot/shifarbot_dccount.txt", "r")
	current_dc = f.read()
	new_dc = str(int(current_dc) + 1)
	#new_dc = str(new_dc)
	f = open("/opt/bots/shifarbot/shifarbot_dccount.txt", "w")
	f.write(new_dc)
	f.close()

# responses for shifarbot
def handle_response(message) -> str:
	p_message = message.lower()

	if p_message == '!shifar_disconnects':
		# call function to get current disconnect total and print
		total_dc = get_total_dc()
		return "Shifar has disconnected while playing games with his friends " + total_dc + " times since October 2023"

	if p_message == '!shifar_disconnected':
		# call function to update the disconnect total
		update_total_dc()
		response = random.choice(shifar_quotes)
		return response

	if p_message == '!shifar_quotes':
		shifar_quote = random.choice(shifar_quotes)
		return shifar_quote

	if p_message == '!help':
		help_message = """`!shifar_disconnects to see the total number of times shifar has disconnected from games.\n!shifar_disconnected to add 1 to the counter of times shifar has disconnected from games.\n!shifar_quotes to randomly send a shifar quote.`"""
		return help_message
