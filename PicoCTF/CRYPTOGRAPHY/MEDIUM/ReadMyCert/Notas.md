Okey me da una arhivo de este tipo:

file readmycert.csr 
readmycert.csr: PEM certificate request

es un bloque de texto cifrado que se envía a una autoridad de certificación (CA) para solicitar un certificado SSL/TLS.
Contiene información de identidad de quien solicita el certificado, como el nombre del dominio, datos de la organización
y la clave pública.

Entonces tenemos que buscar una forma de leer este tipo de archivos, entonces la herramienta `openssl` nos ayuda con eso,
lo vamos a hacer con el siguiente comando:

`openssl req -in <nombre_del_.csr> -text -noout`

Para leer el certificado, en parte de la respuesta tenemos los siguiente:

Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN = picoCTF{read_mycert_693f7c03}, name = ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
Donde podemos ver el flag en la respuesta.
