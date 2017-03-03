import datetime
import forecastio
import argparse

def main(args):
	
	parser = argparse.ArgumentParser(description='Get a summary of your day')
	parser.add_argument('-x','--latitude', help='Input for the latitude of your location',required=True)
	parser.add_argument('-y','--longitude', help='Input for the longitude of your location',required=True)
	parser.add_argument('-k','--key', help='Input for key of Darksky API',required=True)
	args = parser.parse_args()
	
	key = args.key
	lat = args.latitude
	lng = args.longitude
	time = datetime.datetime.now()
	
	forecast = forecastio.load_forecast(key, lat, lng, time=time)
	
	daily = forecast.hourly()
	daily_sum = daily.summary
	
	print(daily_sum)
	
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
