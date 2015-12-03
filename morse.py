
import RPi.GPIO as GPIO
from time import sleep

#Define alphabets.
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
morseAlpha = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', ' -.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '/']   

#Get sentence from user then convert it to lower case and get it's length.
word = input("Input a sentence: ").lower()
length = len(word)

#For every letter in the sentence, get it's position in the array and get the corresponding letter from the morse code array.
morse = ''
for i in range(0, length):
    morse = (morse + (morseAlpha[alpha.index(word[i])]))

#Print the sentence in morse code.
print(morse)

#Get the length of the morse code.
morseLength = len(morse)

#Set up GPIO.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

#For every character in the morse code determine whether it is "-", ".", or " " and act appropriately.
for m in range(0, morseLength):
	#If character is ".", print "." and power GPIO 18 for 0.25s.
	if(morse[m] == '.'):
		print('.')
		GPIO.output(18, True)
		sleep(0.25)
		GPIO.output(18, False)

	#If character is "-", print "-" and power GPIO 18 for 0.5s.
	elif(morse[m] == '-'):
	    print('-')
		GPIO.output(18, True)
		sleep(0.5)
		GPIO.output(18, False)	     

	#If character is " ", print " " and leave GPIO 18 off for 1s.
	elif(morse[m] == '/'):
		print('/')
		GPIO.output(18, False)
		sleep(1)
		GPIO.output(18, False)
