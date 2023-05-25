"""Function printing python version."""

# Taller 2
# Integrantes: Paulo Zarate
####################################################################################################

MSG_MENU_M = """
 ----------------------------------------------------------
 ----------------------------------------------------------
 1. Ingresar Datos.
 2. Leer datos.
 3. Salir
 ----------------------------------------------------------
 Elegir: """
MSG_MENU_W = """
 ----------------------------------------------------------
 ----------------------------------------------------------
 1. Registro de ventas.
 2. Registro de producciónes.
 3. Registro de transacciones.
 4. Salir.
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

def veri_menus(opciones, select):
    """Verificador de menus"""

    opciones_totales = []

    for opcion in range(1, opciones + 1):
        opciones_totales.append(opcion)

    try:
        select = int(select)
        if select in opciones_totales:
            veri = True
            return veri, select
        else:
            raise ValueError
    except ValueError:
        veri = False
        return veri, select

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

def veri_opcion(opcion):
    """Verificador de inicio"""

    try:
        if opcion == 'Y':
            veri = 'Y'
            return veri
        elif opcion == 'N':
            veri = 'N'
            return veri
        else:
            raise ValueError("Opción de inicio inválida. Por favor, ingrese 'Y' o 'N'.")

    except ValueError:
        veri = False
        return veri

def veri_sucur(sucursal):
    """Verificador de sucursal"""

    try:
        if sucursal in SUCURSALES:
            veri = True
            return veri, sucursal
        else:
            raise ValueError
    except ValueError:
        veri = False
        return veri, sucursal

def veri_fecha(fecha):
    """Verificador de fechas"""

    try:
        dia_n, dia, mes, anho = fecha.split('/')
        dia = int(dia)
        anho = int(anho)
        dia_n = dia_n.title()
        mes = mes.title()
        if dia_n in DIAS and 1 <= dia <= 31 and mes in MESES and 1900 <= anho <= 2023:
            veri = True
            fecha = f'{dia_n}/{dia}/{mes}/{anho}'
            return veri, fecha, dia_n, dia, mes, anho
        else:
            raise ValueError
    except (ValueError, IndexError,TypeError):
        veri = False
        dia = ''
        dia_n = ''
        mes = ''
        anho = ''
        return veri, fecha, dia_n, dia, mes, anho

def veri_num(numero):
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

def veri_idprod(ide):
    """Verificador de ID's"""

    try:
        if ide in ID_PRODUCTOS:
            veri = True
            return veri, ide
        else:
            raise ValueError
    except ValueError:
        veri = False
        return veri, ide

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

def reg_ventas():
    """Funcion para registrar ventas"""

    total_err = 0
    with open('datos_de_empresa.txt','a', encoding='utf-8') as file:
        while True:
            # Input de Sucursales
            while True:
                sucursal = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 En que sucursal va a ingresar las ventas?
 Lista de sucursales: Space X, Google, Amazon
 Respuesta: """)
                veri, sucursal = veri_sucur(sucursal)
                if veri:
                    break
                else:
                    print('\n Sucursal invalida. Ingrese una sucursal que este en la lista!!!'
                    '\n (Recuerde usar MAYUSCULAS)')
                    total_err += 1
                    continue
            # Input de Fecha
            while True:
                fecha = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Ingrese una fecha para la/s venta/s.
 Con el siguiente formato:'Lunes/12/Septiembre/2010'.
 Respuesta: """)
                veri, fecha, dia_n, dia, mes, anho = veri_fecha(fecha)
                if veri:
                    break
                else:
                    print('\n Fecha no valida. Asegurese de ingresar en un formato valido!!!')
                    total_err += 1
                    continue
            # Input de numero de ventas
            while True:
                num_de_ventas = input(f"""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Cuantas ventas va a ingresar?
 Para la feha: {fecha}
 Respuesta: """)
                veri, num_de_ventas = veri_num(num_de_ventas)
                if veri:
                    break
                else:
                    print('\n Numero de ventas no valido. Solo puede ingresar numeros positivos!!!')
                    total_err += 1
                    continue

            for venta in range(num_de_ventas):
                # Input de ID de producto
                while True:
                    prod_id = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Ingrese el ID del producto. 
 (formato E4**, E401 hasta E410)
 Respuesta: """)
                    veri, prod_id = veri_idprod(prod_id)
                    if veri:
                        break
                    else:
                        print('\n Ingrese una ID valida!!! (ejemplo: E401, E402 ... E409,E410)')
                        total_err += 1
                        continue
                # Input de cantidad de producto con la ID anterior
                while True:
                    cant_de_producto = input(f"""
 ----------------------------------------------------------
 ----------------------------------------------------------  
 Cuantas unidades se vendieron del producto {prod_id}?
 Respuesta: """)
                    veri, cant_de_producto = veri_num(cant_de_producto)

                    if veri:
                        break
                    else:
                        print('\n Numero de unidades invalida. Asegurese de ingresar valores positivos!!!')
                        total_err += 1
                        continue
                # Input del precio del procducto con la ID anterior
                while True:
                    precio_producto = input(f"""
 ----------------------------------------------------------
 ----------------------------------------------------------
 A que precio se vendio {prod_id}?
 (En dolares)
 Respuestas: $""")
                    veri, precio_producto = veri_num_float(precio_producto)
                    if veri:
                        break
                    else:
                        print('\n Ingrese un precio valido. Solo puedo ingresar valores positivos!!!')
                        total_err += 1
                        continue
                num_de_ventas -= 1
                venta_txt = (f'venta,{sucursal},{dia_n},{dia},{mes},{anho},'
                f'{prod_id},{cant_de_producto},{precio_producto},{total_err}\n')
                file.write(venta_txt)
                print("""
 ----------------------------------------------------------

 Venta ingresada con EXITO.

 ----------------------------------------------------------""")
            while True:
                opcion = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Quiere seguir ingresando ventas?
 Y/N: """).upper()
                veri = veri_opcion(opcion)
                if veri:
                    break
                else:
                    print('\n Solo puede responder con Y o N!!!')
                    continue
            if opcion != 'Y':
                break

