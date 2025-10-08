# Calculamos la diferencia entre el inicio de la funcion main() y print_flag()
main = int('0x5949cd3fc401', 16)
print_flag = int('0x0000000000001269', 16)
diff_1 = main - print_flag
print(diff_1)

# Ahora calculamos la diferencia entre la direccion de retorno de echo_valley() y print_flag()
ev_return_addr = int('0x5949cd3fc413', 16)
diff_2 = ev_return_addr - print_flag
print(diff_2)

# Calculamos la direccion de print_flag() en base a la nueva direccion de main
new_main = int('0x617d57f2e401', 16)
new_print_flag = new_main - diff_1 # Si fuera en base a la nueva de direccion de retorno de echo_valley() seria diff_2
new_print_flag = hex(new_print_flag)
print(new_print_flag) # Va a dar que los ultimos numeros son 269
