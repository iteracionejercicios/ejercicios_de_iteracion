def cuadrados_perfectos(limite):
  # Creamos una lista vacía para almacenar los cuadrados perfectos
    lista = []
  # Inicializamos el contador en 0
    i = 0
  # Mientras el cuadrado del contador sea menor que el límite
    while i**2 < limite:
       # Agregamos el cuadrado del contador a la lista
        lista.append(i**2)
      # Incrementamos el contador
        i += 1  
      # Devolvemos la lista con los cuadrados perfectos
    return lista