def reg_produc():
    """Funcion de registro de produccion"""

    total_err = 0

    with open('datos_de_empresa.txt','a', encoding='utf-8') as file:
        while True:
            # Input de Fecha.
            while True:
                fecha = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Ingrese una fecha para la/s producion/es.
 Con el siguiente formato:'Lunes/12/Septiembre/2010'.
 Respuesta: """)
                veri, fecha, dia_n, dia, mes, anho = veri_fecha(fecha)
                if veri:
                    break
                else:
                    print('\n Fecha no valida. Asegurese de ingresar en el formato valido!!!')
                    total_err += 1
                    continue
            # Input de cantidad de produciones.
            while True:
                cant_de_produccion = input(f"""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Cuantas producciones hubieron en el dia '{fecha}'?
 Respuesta: """)
                veri, cant_de_produccion = veri_num(cant_de_produccion)
                if veri:
                    break
                else:
                    print('\n Cantidad de produciones invalida.'
                    'Asegurese de ingresar valores positivos!!!')
                    total_err += 1
                    continue
            for producion in range(cant_de_produccion):
                while True:
                    # Formato de id E4** ejemplo E402, etc...
                    prod_id = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Ingrese el ID del producto. 
 (formato E4**, E401 hasta E410)
 Respuesta: """)
                    veri, prod_id = veri_idprod(prod_id)
                    if veri:
                        break
                    else:
                        print('\n Ingrese una ID valida!!! (ejemplo: E401, E402 ... E409,E410)')
                        total_err += 1
                        continue
                # Input de cantidad de unidades de la produccion
                while True:
                    cant_de_produccion = input(f"""
 ----------------------------------------------------------
 ----------------------------------------------------------  
 Cuantas unidades se produjeron del producto {prod_id}?
 Respuesta: """)
                    veri, cant_de_produccion = veri_num(cant_de_produccion)
                    if veri:
                        break
                    else:
                        print('\n Numero de unidades invalida. Asegurese de ingresar valores positivos!!!')
                        total_err =+1
                        continue
                # Input para el costo de prod para x cantidad de unidades
                while True:
                    costo_produccion = input(f"""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Que costo de produccion tuvo producir {cant_de_produccion} del producto {prod_id}? 
 (En dolares)
 Respuesta: $""")
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
                print("""
 ----------------------------------------------------------

 Produccion ingresada con EXITO.

 ----------------------------------------------------------""")
            while True:
                opcion = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Quiere seguir ingresando producciones? 
 Y/N: """).upper()
                veri = veri_opcion(opcion)
                if veri:
                    break
                else:
                    print('\n Solo puede responder con Y o N')
                    continue
            if opcion != 'Y':
                break

def reg_fina():
    """Funcion para registrar finanzas de la empresa"""

    total_err = 0

    with open('datos_de_empresa.txt','a', encoding='utf-8') as file:
        while True:
            # Input de numero de transacciones
            while True:
                num_de_tran = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Cuantas transacciones va a ingresar?
 Respuesta: """)
                veri, num_de_tran = veri_num(num_de_tran)
                if veri:
                    break
                else:
                    print('\n Numero de transacciones no valido.'
                    'Solo puede ingresar valores positivos!!!')
                    total_err += 1
                    continue

            for transac in range(num_de_tran):
                while True:
                    iog = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 La transaccion es Ingreso o Gasto?
 Respuesta: """)
                    veri, iog = veri_ingresos(iog)
                    if veri:
                        break
                    else:
                        print('\n Solo pude responder con Ingreso o Gasto.'
                         'Recuerde usar mayusculas en la primera letra!!!')
                        total_err += 1
                        continue
                while True:
                    monto = input(f"""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Introdusca su {iog}.
 Respuesta: $""")
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
                print("""
 ----------------------------------------------------------

 Transaccion ingresada con EXITO.

 ----------------------------------------------------------""")
            while True:
                opcion = input("""
 ----------------------------------------------------------
 ----------------------------------------------------------
 Quiere seguir ingresando ventas? 
 Y/N: """).upper()
                veri = veri_opcion(opcion)
                if veri:
                    print('\n Solo puede responder con Y o N')
                    break
                else:
                    continue

            if opcion != 'Y':
                break

def estadisticas():
    """Funcion que calcula las estadisticas a mostrar"""

    veri =True

    while veri:

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
                    if mes == 'Julio' or mes == 'Junio' or mes == 'Agosto':
                        jja_ventas += (precio_producto * cant_producto)

                elif tipo == 'produccion':
                    dia = part[1]
                    mes = part[3]
                    costo_produccion = float(part[7])
                    errores = int(part[8])

                    # 10. Cantidad de veces que un hubo un error de limpieza de datos.
                    total_errores += errores

                    #  6. Promedio de costos de producción en fin de semana.
                    if dia == 'Sabado' or dia == 'Domingo':
                        costo_produccion_total_sd += costo_produccion
                        cont_produccion_sd += 1

                    #  8. Margen neto para los meses de junio, julio y agosto.
                    if mes == 'Julio' or mes == 'Junio' or mes == 'Agosto':
                        jja_costo_produccion += costo_produccion

                elif tipo == 'transaccion':
                    errores = int(part[2])

                    # 10. Cantidad de veces que un hubo un error de limpieza de datos.
                    total_errores += errores

            # 17. Indicar el mes que tuvo más ventas.
            cant_mes_mayor_venta = max(meses_contadores)
            nombre_mes_mayor = MESES[meses_contadores.index(cant_mes_mayor_venta)]

            if cant_mes_mayor_venta == 0:
                nombre_mes_mayor = 'Ninguno'
                cant_mes_mayor_venta = 'Ninguno'

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

            msg_estadistica = f"""
 ----------------------------------------------------------
 Cantidad de veces que un hubo un error de limpieza de datos: {msg_total_errores}

 Indicar el mes que tuvo más ventas. Mes: {nombre_mes_mayor} Numero de ventas: {cant_mes_mayor_venta}

 Cantidad de productos vendidos para el 2023: {msg_cant_producto_2023}

 Promedio de costos de producción en fin de semana: {promedio_cost_produccion_sd}

 Margen neto para los meses de Junio, Julio y Agosto: {margen_neto_jja_txt}
 """
            print(msg_estadistica)
            for sucursal, monto in zip(SUCURSALES, monto_total_sucursales):
                print(f' Monto total de {sucursal} es: {monto}\n')
            while True:
                print(' ----------------------------------------------------------')
                opcion = input(' Escriba "Y" para continuar: ').upper()
                veri = veri_opcion(opcion)
                if veri:
                    veri = False
                    break
                else:
                    continue

def main():
    """Función principal"""

    while True:
        # Menú principal.
        while True:
            select_main = input(MSG_MENU_M)
            veri, opcion_main = veri_menus(3, select_main)
            if veri:
                break
            else:
                continue

        # Ingresar Datos.
        if opcion_main == 1:
            while True:
                select_write = input(MSG_MENU_W)
                veri, opcion_write = veri_menus(4, select_write)
                if veri:
                    break
                else:
                    continue

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
                print('\n ----------------------------------------------------------\n'
                ' Volviendo al menu princimal...')

        # Mostrar estadísticas.
        elif opcion_main == 2:
            estadisticas()

        # Salir de la app.
        elif opcion_main == 3:
            print("""
 ----------------------------------------------------------
 Saliendo de la app...""")
            break

if __name__ == '__main__':
    main()
