"""Function printing python version."""
# Taller 1
# Integrantes: Paulo Zarate
####################################################################################################
MSG_ERROR = 'Error al ingresar dato'
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
2. Registro de producción.
3. Registro de finanzas.
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
TOTAL_ERR = 0

def veri_monto(monto,iog):
    """Verificador de montos"""
    try:
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
        return veri, monto


def veri_start(start):
    """Verificador de inicio"""
    try:
        if start == 'Y':
            veri = 'Y'
            return veri
        elif start == 'N':
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
        dia_n = dia_n.capitalize()
        mes = mes.capitalize()
        if dia_n in DIAS and 1 <= dia <= 31 and mes in MESES and 1900 <= anho<= 2023:
            veri = True
            fecha = f'{dia_n}/{dia}/{mes}/{anho}'
            return veri, fecha, dia_n, dia, mes, anho
        else:
            raise ValueError
    except Exception:
        print("Error:")
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
        elif iog == 'Gasto':
            veri = True
            iog = 'Gasto'
            return veri, iog
        else:
            raise ValueError
    except ValueError:
        veri = False
        return veri, iog



def reg_ventas():

    """Funcion para registrar ventas"""

    total_err = 0

    while True:
        with open('datos_de_empresa.txt','a', encoding='utf-8') as file:

            # Input de Sucursales

            while True:
                sucursal = input('En que sucursal va a ingresar las ventas?: ')
                veri, sucursal = veri_sucur(sucursal)
                if veri:
                    break
                else:
                    total_err += 1
                    print('No ingreso una sucursal valida!')
                    continue

            # Input de Fecha

            while True:
                fecha = input('Ingrese fecha con formato: Lunes/12/Septiembre/2010: ')
                veri, fecha, dia_n, dia, mes, anho = veri_fecha(fecha)
                if veri:
                    msg_ventas = f"""
----------------------------------------------------------
----------------------------------------------------------
Cuantas ventas va a ingresar en la fecha actual?
fecha = {fecha}
Respuesta: """
                    break
                else:
                    total_err += 1
                    continue

            # Input de numero de ventas

            while True:
                num_de_ventas = input(msg_ventas)
                veri, num_de_ventas = veri_num(num_de_ventas)
                if veri:
                    break
                else:
                    total_err += 1
                    continue

            while num_de_ventas > 0:

                # Input de ID de producto

                while True:
                    # Formato de id E4** ejemplo E402, etc...
                    prod_id = input('Ingrese el ID del producto (formato E4**, E422): ')
                    veri, prod_id = veri_idprod(prod_id)
                    if veri:
                        msg_id_prod = f"""
----------------------------------------------------------
----------------------------------------------------------  
Cuantas unidades se vendieron del producto {prod_id}?: """
                        msg_precio_prod = f"""
----------------------------------------------------------
----------------------------------------------------------
A que precio se vendio {prod_id}? (En dolares): $"""
                        break
                    else:
                        total_err += 1
                        continue

                # Input de cantidad de producto con la ID anterior

                while True:
                    cant_de_prod = input(msg_id_prod)
                    veri, cant_de_prod = veri_num(cant_de_prod)

                    if veri:
                        break
                    else:
                        total_err += 1
                        continue

                # Input del precio del procducto con la ID anterior

                while True:
                    precio_prod = float(input(msg_precio_prod))
                    veri, precio_prod = veri_num(precio_prod)

                    if veri:
                        break
                    else:
                        total_err += 1
                        continue
                num_de_ventas -= 1
                venta = f'venta,{sucursal},{dia_n},{dia},{mes},{anho},{prod_id},{cant_de_prod},{precio_prod},{total_err}\n'
                file.write(venta)
            break

def reg_produc():
    """Funcion de registro de produccion"""
    total_err = 0
    while True:
        while True:
            start = input('Quiere registrar la produccion?: Y/N').upper()
            veri = veri_start(start)
            if veri == 'Y':
                break
            elif veri == 'N':
                break
            else:
                total_err += 1
                continue
        if veri == 'N':
            return total_err
        while True:
            with open('datos_de_empresa.txt','a', encoding='utf-8') as file:
                while True:
                    num_de_prod = input()
                    veri, num_de_prod = veri_num(num_de_prod)
                    if veri:
                        break
                    else:
                        total_err += 1
                        continue
                while num_de_prod > 0:
                    while True:
                        # Formato de id E4** ejemplo E402, etc...
                        prod_id = input('Ingrese el ID del producto (formato E4**, E422): ')
                        veri, prod_id = veri_idprod(prod_id)
                        if veri:
                            msg_id_prod = f"""
        ----------------------------------------------------------
        ----------------------------------------------------------  
        Cuantas unidades se vendieron del producto {prod_id}?: """
                            msg_costo_prod = f"""
        ----------------------------------------------------------
        ----------------------------------------------------------
        Que costo de producion tuvo {prod_id}? (En dolares): $"""
                            break
                        else:
                            total_err += 1
                            continue
                    while True:
                        cant_de_prod = input(msg_id_prod)
                        veri, cant_de_prod = veri_num(cant_de_prod)
                        if veri:
                            break
                        else:
                            total_err =+1
                            continue
                    while True:
                        costo_prod = float(input(msg_costo_prod))
                        veri, costo_prod = veri_num(costo_prod)
                        if veri:
                            break
                        else:
                            total_err += 1
                            continue
                produccion = f'produccion,{prod_id},{cant_de_prod},{costo_prod}'
                file.write(produccion)

