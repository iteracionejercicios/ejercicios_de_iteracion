def palabras_con_letra(letra, diccionario, siguiente, anterior):
    lista = []    # Creamos una lista vacía para almacenar las palabras que cumplen con la condición
    i = 0  # Inicializamos un índice que usaremos para recorrer el diccionario
    while i < len(diccionario) and diccionario[i][0] < letra: # Recorremos el diccionario hasta encontrar una palabra cuya letra inicial sea mayor o igual que la letra dada
        i += 1 # Incrementamos el índice para seguir recorriendo el diccionario
    while i < len(diccionario) and diccionario[i][0] == letra: # Si encontramos una palabra cuya letra inicial sea igual a la letra dada, seguimos recorriendo el diccionario hasta que las palabras dejen de tener esa letra inicial
        lista.append(diccionario[i])   # Añadimos la palabra actual a la lista de palabras que cumplen con la condición
        i += 1  # Incrementamos el índice para seguir recorriendo el diccionario
    if siguiente:   
        while i < len(diccionario) and diccionario[i][0] == siguiente:   # Seguimos recorriendo el diccionario hasta que las palabras dejen de tener la letra siguiente
            lista.append(diccionario[i])  
            i += 1
    if anterior:  # Si se especificó una letra anterior
        i = i - 2   # Retrocedemos dos posiciones en el diccionario para encontrar la última palabra que empieza con la letra anterior (restamos 2 porque i fue incrementado dos veces en el segundo while)
        while i >= 0 and diccionario[i][0] == anterior:   # Seguimos retrocediendo en el diccionario hasta que las palabras dejen de tener la letra anterior
            lista.append(diccionario[i])
            i -= 1
    return lista  # Devolvemos la lista de palabras que cumplen con la condición
