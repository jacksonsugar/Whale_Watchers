import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

source = "/home/pi/Desktop/"

i = 0

while True:
	input = GPIO.input(12)
	if (input == False):
		i += 1
		print("Running Sample...")
		os.system("sudo /home/pi/Desktop/Midterm/USB_DAQ_1_Min")
		destination = "Data%s.txt" % i
		os.chdir(source)
                os.rename("Data.txt", destination)
		os.system("sudo sshpass -p 'ramboat'  scp /home/pi/Desktop/Data%s.txt jack@131.128.105.242:~/Desktop/1/" % i)
		print("Done! %s" % i)
	time.sleep(.2)
