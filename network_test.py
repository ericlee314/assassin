# from socket import *
# from threading import *

# class Server_Thread(Thread):
# 	def __init__(self, port):
# 		this.port = port
# 		Thread.__init__(self)

# 	def run(self):
# 		s = socket(AF_INET, SOCK_STREAM)

# 		host = ""
# 		port = this.port
# 		backlog = 5
# 		size = 1024
# 		s = socket(AF_INET, SOCK_STREAM)
# 		s.bind((host, port))
# 		s.listen(backlog)
# 		while True:
# 			client, address = s.accept()
# 			data = client.recv(size)
# 			if data:
# 				print data

# class Client_Thread(Thread):
# 	def __init__(self, other_address, port):
# 		this.other_address = other_address
# 		this.port = port
# 		Thread.__init__(self)

# 	def run(self):
# 		s = socket(AF_INET, SOCK_STREAM)

# 		host = this.other_address
# 		port = this.port
# 		backlog = 5
# 		size = 1024
# 		s = socket(AF_INET, SOCK_STREAM)
# 		s.connect((host, port))
# 		while True:
# 			s.send("Sending")
# 			# s.send(raw_input())

# server = Server_Thread(1337)
# client = Client_Thread("localhost", 1337)

# server.start()
# client.start()





import pickle
import socket
import threading

# We'll pickle a list of numbers:
someList = [ 1, 2, 7, 9, 0 ]
pickledList = pickle.dumps ( someList )

# Our thread class:
class ClientThread ( threading.Thread ):

   # Override Thread's __init__ method to accept the parameters needed:
   def __init__ ( self, channel, details ):

      self.channel = channel
      self.details = details
      threading.Thread.__init__ ( self )

   def run ( self ):

      print 'Received connection:', self.details [ 0 ]
      self.channel.send ( pickledList )
      for x in xrange ( 10 ):
         print self.channel.recv ( 1024 )
      self.channel.close()
      print 'Closed connection:', self.details [ 0 ]

# Set up the server:
server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
server.bind ( ( '', 2727 ) )
server.listen ( 5 )

# Have the server serve "forever":
while True:
   channel, details = server.accept()
   ClientThread ( channel, details ).start()