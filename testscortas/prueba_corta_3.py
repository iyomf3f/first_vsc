rango18_40 = 0
rango41_60 = 0
rango61_70 = 0
rango70_ = 0
Cuprum = 0
Provida = 0
Habitat = 0 
Modelo = 0 
Capital = 0
Cuprumr = 0
Providar = 0
Habitatr = 0 
Modelor = 0 
Capitalr = 0
montonosr = 0
edadrechazadas = 0
contador_solicitudes = 0
porcentaje_cuprum = 0
porcentaje_provida = 0
porcentaje_habitat = 0
porcentaje_modelo = 0
porcentaje_capital = 0
porcentaje_mayor = 0
nombre_afp_mayor = ''
maxsolicitudes = 0
maxsolicitudes_AFP = ''
si = 0
print('Bienvenido a la app del Gobierno\nLas AFPs disponibles son \'Cuprum, Provida, Habitat, Modelo, Capital.\'')
while True:
    
    #Inicio de la app

    print('Para salir ingrese \'salir\'')
    while True:
        try:
            start = input('Quiere ingresar datos? Y/N: ').lower()
            if start == 'y' or start == 'n':
                break
            else:
                raise ValueError
        except ValueError:
            print('Ingrese solo Y o N para responder!!!')
            continue
    if start == 'n':
        break
    elif start == 'y':
        si += 1

    #Input de nombre

    nombre = input('Ingrese su nombre completo (Ejemplo: Lionel Messi): ').title()

    # Verificador de rut

    while True:
        try:   
            rut = input('Ingrese su rut sin puntos ni guion (Si tiene k en su rut cambielo por un 0) Ejemplo: 218234560\nIngres su rut: ')
            verificador_rut = len(rut)
            rut = int(rut)
            if 8 <= verificador_rut <= 9:
                break
            else:
                raise ValueError
        except ValueError:
            print('Se equivoco al ingresar su Rut!')
            continue
        
    # Verificador de edad + contador de edad

    while True:
        try:
            edad = int(input('Ingrese su edad (Ejemplo: 29): '))
            if edad < 1:
                raise ValueError
            break
        except ValueError:
            print('Se equivoco al ingresar su edad!')
            continue

    if 17 < edad < 41:
        rango18_40 += 1
    elif 40 < edad < 61:
        rango41_60 += 1
    elif 60 < edad < 71:
        rango61_70 += 1
    elif 70 < edad:
        rango70_ += 1

    # Verificador de AFPs 

    while True:
        try:
            print('AFPs disponibles son \'Cuprum, Provida, Habitat, Modelo, Capital.\'')
            afp = input('Ingrese su AFP: ').title()
            if afp != 'Cuprum' and afp != 'Provida' and afp != 'Habitat' and afp != 'Modelo' and afp != 'Capital':
                raise ValueError
            else:
                break
        except ValueError:
            print('Se equivoco al ingresar su AFP!')
            continue

    #Contador de AFPs + mayor numero de solicitudes

    if afp == 'Cuprum':
        Cuprum += 1
        if Cuprum > maxsolicitudes:
            maxsolicitudes = Cuprum
            maxsolicitudes_AFP = 'Cuprum'
    elif afp == 'Provida':
        Provida += 1
        if Provida > maxsolicitudes:
            maxsolicitudes = Provida
            maxsolicitudes_AFP = 'Provida'
    elif afp == 'Habitat':
        Habitat += 1 
        if Habitat > maxsolicitudes:
            maxsolicitudes = Habitat
            maxsolicitudes_AFP = 'Habitat'
    elif afp == 'Modelo':
        Modelo += 1
        if Modelo > maxsolicitudes:
            maxsolicitudes = Modelo
            maxsolicitudes_AFP = 'Modelo'
    elif afp == 'Capital':
        Capital += 1
        if Capital > maxsolicitudes:
            maxsolicitudes = Capital
            maxsolicitudes_AFP = 'Capital'

    # Verificador de monto de AFP 

    while True:
        try:
            montoafp = int(input('Ingrese su monto disponible en su AFP (Ejemplo: $150000): $'))
            if montoafp < 0:
                raise ValueError
            break
        except ValueError:
            print('Se equivoco al ingresar su monto disponible!')
            continue

    #Contador de montos no validos

    if montoafp > 200000:
        montonosr += 1
        edadrechazadas += edad
        if afp == 'Cuprum':
            Cuprumr += 1
        if afp == 'Provida':
            Providar += 1
        if afp == 'Habitat':
            Habitatr += 1 
        if afp == 'Modelo':
            Modelor += 1
        if afp == 'Capital':
            Capitalr += 1 
            
    contador_solicitudes += 1
if si == 1:
    #AFP para la que se recibieron la mayor cantidad de solicitudes

    print(f'La AFP con mas solicitudes es {maxsolicitudes_AFP} con un total de {maxsolicitudes} solicitudes')

    #Rango etario para el que hay más solicitudes de bonos. Los rangos van de 18-40, 41-60, 61-70, sobre 70.

    if rango18_40 > rango41_60 and rango61_70 and rango70_:
        print('El rango etario con mas solicitudes es el de 18-40 anhos')
    elif rango41_60 > rango61_70 and rango70_:
        print('El rango etario con mas solicitudes es el de 41-60 anhos')
    elif rango61_70 > rango70_:
        print('El rango etario con mas solicitudes es el de 61-70 anhos')
    else:
        print('El rango etario con mas solicitudes es el de 70 o mas anhos')

    #AFP que tuvo el mayor porcentaje de solicitudes rechazadas. Asuma que una solicitud con un monto disponible sobre 200.000 se rechaza.

    if Cuprum > 0:
        porcentaje_cuprum = Cuprumr / Cuprum * 100
        if porcentaje_cuprum > porcentaje_mayor:
            porcentaje_mayor = porcentaje_cuprum
            nombre_afp_mayor == 'Cuprum'
    if Provida > 0:
        porcentaje_provida = Providar / Provida * 100
        if porcentaje_provida > porcentaje_mayor:
            porcentaje_mayor = porcentaje_provida  
            nombre_afp_mayor == 'Provida'
            
    if Habitat > 0:
        porcentaje_habitat = Habitatr / Habitat * 100
        if porcentaje_habitat > porcentaje_mayor:
            porcentaje_mayor = porcentaje_habitat
            nombre_afp_mayor == 'Habitat'
            
    if Modelo > 0:
        porcentaje_modelo = Modelor / Modelo * 100
        if porcentaje_modelo > porcentaje_mayor:
            porcentaje_mayor = porcentaje_modelo
            nombre_afp_mayor == 'Modelo'
            

    if Capital > 0:
        porcentaje_capital = Capitalr / Capital * 100
        if porcentaje_capital > porcentaje_mayor:
            porcentaje_mayor = porcentaje_capital
            nombre_afp_mayor == 'Modelo'
        
    print(f'El procenje menor es %{porcentaje_mayor} de la AFP {nombre_afp_mayor}')


    #Promedio de edad para las solicitudes rechazadas.

    if montonosr > 1:
        prom_edad_rechazadas = edadrechazadas / montonosr

        print(f"""El promedio de edades rechazadas es {prom_edad_rechazadas}.""")
    else:
        print(f"""No hay hubieron rechazos.""")
