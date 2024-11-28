'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''


num = int(input("Ingresa un número entero: "))


bin = ""


if num == 0:
    bin = "0"


else:
    while num > 0:
        bin = str(num % 2) + bin
        num = num // 2 


print(f"El número en binario es: {bin}")