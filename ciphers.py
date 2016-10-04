#Aid array
abc = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
msg = []

def getShiftedArray(shift):
	temp = list(abc)
	final = temp[shift:] + temp[:shift]
	return final


def encryptCaesar(shift, text):
	del msg[:]
	alph = getShiftedArray(shift%26)
	for i in range(0, len(text)):	
		if(text[i] != ' '):
			msg.append(alph[ord(str.upper(text[i])) - 65])
			continue;
		msg.append(" ")
	return ''.join(msg)



def decryptCaesar(shift, text):
	del msg[:]
	alph = getShiftedArray(26 - (shift%26))
	for i in range(0, len(text)):
		if(text[i] != ' '):
			msg.append(alph[ord(str.upper(text[i])) - 65])
			continue;
		msg.append(" ")
	return ''.join(msg)


def encryptVigenere(key, text):

	del msg[:]
	for i in range(0, len(text)):
		shift = (ord(text[i])- 65)
		row = getShiftedArray(shift)
		msg.append(row[ord(key[i % len(key)]) - 65])
	return ''.join(msg)

def decryptVigenere(key, enc_text):	

	del msg[:]
	for i in range(0, len(enc_text)):
		shift = (ord(key[i % len(key)]) - 65)
		row = getShiftedArray(26 - shift)
		msg.append(row[(ord(enc_text[i]) - 65)])
	return ''.join(msg)

print(encryptVigenere("FORTIFICATION", "DEFENDTHEEASTWALLOFTHECASTLE"))

