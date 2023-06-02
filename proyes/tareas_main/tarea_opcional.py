"""Ayudantia 31/05 Paralelo """

OPCIONES = [1,2,3,4]

OPCIONES_UTILIZADAS = []

MSG_MENU = """
1.-Trivia Fácil (1 vida)
2.-Trivia Media (2 vidas)
3.-Trivia Difícil (3 vidas)
4.-Salir

Respuesta: """


def menu():
    """Funcion del menu"""

    while True:
        try:
            select = int(input(MSG_MENU))

            if select in OPCIONES:
                return select
            if select in OPCIONES_UTILIZADAS:
                print('Esta pregunta ya la respondio correctamente!!!')
                continue
            raise ValueError

        except ValueError:
            print('Opcion no valida!')
            continue



def trivia(select):
    """Funcion para las trivias"""

    respuestas = [1,2,3]

    if select == 1:
        pregunta = '\n¿Cuál es el nombre del Kong que genera las trivias?\n\n1.- Swanky \n2.- Kranky \n3.- Un gusano\nRespuesta: '

    elif select == 2:
        pregunta = '\n¿Qué es el primer enemigo que ves en el juego?\n\n1.- Un cocodrilo \n2.- Una rata \n3.-Donkey\nRespuesta: '

    elif select == 3:
        pregunta = '\n¿Cómo se llama el ultimo nivel del juego?\n\n1.- King K Rool Time \n2.- K Rool Fight \n3.- K.Rool Duel \nRespuesta: '

    while True:
        try:
            respuesta = int(input(pregunta))
            if respuesta in respuestas:
                if respuesta == select:
                    OPCIONES.remove(select)
                    OPCIONES_UTILIZADAS.append(select)

                    print('\nRESPUESTA CORRECTA!!!\n')
                    vidas_extras = select
                    return vidas_extras

                print('\ntonto\n')
                vidas_extras = 0
                return vidas_extras
            raise ValueError
        except ValueError:
            print('\nSOLO RESPONDA CON 1,2,3!!!\n')
            continue
def main():
    """Funcion principal"""
    vidas = 1

    while True:
        select = menu()

        if select == 4:
            if vidas == 7:
                print('\n\nFelicidades gano el juego con 7 vidas!!!')
            print('\n \nSaliendo del juego...')
            return

        vidas_extras = trivia(select)
        vidas += vidas_extras

if __name__ == '__main__':
    main()
