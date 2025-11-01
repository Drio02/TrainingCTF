Tenemos que usar la herramienta `steghide` para 2 cosas.

La primera es que vamos a analizar el archivo .jpg, utilizamos el siguiente comando `steghide info <archivo>` y 
notamos que hay un archivo .txt embebido, entonces con el siguiente comando los extraemos:

`steghide extract -sf <nombre_del_archivo_imagen>`

Y tenemos el archivo, ahora lo que hacemos es ver el contenido del archivo:

krxlXGU{zgyzhs_xizxp_7142uwv9}

AL investigar que significa **atbash** descubrimos que es un algoritmo de encriptacion, entonces buscamos un decoder
en linea y obtenemos la flag:

picoCTF{atbash_crack_7142fde9}
