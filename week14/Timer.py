import time
import threading
import argparse
import sys

class Timer(threading.Thread):

	def __init__(self):
		super(Timer, self).__init__()
		self.totalSeconds = 0
		self.keep_running = True
	
	# sets total seconds to wait
	def setTotalSeconds(self, hour = 0, minutes = 0, seconds = 0):
		self.totalSeconds = self.totalSeconds + (int(hour) * 3600) + (int(minutes) * 60) + int(seconds)
	
	# runs timer 
	def run(self):
		time.sleep(self.totalSeconds)
		print('TIMER IS GOING OFF!') 

	# stops timer clock
	def stop(self):
		self.keep_running = False

def main(args):
	# get input for timer
	parser = argparse.ArgumentParser(description='A simple Timer')
	parser.add_argument('-hr','--hour', help='Input for hours',required=False)
	parser.add_argument('-m','--minute', help='Input for minutes',required=False)
	parser.add_argument('-s','--second', help='Input for seconds',required=False)
	args = parser.parse_args()
	
	hour = 0
	minute = 0
	second = 0
	
	# check for valid time input
	if args.hour is not None:
		if int(hour) < 0:
			raise ValueError('The hour agrument is less than 0.')
		
		hour = args.hour
	
	if args.minute is not None:
		if int(minute) < 0:
			raise ValueError('The minute agrument is less than 0.')
		
		minute = args.minute
	
	if args.second is not None:
		second = args.second
	
	# check that at least one argument is provided
	if args.hour is None and args.second is None and args.minute is None:
		raise ValueError('No input provided.')
	
	# print confirmation that timer has started
	print('Timer set.')
	
	# create Timer
	timer = Timer()
	Timer.setTotalSeconds(timer, hour, minute, second)
	Timer.start(timer)

if __name__ == '__main__':
	sys.exit(main(sys.argv))
