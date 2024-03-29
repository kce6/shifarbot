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
	'I don\'t hear you bitching about (insert team member that is definitely playing better than I am).',
	'I might have given myself a ban on draft kings but that won\'t stop me from playing blackjack on Caesar\'s.',
	'Grinding Brotha.',
	'Hoboken tonight?',
    'What do you mean the US lost the Vietnam War?  We killed more of them!',
    'I\'m actually Persian, NOT a dirty arab.  Get it right.',
    'Actually that\'s not what I\'m seeing as the first result on Google.',
    'So..............Hoboken tonight?',
    'Why does Tony hate me so much? (10 seconds after saying Tony has an almond peen)',
    '(Shifar has been forcefully disconnected from the chat)',
    'Persia was the only country to never be colonized, if that doesn\'t scream \"I\'m better than you\", I don\'t know what does.',
    'Persia was a global superpower before the Muslims ruined it.',
    'I swear I just picked my controller up and the game disconnected me.',
    'I\'m in a Valorant game, can you guys wait?',
    'I did not throw a slide tackle every single time I got beat.....It was every other time I got beat.',
    'My church burnt down, now my only religion is getting as many nuts in as possible before I die.',
    'Oh don\'t worry, he\'ll stop here and say goodbye on the way out.',
    'Wait 5 minutes, I\'m in a Valorant game.',
    'Why does Tony hate me so much? (After asking Tony to play L4D2)',
    'Why does Tony hate me so much? (After asking Tony how his day went)',
    'Why does Tony hate me so much? (After after telling Tony he\'s going to show up at his house in 5 minutes)',
    'Don\'t worry Tony, if you\'re out of a job, then I\'m out of a job',
    'Don\'t worry guys, I got the T-Mobile 5G Router.  No more bad wifi.',
    'Its straight data.',
    'I can\'t put the router in my room, it needs to connect through the windows!',
    'I\'m just going to get to level 32 and then I\'m gonna get off.',
    'I\'m just going to watch you attack the Jourmuntide....hey can I try and catch it after Tony?',
    'You\'ve got too much time on your hands brotha!',
    'Tony I\'m down here in the mines suffering so you can have fun on the game!',
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
