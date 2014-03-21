from sys import argv
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((argv[1], 1337))
s.send(bytes(argv[2], "UTF-8"))
reply = s.recv(1024)
while not reply:
	reply = s.recv(1024)
print "Server replied:", str(reply)[2:-1]
s.close()