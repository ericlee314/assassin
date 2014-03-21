from socket import *

class Player:
	self.name = None
	self.ip = None
	self.id = None
	self.score = None
	self.kills = None
	self.deaths = None

	def __init__(self, name, ip, ident, kills, deaths):
		self.name = name
		self.ip = ip
		self.id = ident
		self.score = kills - deaths
		self.kills = kills
		self.deaths = deaths

	def kill(self):
		self.kills += 1
		self.score += 1

	def die(self):
		self.deaths += 1
		self.score -= 1

class Assassin_Daemon:
	self.file_name = ""
	self.data = []

	def __init__(self, data_file_name):
		self.file_name = data_file_name

	def kill(self, killer, victim):
		for p in self.data:
			if p.id == killer:
				p.kill()
			elif p.id == victim:
				p.die()

	def load_data_file(self):
		with open(self.file_name, "r") as f:
			for line in f:
				player_data = split(line)

				self.data += [Player(player_data[0], player_data[1], player_data[2], player_data[4], player_data[5])]

	def save_data_file(self):
		with open(self.file_name, "w") as f:
			self.data.sort(cmp = lambda x, y: x.score - y.score)

			f.writelines(["{0} {1} {2} {3} {4} {5}".format(p.name, p.ip, p.id, p.score, p.kills, p.deaths) for p in self.data])

	def run(self):
		self.load_data_file(self.file_name)

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
				msg = str(data)[2:-1]

				client.send(msg)
				print "Recieved:", str(msg)

				cmd = split(msg)
				if cmd[0] == "kill":
					self.kill(*cmd[1:])

				self.save_data_file()
			client.close()