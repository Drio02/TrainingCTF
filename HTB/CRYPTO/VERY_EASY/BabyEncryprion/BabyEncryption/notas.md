Este reto lo que hace es agarrar cada caracter de la flag y le hace una operacion matematica, para despues aplicar modulo 256, para que sea un byte
cada byte va  ser imprimible, entonces vamos a hacer un tipo de brute force, con el siguiente codigo:

```
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

```

Con eso obtenemos el flag
