'''/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *       _|
 *     _|
 *   _|
 * _|
 *
 */'''

print('CREADOR DE ESCALERAS'.center(40,'*'))


def escalera():
    while True:
        choice = (input('Desea crear una escalera (y/n): '))

        if choice.lower() != 'y':
            print('\n''<<< Terminado >>>''\n')
            break
        elif choice.lower() == 'y':
            option = (input('Seleccione el numero de escalones que desea: '))

            option = int(option)

            if option == 0:
                print('\n' '__' '\n')

        
                
            if option > 0:
                valor1 = option*2
                for x in range(option):
                    escalon = '_|'
                    espacio = ' ' 
                    valor1 -= 2
                    print(espacio*valor1 + escalon)


            if option < 0: 
                option = int(option * -1)
                valor = 0
                
                for x in range(option):
                    escalon = '|_'
                    espacio = ' ' 
                    valor += 2
                    print(espacio*valor + escalon)


                


escalera()