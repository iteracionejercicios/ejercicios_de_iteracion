def raiz_cuadrada_entera(n):
  # si el número es cero, su raíz cuadrada es cero
    if n == 0:
      # si el número es uno, su raíz cuadrada es uno
        return 0
    if n == 1:
        return 1
      
    # comenzamos asumiendo que la raíz cuadrada es n // 2
    r = n // 2
  # mientras el cuadrado de la raíz asumida sea mayor que el número, actualizamos la raíz con el promedio de esta y la división entera del número entre la raíz actual
    while r**2 > n:
        r = (r + n // r) // 2
   # cuando el ciclo termina, la variable r tiene el valor de la raíz cuadrada entera
    return r