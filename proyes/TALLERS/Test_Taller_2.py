"""Postplant"""
# Taller 1
# Integrantes: Paulo Zarate y
# Num aleatorios por rut: [6, 12, 8, 3, 10, 17]
##################################################

TOTAL_ERR = 0
def verify():
    '''Funcion para verificar datos'''
    num_err = 0
    while True:
        try:
            variable = int(input("Ingrese un número: "))
            if variable >= 1:
                break
            else:
                num_err += 1
                raise ValueError
        except ValueError:
            continue

    return variable, num_err

def veri_num(numero):
    """verificador de num"""
    errores = 0
    try:
        numero = int(numero)
        if numero > 0:
            veri = True
            return veri, errores
        else:
            raise ValueError
    except ValueError:
        errores += 1
        veri = False
        return veri, errores
SUCURSALES = [
    'Space X',
    'Google',
    'Amazon'
    ]
MESES = [
    'Enero',
    'Febrero',
    'Marzo',
    'Abril',
    'Mayo',
    'Junio',
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre'
    ]

monto_total_sucursales = {sucursal: 0 for sucursal in SUCURSALES}

while True:
    sucursal = input("Ingrese una sucursal: ")
    precio_prod = int(input('precio: '))
    cant_prod = int(input('Cantidad: '))
    monto_total_sucursales[sucursal] += (precio_prod * cant_prod)