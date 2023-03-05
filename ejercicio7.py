#Escribir un algoritmo iterativo que transforme un número entero n cualquiera en su representación en una base B ≥ 2 cualquiera.
print("Elija un numero y la base donde quiere su representacion siendo esta mayor que 2")
n = int(input("Numero: ")) #permitimos introducir el numero a cambiar
B = int(input("Base: ")) #permitimos introducir la base 
if B < 2: #definimos la funcion para cuando B es menor que 2 
    print("La base debe ser mayor que 2") #Decimos que la base debe ser mayor que 2 ya que asi lo pide el enunciado
elif 2 <= B <= 36: #definimos la funcion para cuando el valor dado a la base esta entre 2 y 36
    print("La representacion de", n, "en base", B, "es:", end=" ")
    while n > 0:
        else:
            print(chr(n % B + 55), end="")
    print()
elif B > 36: #definimos la funcion para cuando B es mayor que 36
    print("La representacion de", n, "en base", B, "es:", end=" ")
    while n > 0:
        print(n % B, end="") #Se pasa el numero a en base 10
        n = n // B
    print()
