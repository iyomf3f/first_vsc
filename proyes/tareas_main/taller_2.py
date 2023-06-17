""" Taller numero #2 """

# Taller 2
# Integrantes: Paulo Zarate
####################################################################################################

# Listas / Mensajes

MSG_MENU_M = """
 Menu Principal
 ----------------------------------------------------------
 ----------------------------------------------------------
 1. Registrar Datos.
 2. Leer datos.
 3. Salir
 ----------------------------------------------------------
 Elegir: """
MSG_MENU_W = """
 Menu de Registros
 ----------------------------------------------------------
 ----------------------------------------------------------
 1. Registrar venta.
 2. Registrar producción.
 3. Registrar transaccion.
 4. Volver.
 ----------------------------------------------------------
 Elegir: """
SUCURSALES = [
    'Space X',
    'Google',
    'Amazon'
    ]
DIAS = [
    'Lunes',
    'Martes',
    'Miercoles',
    'Jueves',
    'Viernes',
    'Sabado',
    'Domingo'
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
ID_PRODUCTOS = [
    'E401',
    'E402',
    'E403',
    'E404',
    'E405',
    'E406',
    'E407',
    'E408',
    'E409',
    'E410'
    ]

# Funciones para menus y repetir funcion o seguir.

def veri_menus(opciones,msg):
    """Verificador de menus"""

    opciones_totales = []

    while True:
        try:
            select = int(input(msg))

            opciones_totales = list(range(1,opciones + 1))

            if select in opciones_totales:
                return select
            else:
                raise ValueError
        except ValueError:
            print(f'\nENTRADA NO VALIDA. Ingrese un numero del 1 al {opciones}')
            continue

def repetir_o_no(tipo):
    """Verificador de 'seguir o no' en ingresos de registro y mostrando estadisticas"""

    if tipo == 1:
        vpt = 'seguir ingresando ventas?'
    elif tipo == 2:
        vpt = 'seguir ingresando producciones?'
    elif tipo == 3:
        vpt = 'seguir ingresando transacciones?'
    elif tipo == 4:
        vpt = 'salir de las estadisticas?'

    while True:
        try:
            opcion = input(
            f' ----------------------------------------------------------\n'
            f' Quiere {vpt}?\n'
            f' Y/N: ')

            if opcion == 'Y' or opcion == 'N':
                return opcion
            else:
                raise ValueError

        except ValueError:
            print('\n Solo puede responder con Y o N!!!')
            continue

# Funciones para verificar entradas de datos.

def veri_ingresos(iog):
    """Verificador de ingresos o gastos"""

    try:
        if iog == 'Ingreso':
            veri = True
            return veri, iog
        elif iog == 'Gasto':
            veri = True
            return veri, iog
        else:
            raise ValueError
    except ValueError:
        veri = False
        return veri, iog

def veri_monto(monto,iog):
    """Verificador de montos"""

    try:
        monto = int(monto)
        if iog == 'Ingreso':
            if monto > 0:
                veri = True
                return veri, monto
            else:
                raise ValueError
        elif iog == 'Gasto':
            if monto < 0:
                veri = True
                return veri, monto
            else:
                raise ValueError
    except ValueError:
        veri = False
        return veri, monto

def veri_sucur():
    """Verificador de sucursal"""

    errores = 0

    while True:
        try:
            sucursal = input(
            ' ----------------------------------------------------------\n'
            ' ----------------------------------------------------------\n'
            ' En que sucursal va a ingresar las ventas?\n'
            ' Lista de sucursales: Space X, Google, Amazon\n'
            ' Respuesta: ')
            if sucursal in SUCURSALES:
                return sucursal, errores
            else:
                raise ValueError
        except ValueError:
            errores += 1
            print('\n SUCURSAL INVALIDA. Ingrese una sucursal que este en la lista!!!'
            '\n (Recuerde usar MAYUSCULAS)')
            continue

def veri_fecha(tipo):
    """Verificador de fechas"""

    errores = 0

    if tipo == 'venta':
        texto = "la/s venta/s."
    elif tipo == 'produccion':
        texto = "la/s producion/es"


    while True:
        try:
            fecha = input(
                f' ----------------------------------------------------------\n'
                f' ----------------------------------------------------------\n'
                f' Ingrese una fecha para {texto}\n'
                f' Con el siguiente formato: Lunes/12/Septiembre/2010.\n'
                f' Respuesta: ')
            dia_n, dia, mes, anho = fecha.split('/')
            dia = int(dia)
            anho = int(anho)
            dia_n = dia_n.title()
            mes = mes.title()
            if dia_n in DIAS and 1 <= dia <= 31 and mes in MESES and 1900 <= anho <= 2023:
                fecha = f'{dia_n}/{dia}/{mes}/{anho}'
                return fecha, dia_n, dia, mes, anho, errores
            else:
                raise ValueError
        except (ValueError, IndexError,TypeError):
            print('\n FECHA NO VALIDA. Asegurese de ingresar en un formato valido!!!')
            errores += 1
            continue

def veri_num_int(numero):
    """verificador de num"""

    try:
        numero = int(numero)
        if numero > 0:
            veri = True
            return veri, numero
        else:
            raise ValueError
    except ValueError:
        veri = False
        return veri, numero

def veri_num_float(numero):
    """verificador de num"""

    try:
        numero = float(numero)
        if numero > 0:
            veri = True
            return veri, numero
        else:
            raise ValueError
    except ValueError:
        veri = False
        return veri, numero

def veri_idprod():
    """Verificador de ID's"""

    while True:

        errores = 0

        try:
            prod_id = input(
                ' ----------------------------------------------------------\n'
                ' ----------------------------------------------------------\n'
                ' Ingrese el ID del producto. (formato E4**, E401 hasta E410)\n'
                ' Respuesta: ')
            if prod_id in ID_PRODUCTOS:
                return prod_id, errores
            else:
                raise ValueError
        except ValueError:
            print('\n ID NO VALIDA. (ejemplo: E401, E402 ... E409,E410)')
            errores += 1
            continue

# Funciones de registro / estadisticas.

def reg_ventas():
    """Funcion para registrar ventas"""

    total_err = 0
    with open('datos_de_empresa.txt','a', encoding='utf-8') as file:
        while True:
            # Input de Sucursales
            sucursal, errores = veri_sucur()
            total_err += errores

            # Input de Fecha
            fecha, dia_n, dia, mes, anho, errores = veri_fecha('venta')
            total_err += errores

            # Input de numero de ventas
            while True:
                num_de_ventas = input(
                f' ----------------------------------------------------------\n'
                f' ----------------------------------------------------------\n'
                f' Cuantas ventas va a ingresar?\n'
                f' Para la feha: {fecha}\n'
                f' Respuesta: ')
                veri, num_de_ventas = veri_num_int(num_de_ventas)
                if veri:
                    break
                else:
                    print('\n Numero de ventas no valido. Solo puede ingresar numeros positivos!!!')
                    total_err += 1
                    continue

            for venta in range(num_de_ventas):

                # Input de ID de producto
                prod_id, errores = veri_idprod()
                total_err += errores

                # Input de cantidad de producto con la ID anterior
                while True:
                    cant_de_producto = input(
                        f' ----------------------------------------------------------\n'
                        f' ----------------------------------------------------------\n'
                        f' Cuantas unidades se vendieron del producto: {prod_id}?\n'
                        f' Respuesta: ')
                    veri, cant_de_producto = veri_num_int(cant_de_producto)
                    if veri:
                        break
                    else:
                        print('\n NUMERO DE UNIDADES INVALIDA. Asegurese de ingresar valores positivos!!!')
                        total_err += 1
                        continue

                # Input del precio del procducto con la ID anterior
                while True:
                    precio_producto = input(
                    f' ----------------------------------------------------------\n'
                    f' ----------------------------------------------------------\n'
                    f' A que precio se vendio la unidad de {prod_id}? (En dolares)\n'
                    f' Respuestas: $')
                    veri, precio_producto = veri_num_float(precio_producto)
                    if veri:
                        break
                    else:
                        print('\n PRECIO INVALIDO. Solo puedo ingresar valores positivos!!!')
                        total_err += 1
                        continue

                venta_txt = (f'venta,{sucursal},{dia_n},{dia},{mes},{anho},'
                f'{prod_id},{cant_de_producto},{precio_producto},{total_err}\n')
                file.write(venta_txt)
                print(
                ' ----------------------------------------------------------\n\n'
                ' Venta ingresada con EXITO.\n\n'
                ' ----------------------------------------------------------')
            
            opcion = repetir_o_no(1)

            if opcion == 'N':
                break

def reg_produc():
    """Funcion de registro de produccion"""

    total_err = 0

    with open('datos_de_empresa.txt','a', encoding='utf-8') as file:
        while True:
            # Input de Fecha.
            fecha, dia_n, dia, mes, anho, errores = veri_fecha('produccion')
            total_err += errores

            # Input de cantidad de produciones.
            while True:
                cant_de_produccion = input(
                f' ----------------------------------------------------------\n'
                f' ----------------------------------------------------------\n'
                f' Cuantas producciones hubieron en el dia {fecha}?\n'
                f' Respuesta: ')
                veri, cant_de_produccion = veri_num_int(cant_de_produccion)
                if veri:
                    break
                else:
                    print(
                    '\n Cantidad de produciones invalida.\n'
                    ' Asegurese de ingresar valores positivos!!!')
                    total_err += 1
                    continue
            for producion in range(cant_de_produccion):

                # Input de id de producto
                prod_id, errores = veri_idprod()
                total_err += errores

                # Input de cantidad de unidades de la produccion
                while True:
                    cant_de_produccion = input(
                    f' ----------------------------------------------------------\n'
                    f' ----------------------------------------------------------\n'
                    f' Cuantas unidades se produjeron del producto {prod_id}?\n'
                    f' Respuesta: ')

                    veri, cant_de_produccion = veri_num_int(cant_de_produccion)
                    if veri:
                        break
                    else:
                        print('\n Numero de unidades invalida. Asegurese de ingresar valores positivos!!!')
                        total_err =+1
                        continue

                # Input para el costo de prod para x cantidad de unidades
                while True:
                    costo_produccion = input(
                        f' ----------------------------------------------------------\n'
                        f' ----------------------------------------------------------\n'
                        f' Que costo de produccion tuvo producir {cant_de_produccion} unidades del producto {prod_id}?\n'
                        f' Respuesta: $')
                    veri, costo_produccion = veri_num_float(costo_produccion)
                    if veri:
                        break
                    else:
                        print('\n Ingrese un costo valido. Solo puede ingresar valores positivos!!!')
                        total_err += 1
                        continue

                produccion_txt = (f'produccion,{dia_n}, {dia}, {mes}, {anho},'
                f'{prod_id},{cant_de_produccion},{costo_produccion},{total_err}\n')
                file.write(produccion_txt)
                print(
                ' ----------------------------------------------------------\n\n'
                ' Produccion ingresada con EXITO.\n\n'
                ' ----------------------------------------------------------')
            opcion = repetir_o_no(2)

            if opcion == 'N':
                break

def reg_fina():
    """Funcion para registrar finanzas de la empresa"""

    total_err = 0

    with open('datos_de_empresa.txt','a', encoding='utf-8') as file:
        while True:
            # Input de numero de transacciones
            while True:
                num_de_tran = input(
                ' ----------------------------------------------------------\n'
                ' ----------------------------------------------------------\n'
                ' Cuantas transacciones va a ingresar?\n'
                ' Respuesta: ')
                veri, num_de_tran = veri_num_int(num_de_tran)
                if veri:
                    break
                else:
                    print('\n Numero de transacciones no valido.'
                    'Solo puede ingresar valores positivos!!!')
                    total_err += 1
                    continue

            for transac in range(num_de_tran):
                while True:
                    iog = input(
                    ' ----------------------------------------------------------\n'
                    ' ----------------------------------------------------------\n'
                    ' La transaccion es Ingreso o Gasto?\n'
                    ' Respuesta: ')
                    veri, iog = veri_ingresos(iog)
                    if veri:
                        break
                    else:
                        print('\n Solo pude responder con Ingreso o Gasto.'
                         'Recuerde usar mayusculas en la primera letra!!!')
                        total_err += 1
                        continue
                while True:
                    monto = input(
                    f' ----------------------------------------------------------\n'
                    f' ----------------------------------------------------------\n'
                    f' Introdusca su {iog}.\n'
                    f' Respuesta: $')
                    veri, monto = veri_monto(monto,iog)
                    if veri:
                        break
                    else:
                        print('\n Monto no valido.'
                        'Recuerde que los Gastos son negativos y los Ingresos positivos!!!')
                        total_err += 1
                        continue

                num_de_tran -= 1
                transaccion_txt = f'transaccion, {monto},{total_err}\n'
                file.write(transaccion_txt)
                print(
                ' ----------------------------------------------------------\n\n'
                ' Transaccion ingresada con EXITO.\n\n'
                ' ----------------------------------------------------------')
            opcion = repetir_o_no(3)

            if opcion == 'N':
                break

def estadisticas():
    """Funcion que calcula las estadisticas a mostrar"""
    # 17. Indicar el mes que tuvo más ventas.
    #  3. Monto total de ventas por cada sucursal.
    # 10. Cantidad de veces que un hubo un error de limpieza de datos.
    # 12. Cantidad de productos vendidos para el 2023.
    #  8. Margen neto para los meses de junio, julio y agosto.
    #  6. Promedio de costos de producción en fin de semana.

    try:
        while True:

            total_errores = 0
            cant_producto_2023 = 0
            jja_ventas = 0
            jja_costo_produccion = 0
            costo_produccion_total_sd = 0
            cont_produccion_sd = 0

            meses_contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            monto_total_sucursales = [0, 0, 0]

            with open('datos_de_empresa.txt','r', encoding='utf-8') as file:
                for lines in file:
                    part = lines.strip().split(',')
                    tipo = part[0]
                    if tipo == 'venta':
                        sucursal = part[1]
                        dia = part[2]
                        mes = part[4]
                        anho = int(part[5])
                        cant_producto = int(part[7])
                        precio_producto = float(part[8])
                        errores = int(part[9])

                                    # 17. Indicar el mes que tuvo más ventas.
                        meses_contadores[MESES.index(mes)] += 1

                                    #  3. Monto total de ventas por cada sucursal.
                        monto_total_sucursales[SUCURSALES.index(sucursal)] += (precio_producto * cant_producto)

                                    # 10. Cantidad de veces que un hubo un error de limpieza de datos.
                        total_errores += errores

                                    # 12. Cantidad de productos vendidos para el 2023.
                        if anho == 2023:
                            cant_producto_2023 += cant_producto

                                    #  8. Margen neto para los meses de junio, julio y agosto.
                        if mes in ['Julio','Junio','Agosto']:
                            jja_ventas += (precio_producto * cant_producto)

                    elif tipo == 'produccion':
                        dia = part[1]
                        mes = part[3]
                        costo_produccion = float(part[7])
                        errores = int(part[8])

                                    # 10. Cantidad de veces que un hubo un error de limpieza de datos.
                        total_errores += errores

                                    #  6. Promedio de costos de producción en fin de semana.
                        if dia in ['Sabado','Domingo']:
                            costo_produccion_total_sd += costo_produccion
                            cont_produccion_sd += 1

                                    #  8. Margen neto para los meses de junio, julio y agosto.
                        if mes in ['Julio','Junio','Agosto']:
                            jja_costo_produccion += costo_produccion

                    elif tipo == 'transaccion':
                        errores = int(part[2])

                                    # 10. Cantidad de veces que un hubo un error de limpieza de datos.
                        total_errores += errores

                            # 17. Indicar el mes que tuvo más ventas.
                cant_mes_mayor_venta = max(meses_contadores)
                nombre_mes_mayor = MESES[meses_contadores.index(cant_mes_mayor_venta)]
                
                            #Bloque para determinar si algun valor es 0 para cambiarlo por un mensaje que indique 'No hube/registro/hay x cosa'
                if cant_mes_mayor_venta == 0:
                    nombre_mes_mayor = 'Ninguno'
                    cant_mes_mayor_venta = '0'
                
                if cont_produccion_sd > 0:
                    promedio_cost_produccion_sd = costo_produccion_total_sd / cont_produccion_sd
                else:
                    promedio_cost_produccion_sd = 'No hubo producion en fin de semana.'

                if jja_ventas > 0 or jja_costo_produccion > 0:
                    margen_neto_jja = jja_ventas - jja_costo_produccion
                    margen_neto_jja_txt = f'${margen_neto_jja}'
                else:
                    margen_neto_jja_txt = ('No hubo ventas ni produccion en'
                    ' los meses de Junio, Julio y Agosto.')

                if total_errores > 0:
                    msg_total_errores = total_errores
                else:
                    msg_total_errores = 'No hubo errores al ingresar los datos.'

                if cant_producto_2023 > 0:
                    msg_cant_producto_2023 = cant_producto_2023
                else:
                    msg_cant_producto_2023 = 'No se vendio ningun producto en 2023'



                            # 17. Indicar el mes que tuvo más ventas.

                    # Si la cantidad de ventas se repite en mas de un mes se buscan e imprimen con una iteracion
                    # Inicio de print's de datos
                if meses_contadores.count(cant_mes_mayor_venta) > 1:
                    print(
                        f'\n'
                        f' ----------------------------------------------------------\n'
                        f' Meses con la mayor cantidad de ventas ({cant_mes_mayor_venta}):'
                        )
                    for mess, cant_de_ventas in zip(MESES, meses_contadores):
                        if cant_de_ventas == cant_mes_mayor_venta:
                            print(f' {mess}')
                else:
                    print(
                        f' ----------------------------------------------------------\n'
                        f' El mes con mas ventas: {nombre_mes_mayor}\n' 
                        f' Con: {cant_mes_mayor_venta} ventas.')

                print(
                    f' Cantidad de veces que un hubo un error de limpieza de datos: {msg_total_errores}\n'
                    f' Cantidad de productos vendidos para el 2023: {msg_cant_producto_2023}\n'
                    f' Promedio de costos de producción en fin de semana: {promedio_cost_produccion_sd}\n'
                    f' Margen neto para los meses de Junio, Julio y Agosto: {margen_neto_jja_txt}\n'
                    )

                for sucursal, monto in zip(SUCURSALES, monto_total_sucursales):
                    print(f' Monto total de {sucursal} es: {monto}\n')

                opcion = repetir_o_no(4)
                if opcion == 'Y':
                    break

    except Exception as error:
        print(error)
        print('\n Uno o mas datos del archivo que ingreso estan erroneos!!\n')


def main():
    """Función principal"""

    # Menú principal.
    while True:
        opcion_main = veri_menus(3,MSG_MENU_M)

        # Menu para ingresar Datos.
        if opcion_main == 1:
            opcion_write = veri_menus(4,MSG_MENU_W)

            # Registro de ventas.
            if opcion_write == 1:
                reg_ventas()

            # Registro de producciones.
            elif opcion_write == 2:
                reg_produc()

            # Registro de finanzas.
            elif opcion_write == 3:
                reg_fina()

            # Volver al menu principal
            elif  opcion_write == 4:
                print(
                '\n'
                ' Volviendo al menu princimal...'
                ' ----------------------------------------------------------\n')

        # Opcion para mostrar estadísticas.
        elif opcion_main == 2:
            estadisticas()

        # Salir de la app.
        elif opcion_main == 3:
            print(
            '\n'
            ' ----------------------------------------------------------\n'
            ' Saliendo de la app...')
            break

if __name__ == '__main__':
    main()
