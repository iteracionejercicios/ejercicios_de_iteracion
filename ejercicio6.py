#tipo cuenta
#definimos una serie de cuentas con sus movimientos y saldos
cuentas = {
    "cuenta1": {"Saldo": 73764, "Nombre": "ElG",  "Movimientos": [190, 289, 456, 677, 22]}
    "cuenta2": {"Saldo": 12345, "Nombre": "Paco",  "Movimientos": [222, 33, 785, 478, 10]}
    "cuenta3": {"Saldo": 12345, "Nombre": "Pascual",  "Movimientos": [222, 33, 785, 478, 10]}
}


print (cuentas)
def saldo_final(cuentas): #definiremos el saldo final
    for cuenta in cuentas:
        for movimiento in cuentas[cuenta]["Movimientos"]: #definimos la funcion para que se sumen los movimientos
            cuentas[cuenta]["Saldo"] += movimiento #obtendremos el saldo final
    return cuentas
print (saldo_final(cuentas))
 