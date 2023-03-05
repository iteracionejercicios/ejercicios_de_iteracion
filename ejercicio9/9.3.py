def añadir_palabra(nueva_palabra, diccionario, siguiente, anterior):
    diccionario.append(nueva_palabra)
    indice_nueva_palabra = len(diccionario) - 1
    indice_actual = 0
    while diccionario[indice_actual].palabra < nueva_palabra.palabra:
        indice_actual += 1
    if diccionario[indice_actual].palabra == nueva_palabra.palabra:
        diccionario[indice_actual] = nueva_palabra
    else:
        diccionario.insert(indice_actual, nueva_palabra)
    if siguiente:
        indice_actual += 1
        while diccionario[indice_actual].palabra[0] == siguiente:
            diccionario[indice_actual].anterior = nueva_palabra.palabra
            indice_actual += 1
    if anterior:
        indice_nueva_palabra -= 2
        while diccionario[indice_actual].palabra[0] == anterior:
            diccionario[indice_actual].siguiente = nueva_palabra.palabra
            indice_actual -= 1
    return diccionario