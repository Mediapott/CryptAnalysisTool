import re
import sys


class Counter:
	def __init__(self):
		pass

	def get_mode(self):
		while True:
			print("\n+--------------------------------------------------------------+")
			print("[1] Datei analysieren\t\t", "[2] Caesar verschluesseln")
			print("[3] Caesar entschluesseln\t", "[4] Caeser bruteforcen")
			print("[5] Substitution verschluesseln\t", "[6] Substitution entschluesseln")
			print("[0] Programm beenden")
			print("+--------------------------------------------------------------+")
			print("Was willst du tun? ")
			mode = input().lower()
			if mode in '1 2 3 4 5 6 0'.split():
				return mode
			else:
				print("Eingabe nicht erkannt. Bitte einen der Werte 1, 2, 3, 4, 5, 6, 0 eingeben")

	def get_message(self):
		print("Bitte Text eingeben: ")
		return input().lower()

	def get_key(self):
		while True:
			print("Bitte einen Wert zwischen 1 und 25 eingeben")
			key = int(input())
			if 2 <= key <= 25:
				return key

	def get_subkey(self):
		key = ''
		print("Bitte das Ersatzalphabet eingeben")
		while True:
			key = str(input())
			# if (len(key) == 26):
			return key
		# else:
		# print ("Bitte genau 26 Zeichen angeben")

	def get_translated_message(self, mode, message, key):
		if mode[0] == '3' or mode[0] == '4':
			key = -key
		translated = ''

		for symbol in message:
			if symbol.isalpha():
				num = ord(symbol)
				num += key

				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

				translated += chr(num)
			else:
				translated += symbol
		return translated

	def main_fn(self):
		global filename, inpDatei
		diction = {}
		mode = self.get_mode(self)

		if mode[0] == '2' or mode[0] == '3':
			message = self.get_message(self)
			key = self.get_key(self)
			print("Die uebersetzte Nachricht lautet:")
			print(self.get_translated_message(self, mode, message, key))
		elif mode[0] == '4':
			message = self.get_message(self)
			for key in range(1, 26):
				print(key, "\t", self.get_translated_message(self, mode, message, key))
		elif mode[0] == '0':
			sys.exit()
		elif mode[0] == '5':
			message = self.get_message(self)
			subKey = self.get_subkey(self)
			print(self.substitution(self, mode, message, subKey))
		elif mode[0] == '1':
			error = False
			try:
				filename = sys.argv[1]
				inpDatei = open(filename).read()
				inpDatei = inpDatei.lower()
			except (IOError, ValueError, IndexError):
				error = True
			if error:
				print(
					"Keine Datei uebergeben oder erkannt! Bitte beim Start des Programms gueltigen Dateinamen angeben!")
			else:
				print(filename, "\n")
				print(str(inpDatei))
				inpdatei_split = inpDatei.split()
				words = len(inpdatei_split)
				print("\nDer Text besteht aus", str(words), "Wörtern")

				x = "".join(inpdatei_split)
				chars = len(x)
				print("Der Text besteht aus", str(chars), "Zeichen")

				p = len(inpDatei)
				print("Der Text besteht aus", str(p), "Zeichen inkl. Leerzeichen")

				j = 0
				for y in inpDatei:
					if re.search(r"[a-z]", y):
						j += 1

				print("Der Text besteht aus", str(j), "Buchstaben\n\n")

				for c in inpDatei:
					if not c in diction.keys():
						diction[c] = 0
					diction[c] += 1

				print("Buchstabe\t", "absolute Anzahl\t", "relative Anzahl in Prozent\n")

				k = ord("a")
				while k <= ord("z"):
					l = chr(k)
					print(l, "\t\t", diction[l], "\t\t\t", "%.2f" % float((diction[l] / chars) * 100))
					k += 1

	def substitution(self, mode, message, subkey):
		message = message.lower()
		trans_sub = ''
		dict_sub = {}
		for h in range(0, len(message)):
			if message[h] == 'a':
				trans_sub = trans_sub + 'S'
			else:
				trans_sub = trans_sub + message[h]

		for r in dict_sub.keys():
			print(r)

		return trans_sub

	diction = {}


while True:
	Counter.main_fn(Counter)
