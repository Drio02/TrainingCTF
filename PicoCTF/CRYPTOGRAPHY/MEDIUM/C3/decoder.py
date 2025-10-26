lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"  
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst" 

with open("ciphertext", "r") as f:
	c = f.read()

flag = ""

prev = 0
for i in c:
	iFlag = (lookup2.index(i) + prev) % 40
	flag += lookup1[iFlag]
	prev = iFlag

print(flag)
