"""Tarea opcional 3"""
LIST_CONT_APROBADOS = []

def veri_nota(tipo, num):
    """"Funcion verificadora de notas"""

    if tipo == 1:
        texto = 'Catedra'
    elif tipo == 2:
        texto = 'Taller'
    while True:
        try:
            nota = float(input(f'Ingrese su nota de {texto} numero {num}: '))
            if 1.0 <= nota <= 7.0:
                return nota
            else:
                raise ValueError
        except ValueError:
            print('Recuerde que las notas son desde 1.0 a 4.0!!!')
            continue

def calc_notas(nota_1, nota_2, nota_3, nota_4, nota_5, nota_6):
    """Calculador de notas"""

    nota_cat = (nota_1 * 0.25) + (nota_2 * 0.35) + (nota_3 * 0.4)
    nota_tall = (nota_4 * 0.25) + (nota_5 * 0.35) + (nota_6 * 0.4)
    return nota_cat, nota_tall

def mostrar_resultados(nota_cat, nota_tall):
    """Funcion para mostrar resultados"""

    nota_final = (nota_cat * 0.6) + (nota_tall * 0.4)

    if nota_cat >= 4.0 and nota_tall >= 4.0:
        print(f'Usted aprobo el ramo, con la nota de {nota_final}')
        LIST_CONT_APROBADOS.append(0)

    elif 3.4 <= nota_cat < 4 and nota_tall >= 4.0:
        print(f'Usted podra rendin el exmen, ya que aprobo el taller con: {nota_tall} y en catedra su nota se encuentra del rango 3.4 y 3.9 con: {nota_cat}')

    else:
        if nota_cat < 4.0:
            if nota_cat < nota_tall:
                print(f'Reprobo el ramo con una nota final de: {nota_cat}')
            else:
                print(f'Reprobo el ramo con una nota final de: {nota_tall}')
        else:
            print(f'Reprobo el ramo con una nota final de: {nota_tall}')




def main():
    """Funcion main"""

    for alumono in range(25):
        nombre = input('Ingrese su nombre: ')
        nota_catedra_1 =veri_nota(1, 1)
        nota_catedra_2 =veri_nota(1, 2)
        nota_catedra_3 =veri_nota(1, 3)
        nota_taller_1 =veri_nota(2, 1)
        nota_taller_2 =veri_nota(2, 2)
        nota_taller_3 =veri_nota(2, 3)

        nota_cat, nota_tall = calc_notas(nota_catedra_1, nota_catedra_2, nota_catedra_3, nota_taller_1, nota_taller_2, nota_taller_3)

        mostrar_resultados(nota_cat, nota_tall)
    print(f'El porcentaje de alumnos que no rindieron el examen es de: {(len(LIST_CONT_APROBADOS) / 25) * 100}')


if __name__ == '__main__':
    main()
