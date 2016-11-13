import time
import os
import threading
import argparse
import sys

class Alarm(threading.Thread):

	def __init__(self, wakeupTime):
		# init class
		super(Alarm, self).__init__()
		self.wakeupTime = wakeupTime
		self.keep_running = True

	# runs alarm clock
	def run(self):
		
		# check time
		try:
			while self.keep_running:
				currentTime = time.strftime("%H:%M")
				if self.wakeupTime in currentTime:
					print('\nALARM IS GOING OFF')
					self.stop()

			# wait a bit
			time.sleep(1)

		except:
			# do nothing!
			return

	# stops alarm clock
	def stop(self):
		self.keep_running = False
		#sys.exit()


def main(args):

	# get input for alarm clock
	parser = argparse.ArgumentParser(description='This is a demo script by nixCraft.')
	parser.add_argument('-t','--time', help='Enter wakeup time (h:mm), no military time',required=True)
	parser.add_argument('-y','--type', help='AM or PM?',required=True)
	args = parser.parse_args()

	# check for valid time input
	wakeupTime = args.time

	try:
		time.strptime(wakeupTime, '%H:%M')

	except ValueError:
		print('Use correct time format (h:mm)')

	# format time
	if 'pm' in args.type or 'PM' in args.type:
		hour = wakeupTime[:wakeupTime.index(':')]
		militaryHour = str(int(hour) + 12)
		wakeupTime = militaryHour + wakeupTime[wakeupTime.index(':'):]
		print('Alarm set for: ' + wakeupTime)


	# turn on alarm clock
	alarm = Alarm(wakeupTime)
	alarm.start()

if __name__ == '__main__':
	sys.exit(main(sys.argv))
