from socket import *

class Player:
	name = None
	ip = None
	ident = None
	score = None
	kills = None
	deaths = None

	def __init__(self, name, ip, ident, kills, deaths):
		self.name = name
		self.ip = ip
		self.ident = ident
		self.score = kills - deaths
		self.kills = kills
		self.deaths = deaths

	def __str__(self):
		return "{0} {1} {2}".format(self.name, self.kills, self.deaths)

	def kill(self):
		self.kills += 1
		self.score += 1

	def die(self):
		self.deaths += 1
		self.score -= 1

class Assassin_Daemon:
	file_name = ""
	data = []

	def __init__(self, data_file_name):
		self.file_name = data_file_name

	def kill(self, killer, victim):
		for p in self.data:
			if p.ident == int(killer):
				p.kill()
			if p.ident == int(victim):
				p.die()

	def load_data_file(self):
		with open(self.file_name, "r") as f:
			for line in f:
				player_data = line.split()

				self.data += [Player(player_data[0], player_data[1], int(player_data[2]), int(player_data[4]), int(player_data[5]))]

	def save_data_file(self):
		with open(self.file_name, "w") as f:
			self.data.sort(cmp = lambda x, y: x.score - y.score)

			f.writelines(["{0} {1} {2} {3} {4} {5}\n".format(p.name, p.ip, p.ident, p.score, p.kills, p.deaths) for p in self.data])

	def run(self):
		self.load_data_file()

		s = socket(AF_INET, SOCK_STREAM)

		host = ""
		port = 1337
		backlog = 5
		size = 1024
		s = socket(AF_INET, SOCK_STREAM)
		s.bind((host, port))
		s.listen(backlog)
		while True:
			for p in self.data:
				print p

			client, address = s.accept()
			data = client.recv(size)
			if data:
				msg = str(data)

				client.send(msg)
				print "Recieved:", str(msg)

				cmd = msg.split()
				if cmd[0] == "kill":
					self.kill(*cmd[1:])

				self.save_data_file()
			client.close()

Assassin_Daemon("data").run()