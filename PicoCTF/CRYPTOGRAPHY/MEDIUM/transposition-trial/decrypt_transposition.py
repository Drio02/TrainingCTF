def decrypt(n):
	f = open("message.txt", "r", encoding="UTF-8")
	txt = f.read()

	txt3gram = [txt[i:i+n] for i in range(0, len(txt), n)]
	decode_lst = []

	for i in range(len(txt3gram)):
		decode_lst.append(txt3gram[i][2]+txt3gram[i][0]+txt3gram[i][1])

	print(''.join(decode_lst))

decrypt(3)
