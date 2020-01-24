#!/usr/bin/env python

# CCC

import bisect, random, socket, signal, base64, pickle, hashlib, sys, re, os

def load_encrypt_key():
	try:
		f = open('encrypt_key.bin', 'r')
		try:
			encrypt_key = f.read(4096)
			if len(encrypt_key) == 4096:
				return encrypt_key
		finally:
			f.close()
	except:
		pass
		
	rand = random.SystemRandom()
	encrypt_key = ""
	for i in xrange(0, 4096):
		encrypt_key += chr(rand.randint(0,255))

	try:
		f = open('encrypt_key.bin', 'w')
		try:
			f.write(encrypt_key)
		finally:
			f.close()
	except:
		pass
	
	return encrypt_key

class Field:
	def __init__(self, w, h, mines):
		self.w = w
		self.h = h
		self.mines = set()
		while len(self.mines) < mines:
			y = random.randint(0, h - 1)
			x = random.randint(0, w - 1)
			self.mines.add((y, x))
		self.mines = sorted(self.mines)
		self.opened = []
		self.flagged = []

	def calc_num(self, point):
		n = 0
		for y in xrange(point[0] - 1, point[0] + 2):
			for x in xrange(point[1] - 1, point[1] + 2):
				p = (y, x)
				if p != point and p in self.mines:
					n += 1
		return n

	def open(self, y, x):
		point = (int(y), int(x))
		if point[0] < 0 or point[0] >= self.h:
			return (True, "Illegal point")
		if point[1] < 0 or point[1] >= self.w:
			return (True, "Illegal point")
		if point in self.opened:
			return (True, "Already opened")
		if point in self.flagged:
			return (True, "Already flagged")
		bisect.insort(self.opened, point)
		if point in self.mines:
			return (False, "You lose")
		if len(self.opened) + len(self.mines) == self.w * self.h:
			return (False, "You win")
		if self.calc_num(point) == 0:
			#open everything around - it can not result in something bad
			self.open(y-1, x-1)
			self.open(y-1, x)
			self.open(y-1, x+1)
			self.open(y, x-1)
			self.open(y, x+1)
			self.open(y+1, x-1)
			self.open(y+1, x)
			self.open(y+1, x+1)
		return (True, None)
		

	def flag(self, y, x):
		point = (int(y), int(x))
		if point[0] < 0 or point[0] >= self.h:
			return "Illegal point"
		if point[1] < 0 or point[1] >= self.w:
			return "Illegal point"
		if point in self.opened:
			return "Already opened"
		if point in self.flagged:
			self.flagged.remove(point)
		else:
			bisect.insort(self.flagged, point)
		return None

	def load(self, data):
		self.__dict__ = pickle.loads(data)

	def save(self):
		return pickle.dumps(self.__dict__, 1)

	def write(self, stream):
		mine = 0
		open = 0
		flag = 0
		screen = "  " + ("0123456789" * ((self.w + 9) / 10))[0:self.w] + "\n +" + ("-" * self.w) + "+\n"
		for y in xrange(0, self.h):
			have_mines = mine < len(self.mines) and self.mines[mine][0] == y
			have_opened = open < len(self.opened) and self.opened[open][0] == y
			have_flagged = flag < len(self.flagged) and self.flagged[flag][0] == y
			screen += chr(0x30 | (y % 10)) + "|"
			for x in xrange(0, self.w):
				is_mine = have_mines and self.mines[mine][1] == x
				is_opened = have_opened and self.opened[open][1] == x
				is_flagged = have_flagged and self.flagged[flag][1] == x
				assert(not (is_opened and is_flagged))
				if is_mine:
					mine += 1
					have_mines = mine < len(self.mines) and self.mines[mine][0] == y
				if is_opened:
					open += 1
					have_opened = open < len(self.opened) and self.opened[open][0] == y
					if is_mine:
						c = "*"
					else:
						c = ord("0")
						#check prev row
						for m in xrange(mine - 1, -1, -1):
							if self.mines[m][0] < y - 1:
								break
							if self.mines[m][0] == y - 1 and self.mines[m][1] in (x - 1, x, x + 1):
								c += 1
						#check left & right
						if mine > 0 and self.mines[mine - 1][0] == y and self.mines[mine - 1][1] == x - 1:
							c += 1
						if have_mines and self.mines[mine][1] == x + 1:
							c += 1
						#check next row
						for m in xrange(mine, len(self.mines)):
							if self.mines[m][0] > y + 1:
								break
							if self.mines[m][0] == y + 1 and self.mines[m][1] in (x - 1, x, x + 1):
								c += 1
						c = chr(c)
				elif is_flagged:
					flag += 1
					have_flagged = flag < len(self.flagged) and self.flagged[flag][0] == y
					c = "!"
				else:
					c = " "
				screen += c
			screen += "|" + chr(0x30 | (y % 10)) + "\n"
		screen += " +" + ("-" * self.w) + "+\n  " + ("0123456789" * ((self.w + 9) / 10))[0:self.w] + "\n"
		stream.send(screen)

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 1024))
sock.listen(10)

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

