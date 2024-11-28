'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''
limite = int(input("Cuantos numeros quieres escribir: "))
cNmenor = 0
cNigual = 0
cNmayor = 0
for i in range(1,limite + 1):
    num = int(input(f"Escribe el numero {i}: "))
    
    if num > 0:
        cNmayor += 1
    elif num < 0:
        cNmenor += 1
    else:
        cNigual += 1
        
print(f"De los numeros introducidos {cNmayor} son mayores que 0")
print(f"De los numeros introducidos {cNmenor} son menores que 0")
print(f"De los numeros introducidos {cNigual} son iguales a 0")