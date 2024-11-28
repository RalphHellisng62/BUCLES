'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''
print("Escribe 10 numeros")
suma = 0
for i in range(1,11):
    num  = int(input("Escribe un numero: "))
    suma += num
    
print(f"La suma fue: {suma}")
prome = suma / 10

print(f"El promedio es: {prome}")