encrypt_key = load_encrypt_key()

while 1:
	client, addr = sock.accept()
	if os.fork() == 0:
		break
	client.close()
sock.close()

f = Field(16, 16, 20)

re_pos = re.compile("^. *([0-9]+)[ :;,]+([0-9]+) *$")
re_save = re.compile("^. *([0-9a-zA-Z+/]+=*) *$")
def handle(line):
	if len(line) < 1:
		return (True, None)
	if len(line) == 1 and line[0] in "qxQX":
		return (False, "Bye")
	global f
	if line[0] in "foFO":
		m = re_pos.match(line)
		if m is None:
			return (True, "Usage: '([oOfF]) *([0-9]+)[ :;,]+([0-9]+) *', Cmd=\\1(Open/Flag) X=\\2 Y=\\3")
		x,y = m.groups()
		x = int(x)
		y = int(y)
		if line[0] in "oO":
			return f.open(y,x)
		else:
			return (True, f.flag(y,x))
	elif line[0] in "lL":
		m = re_save.match(line)
		if m is None:
			return (True, "Usage: '([lL]) *([0-9a-zA-Z+/]+=*) *', Cmd=\\1(Load) Save=\\2")
		msg = base64.standard_b64decode(m.group(1))
		tmp = ""
		for i in xrange(0, len(msg)):
			tmp += chr(ord(msg[i]) ^ ord(encrypt_key[i % len(encrypt_key)]))
		msg = tmp
		if msg[0:9] != "4n71cH3aT":
			return (True, "Unable to load savegame (magic)")
		h = hashlib.sha1()
		h.update(msg[9+h.digest_size:])
		if msg[9:9+h.digest_size] != h.digest():
			return (True, "Unable to load savegame (checksum)")
		try:
			f.load(msg[9+h.digest_size:])
		except:
			return (True, "Unable to load savegame (exception)")
		return (True, "Savegame loaded")
	elif len(line) == 1 and line[0] in "sS":
		msg = f.save()
		h = hashlib.sha1()
		h.update(msg)
		msg = "4n71cH3aT" + h.digest() + msg
		tmp = ""
		for i in xrange(0, len(msg)):
			tmp += chr(ord(msg[i]) ^ ord(encrypt_key[i % len(encrypt_key)]))
		msg = tmp
		return (True, "Your savegame: " + base64.standard_b64encode(msg))
	#elif len(line) == 1 and line[0] in "dD":
	#	return (True, repr(f.__dict__)+"\n")
	else:
		return (True, "Unknown Command: '" + line[0] + "', valid commands: o f q x l s")

data = ""
while 1:
	f.write(client)
	while 1:
		pos = data.find("\n")
		if pos != -1:
			cont, msg = handle(data[0:pos])
			if not cont:
				if msg is not None:
					client.send(msg + "\n")
				f.write(client)
				client.close()
				sys.exit(0)
			if msg is not None:
				client.send(msg + "\n")
			data = data[pos+1:]
			break
		new_data = client.recv(4096)
		if len(new_data) == 0:
			sys.exit(0)
		data += new_data
