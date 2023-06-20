def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción (1 a 6): "))
            if opcion in(1,2,3,4,5,6):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su Rut para reservar una mesa: "))
            if len(str(rut))>=7 and len(str(rut))<=8:
                return rut
            else:
                print("ERROR! el rut debe tener entre 7 y 8 dígitos!")
        except:
            print("ERROR! debe ingresar un número entero!")
        
def validar_correo():
    while True:
            correo = input("Ingrese correo para al reserva: ")
            if "@" in correo:
                return correo
            else:
                print("ERROR! correo incorrecto!")

def validar_nombre():
    while True:
            nombre_usuario = input("Ingrese nombre para la reserva: ")
            if len(nombre_usuario.strip()) >= 3:
                return nombre_usuario
            else:
                print("ERROR! el nombre debe tener al menos 3 caracteres!")

def validar_numero(p_texto):
    while True:
        try:
            numero = int(input(f"Ingrese {p_texto} del producto: "))
            if numero > 0:
                return numero
            else:
                print(f"ERROR! EL {p_texto} DEBE SER POSITIVO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def calcular_iva():
    precio = validar_numero("precio")
    iva = round(precio*19/100)
    print("El valor del iva del producto con precio",precio,"es",iva)