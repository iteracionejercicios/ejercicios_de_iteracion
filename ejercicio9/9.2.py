class Palabra:
    def __init__(self, palabra, anterior, siguiente): 
        self.palabra = palabra
        self.anterior = anterior
        self.siguiente = siguiente

def palabras_con_letra(letra, diccionario, anterior, siguiente): # definimos la funcion
    lista = []
    i = 0
    while i < len(diccionario) and diccionario[i].palabra[0] < letra: #definimos la funcion para cuando la letra es menor que la letra dada
          i += 1
    while i < len(diccionario) and diccionario[i].palabra[0] == letra: #definimos la funcion para cuando la letra es igual que la letra dada
        lista.append(diccionario[i])
        i += 1
   
    return lista #devolvemos la lista
        