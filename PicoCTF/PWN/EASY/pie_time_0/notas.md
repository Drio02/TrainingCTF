El reto consiste en un codigo en que al darle una direccion de memoria salta a ella, tenemos una funcion win() que nos
imprime el flag. Al realizarle un *checksec* con pwntools, tenemos la siguiente salida.

    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No

Notamos que tenemos la defensa de PIE activa. Busquemos acerca de PIE:


Cada vez que el binario se ejecuta, al tener la defensa PIE activa, el sistema operativo carga el programa 
en una direccion de memoria aleatoria, eso dificulta el ataque de explotaciones binarias a los atacantes.

En el caso de este reto, vamos a tener direcciones de memoria distintas para el binario local como para el que 
tenemos en el server. Para bypassear esta defensa lo que vamos a hacer es calcular el offset entre donde empieza
la funcion main (en el output del reto, nos dice la direccion de main) y la direccion de donde inicia la 
funcion win(). Al realizar la resta nos da que el offset es de 96.

Entonces ahora tomamos la direccion del main en el server y le restamos 96, el resultado va a ser la 
direccion de memoria en donde esta la funcion win().

Flag -> picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_6f4e7236}

