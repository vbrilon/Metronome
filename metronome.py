#!/usr/local/bin/python
"""
Usage: %(scriptName)s min_bpm, max_bpm, number of clicks to loop on a given bpm, seconds to wait before starting next loop
Example: %(scriptName)s 100 120 4 5
This will generate a random bpm between 100 and 120 and repeat it for 4 clicks before moving to a new value after 5 seconds
"""

import sys  
import pygame
import random
import time

def start_tick(minbpm, maxbpm, beats, seconds):
	count = 0
	bpm = random.randint(minbpm, maxbpm)
	delay = 60000/bpm
	sys.stdout.write(str(bpm) + " bpm ")
	sys.stdout.flush()
	time.sleep(seconds)
	while count < beats:
		tick_sound.play()
		sys.stdout.write(". ")
		sys.stdout.flush()
		pygame.time.delay(delay)
		count += 1
	print
	start_tick(minbpm, maxbpm, beats, seconds)  
	
	
def main(argv):  
	if len(argv) != 5:  
		print __doc__ % {'scriptName' : sys.argv[0].split("/")[-1]} 
		return -1   
	minbpm = float(argv[1])  
	maxbpm = float(argv[2])  
	beats = float(argv[3])
	seconds = float(argv[4])
	start_tick(minbpm, maxbpm, beats, seconds)  
   
if __name__ == '__main__':  
	pygame.mixer.pre_init(44100, -16, 2, 512)  
	pygame.init()  
	tick_sound = pygame.mixer.Sound("click.wav")
	main(sys.argv)
