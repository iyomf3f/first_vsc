"""Profe se me olvido entregarlo D:"""
CONT_TOTAL = 0
CONT_HERRA_INA = 0
POR_HERRA_INA = 0
PRECIO_HIGH_todoferre = 0
NOMBRE_HIGH_todoferre = 0
CANTIDAD_IGUALES = 0
with open('weas//ferreteria.txt', 'r') as file:
    for linea in file:
        linea = linea.strip().split(',')
        partes = linea
        NOMBRE_PRODUCTO = partes[0]
        CANTIDAD_PRODUCTO = int(partes[1])
        CANTIDAD_MAX = int(partes[2])
        PRECIO_U = int(partes[3])
        TIPO_PRODUCTO = partes[4]
        DISTRIBUIDOR = partes[5]

        CONT_TOTAL += 1

        if TIPO_PRODUCTO == 'Herramientas Inalambricas':
            CONT_HERRA_INA += 1
        if DISTRIBUIDOR == 'Todo Ferretero':
            if PRECIO_U > PRECIO_HIGH_todoferre:
                PRECIO_HIGH_todoferre = PRECIO_U
                NOMBRE_HIGH_todoferre = NOMBRE_PRODUCTO
        if CANTIDAD_PRODUCTO == CANTIDAD_MAX:
            CANTIDAD_IGUALES += 1

# Porcentaje de productos que tienen la familia “Herramientas Inalambricas”

if CONT_TOTAL > 0:
    POR_HERRA_INA = (CONT_HERRA_INA / CONT_TOTAL) * 100
    print(f'El porcentaje de Herramientas Inalambricas es %{POR_HERRA_INA}')
else:
    print('No hay ningun producto')

# Producto más caro distribuido por “Todo Ferretero”.
print(f"El producto mas caro de 'Todo Ferretero' es: {NOMBRE_HIGH_todoferre} con un costo de ${PRECIO_HIGH_todoferre}")

# Mostrar la cantidad de los productos que tienen su cantidad actual igual a su cantidad máxima.

print(f'El numero de productos que tienen su cantidad actual igual a su cantidad máxima es de {CANTIDAD_IGUALES} productos')