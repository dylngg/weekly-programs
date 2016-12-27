import select
import socket
import sys
import threading

class Server:
	# init
	def __init__(self):
		self.host = '192.168.1.108'
		self.port = 80
		self.backlog = 5
		self.size = 1024
		self.server = None
		self.threads = []
	
	
	# open socket
	def open_socket(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind((self.host,self.port))
		self.server.listen(5)
		print('[*] Listening on', self.host, ':', self.port)


	def run(self):
		self.open_socket()
		
		input = [self.server,sys.stdin]
		running = True
		while running is True:
			inputready,outputready,exceptready = select.select(input,[],[])
			
			for s in inputready:

				if s == self.server:
					client, addr = self.server.accept()
					
					# start client thread
					client_handler =  Client((client, addr))
					print('[*] Accepted connection from', addr)
					
					client_handler.start()
					self.threads.append(client_handler)
			
				elif s == sys.stdin:
					# handle standard input
					junk = sys.stdin.readline()
					running = False 
		
		
		# close all threads
		self.server.close()
		for c in self.threads:
			c.join()


class Client(threading.Thread):
	# init
	def __init__(self,(client,address)):
		threading.Thread.__init__(self)
		self.client = client
		self.address = address
		self.size = 1024


	def run(self):
		running = 1
		while running:
			request = self.client.recv(self.size)
			print('[*] Recieved', request)
			
			if request:
				response = str(raw_input('Response: '))
				self.client.send(response)
			
			else:
				self.client.close()
				running = 0

def main(args):
	s = Server()
	s.run()

if __name__ == "__main__":
	sys.exit(main(sys.argv))
