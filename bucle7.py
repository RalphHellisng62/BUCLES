'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
print("Identificador de vocales (para salir ingresa espacio)")

while True:
    letra = input("Escribe una letra: ")
    letra = letra.upper()
    
    if letra == " ":
        break
    else:
        if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' :
            print("SI ES VOCAL")
        else:
            print("NO ES UNA VOCAL") 
    