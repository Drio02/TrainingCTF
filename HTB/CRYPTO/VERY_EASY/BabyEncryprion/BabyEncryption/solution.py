import os

f = open('msg.enc', 'r')

plain = ""

secret = f.read()
print(secret)
cipher = bytes.fromhex(secret)

print(cipher)

for i in cipher:
	for brute in range(33, 126): #CAracteres imprimiblres en ASCII
		if((123 * brute + 18) % 256) == i:
			plain += chr(brute)
			break
print(plain)
