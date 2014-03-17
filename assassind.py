from socket import *

s = socket(AF_INET, SOCK_STREAM)

host = ""
port = 1337
backlog = 5
size = 1024
s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)
while True:
	client, address = s.accept()
	data = client.recv(size)
	if data:
		client.send(data)
		print "Recieved:", str(data)
		with open("nwt_output", "w") as f:
			f.write(data)
			f.close()
	client.close()