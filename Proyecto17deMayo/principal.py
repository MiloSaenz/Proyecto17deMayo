#Importar las clases
from clientes import cliente
from equipos import equipo

#Crear los objetos cliente y equipo
cliente1 = cliente()
equipo1 = equipo()
Opcion = ""

while (Opcion!=5):
    print("1. Agregar Cliente")
    print("2. Crear Equipo")
    print("3. Asignar Equipos a Cliente")
    print("4. Ver Listado de Equipos")
    print("5. Salir")
    print("-*50")
    print("Ingrese la opción que desea: ")
    Opcion = int(input())

    if Opcion == 1:
        # Pedir los datos del cliente
        apellidos = input("Ingrese apellidos del cliente: ")
        nombre = input("Ingrese nombre del cliente: ")
        telefono = input("Ingrese teléfono del cliente: ")

        # Agregar datos del cliente
        cliente1.AgregarCliente(apellidos,nombre,telefono)
    elif Opcion == 2:
        # Ingresar datos del equipo
        codigo = input("Ingrese el código del equipo: ")
        nomEquipo = input(" Ingrese nombre del equipo: ")
        precio = float(input("Ingrese precio del equipo: "))

        #Crear el equipo con sus características
        equipo1.AgregarEquipo(codigo,nomEquipo,precio)

    elif Opcion == 3:
        cliente1.AgregarEquipo(equipo1)

    elif Opcion == 4:
        cliente1.VerEquipos()

