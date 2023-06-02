"""Tarea opcional 2"""

LIST_NOMBRE = []
LIST_EDAD = []
LIST_SUELDO_BRUTO = []
LIST_SUELDO_LIQUIDO_BONO = []
LIST_INASISTENCIAS = []
LIST_NOBMRES_SUELDOS_ALTOS = []
LIST_CONT_SUELDOS_BONO = []

def calc_sueldos_liquidos(inasistencia, sueldo_bruto):
    "Calculador de sueldo liquido"""

    sueldo_liquido = sueldo_bruto * 0.8875

    if inasistencia == 0:

        sueldo_liquido_bono = sueldo_liquido + 150000
        LIST_SUELDO_LIQUIDO_BONO.append(sueldo_liquido_bono)
        return sueldo_liquido_bono

    else:
        LIST_SUELDO_LIQUIDO_BONO.append(sueldo_liquido)
        return sueldo_liquido

def lectura():
    """Lector de .txt"""

    with open('empleados.txt','r',encoding='utf-8') as archivo:
        for linea in archivo:
            part = linea.strip().split(';')
            sueldo_bruto = int(part[2])
            inasistencia = int(part[3])

            LIST_NOMBRE.append(part[0])
            LIST_EDAD.append(int(part[1]))
            LIST_SUELDO_BRUTO.append(sueldo_bruto)
            LIST_INASISTENCIAS.append(inasistencia)
            sueldo = calc_sueldos_liquidos(inasistencia, sueldo_bruto)
            if sueldo > 1400000:
                LIST_NOBMRES_SUELDOS_ALTOS.append(part[0])

def estadisticas():
    """Funcion para obtener estadisticas"""    ""

    # Promedio sueldo bruto/liquido
    prom_sueldo_bruto = round(sum(LIST_SUELDO_BRUTO) / len(LIST_EDAD))
    prom_sueldo_liquido = round(sum(LIST_SUELDO_LIQUIDO_BONO) / len(LIST_EDAD))

    # Nombre del empleado mas joven
    nombre_empleado_menor = LIST_NOMBRE[LIST_EDAD.index(min(LIST_EDAD))]

    # Mayor sueldo entre los sueldos liquidos mas bono

    sueldo_max_bono = max(LIST_SUELDO_LIQUIDO_BONO)

    msg = (f'El promedio de sueldo bruto es de: ${prom_sueldo_bruto}\n'
    f'El promedio de sueldo liquido es de: ${prom_sueldo_liquido}\n'
    f'Nombre del empleado mas joven: {nombre_empleado_menor}\n'
    f'Sueldo mayor entre los sueldos liquidos mas bono: ${sueldo_max_bono}\n'
    'Nombre de empleados con sueldo mayor a $1400000')
    print(msg)
    for empleados in LIST_NOBMRES_SUELDOS_ALTOS:
        print(empleados)


def main():
    """Funcion main"""

    lectura()
    estadisticas()

if __name__ == '__main__':
    main()
