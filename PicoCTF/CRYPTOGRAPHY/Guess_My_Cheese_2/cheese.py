import hashlib

file=open("cheese_list.txt","r").readlines()
for j in file:
    for k in "0123456789abcdef":
        for l in "0123456789abcdef":
            print(j[:-1]+k+l,hashlib.sha256((j[:-1]+k+l).encode('utf-8')).hexdigest())
            print(k+l+j[:-1],hashlib.sha256((k+l+j[:-1]).encode('utf-8')).hexdigest())
for j in file:
    for k in range(256):
        print(j[:-1]+hex(k),hashlib.sha256((j[:-1]+chr(k)).encode('utf-8')).hexdigest())
        print(hex(k)+j[:-1],hashlib.sha256((chr(k)+j[:-1]).encode('utf-8')).hexdigest())
        print(j[:-1]+hex(k),hashlib.sha256((j[:-1]+chr(k)).lower().encode('utf-8')).hexdigest())
        print(hex(k)+j[:-1],hashlib.sha256((chr(k)+j[:-1]).lower().encode('utf-8')).hexdigest())