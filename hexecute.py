import os, sys
import random
import time

def game(rounds:int=4, level:int=1):
	start, pts = time.time(), 0

	print('[*] There are no winners, everyone is hexed in a different way.')
	for r in range(rounds):
		rand = random.randint(10*level, 64*level)

		shot = input(
			f'[*] Round {r}. Points : {pts}. Give me you equivalent in decimal, human.'+
			'\n'+hex(rand)[2:]+'\n')

		if shot.strip() == str(rand): pts +=16
		else: print('Correct answer was :', rand)
	end 	= 	time.time()
	elapsed = 	round(end-start)
	print('[*] The end. Your score was :', pts-elapsed)

game()
