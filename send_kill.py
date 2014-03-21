from sys import argv
from socket import *

s = socket(AF_INET, SOCK_STREAM)

with open(self.file_name, "r") as f:
	for line in f:
		player_data = split(line)

		s.connect((player_data[1], 1337))
		s.send(bytes("kill {0} {1}".format(argv[1], argv[2]), "UTF-8"))
		reply = s.recv(1024)
		while not reply:
			reply = s.recv(1024)
		print "Server replied:", str(reply)[2:-1]

s.close()