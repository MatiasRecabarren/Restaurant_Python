import numpy
import os
import time
import msvcrt
import Funciones_Restaurant as fn

arreglo_restaurant = numpy.zeros((3,3), int)

while True:
    os.system("cls")
    print ('''Menu Restaurant
    1.Ver Restaurant
    2.Reserva Mesa
    3.Carta
    4.Pagar
    5.Cancelar
    6.Salir
    ''')
    
    opcion = fn.validar_opcion()
           
    if opcion == 1:
        
        for x in range(3):
            print(f'Mesas Para {((x+1)*2)}:\t', end=" ")
            for y in range(3):
                print (arreglo_restaurant[x][y], end=" ")
            print ()
        print("")
        print ("                 1 2 3  ")
        print ("                 MESAS")

        print ('\nPresione una Tecla para Continuar....')
        msvcrt.getch()

    elif opcion == 2:
        rut = fn.validar_rut()
        nombre = fn.validar_nombre()
        correo = fn.validar_correo()
        
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        break