def mcd(a, b):  # Convertir a y b a valores absolutos para asegurar que sean números positivos
    a = abs(a)
    b = abs(b)
   # Iniciar un bucle mientras a no sea igual a b
    while a != b:
      # Si a es mayor que b, restar b de a
        if a > b:
            a = a - b
         # Si b es mayor que a, restar a de b
        else:
            b = b - a
  # Cuando a y b son iguales, devolver su valor (el MCD)  
    return a