def reg_fina():
    """Funcion para registrar finanzas de la empresa"""
    total_err = 0
    while True:
        while True:
            start = input('Quiere registrar la transaccion?: Y/N').upper()
            veri = veri_start(start)
            if veri == 'Y':
                break
            elif veri == 'N':
                break
            else:
                continue
        if veri == 'N':
            return total_err
        with open('datos_de_empresa.txt','a', encoding='utf-8') as file:
            while True:

                # Input de numero de transacciones

                while True:
                    num_de_tran = input('Cuantas transacciones va a ingresar?: ')
                    veri, num_de_tran = veri_num(num_de_tran)
                    if veri:
                        break
                    else:
                        total_err += 1
                        continue
                while num_de_tran > 0:
                    while True:
                        iog = input('La transaccion es Ingreso o Gasto?: ')
                        veri, iog = veri_ingresos(iog)
                        if veri:
                            break
                        else:
                            total_err += 1
                            continue
                    while True:
                        monto = input(f'Introdusca su {iog}: ')
                        veri, monto = veri_monto(monto,iog)
                        if veri:
                            break
                        else:
                            total_err += 1
                            continue
                    num_de_tran -= 1
                    transaccion = f'transaccion, {monto}\n,{total_err}'
                    file.write(transaccion)
def estadisticas():
    """Funcion que calcula las estadisticas a mostrar"""
    meses_contadores = {mes: 0 for mes in MESES}
    monto_total_sucursales = {sucursal: 0 for sucursal in SUCURSALES}
    while True:
        with open('datos_de_empresa.txt','a', encoding='utf-8') as file:
            for lines in file:
                part = lines.split(',')
                tipo = part[0]
                if tipo == 'venta':
                    sucursal = part[1]
                    dia = part[2]
                    mes = part[4]
                    anho = part[5]
                    cant_prod = part[7]
                    precio_prod = part[8]
                    if anho == 2023:
                        cant_prod_total += cant_prod
                    meses_contadores[mes] += 1
                    monto_total_sucursales[sucursal] += (precio_prod * cant_prod)
                    if mes == 'Julio' or mes == 'Junio' or mes == 'Agosto':
                        jja_ventas += (precio_prod * cant_prod)
                elif tipo == 'produccion':
                    if dia == 'Sabado' or dia == 'Domingo':
                        pass
                    if mes == 'Julio' or mes == 'Junio' or mes == 'Agosto':
                        pass
            msg_estadistica = 'tu puta madre'
            print(msg_estadistica)

while True:
    while True:
        try:
            SELECT_MAIN = int(input(MSG_MENU_M))
            if SELECT_MAIN in [1,2,3]:
                break
            else:
                raise ValueError
        except ValueError(MSG_ERROR):
            continue

    # Ingresar Datos.

    if SELECT_MAIN == 1:
        while True:
            try:
                SELECT_W = int(input(MSG_MENU_W))
                if SELECT_W in [1,2,3,4]:
                    break
                else:
                    raise ValueError
            except ValueError(MSG_ERROR):
                continue

        # Registro de ventas.
        if SELECT_W == 1:
            reg_ventas()

        elif SELECT_W == 2:
            reg_produc()
        elif SELECT_W == 3:
            reg_fina()
    elif SELECT_MAIN == 2:
        estadisticas()

    elif SELECT_MAIN == 3:
        print('Saliendo de la app...')
        break

# 17. Indicar el mes que tuvo más ventas.
# 12. Cantidad (unidades) de productos vendidos para el 2023.
# 10. Cantidad de veces que un hubo un error de limpieza de datos (el texto estaba vacío
#     o venía con un error de ValueError que fue capturado.
#  8. Margen neto (ventas menos costos de producción) para los meses de junio, julio y
#     agosto.
#  6. Promedio de costos de producción en fin de semana (sábado y domingo).
#  3. Monto total de ventas por cada sucursal.
