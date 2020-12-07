def pedirMenuEntrevistas():

    print("Elegir una opcion ingresando un numero entero")
    opc = 0
    correcionOpc = True
    while(correcionOpc):
        try:
            num = int(input("Introducior opcion: "))
            correcionOpc = False
        except ValueError:
            print("Por favor ingresar un numero entero")
    return num

def leerArchivo():
    print("cargando archivo ....")

def calculo():
    print("calculo")

def generarArchivo():
    print("generando ....")

while True:
    print("1) Lectura de archivo csv ")
    print("2) Calculo de datos")
    print("3) Generacion de archivo Json")
    print("4) salir del programa")
    opcion = pedirMenuEntrevistas()
   #print(opcion)
    if opcion == 1:
       print("leer archivo csv")
       leerArchivo()
    elif opcion == 2:
       print("calculo de datos")
       calculo()
    elif opcion == 3:
       print("archivo JSON")
       generarArchivo()
    elif opcion == 4:
       break
    else:
       print("La opcion",opcion,"no existe")
