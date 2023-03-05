def mcd(a, b):
    if b != 0:  # Si b no es igual a cero, calcula el MCD de b y el resto de a/b, y así sucesivamente hasta llegar a cero
        return mcd(b, a % b)
        