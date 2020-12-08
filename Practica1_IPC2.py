
import json
cont = ""
calc = ""

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
    ruta = input("Ingresar ruta del archivo: ")
    arch = open(ruta, 'r')
    print("cargando archivo "+ruta)
    contenido = arch.read()
    print(contenido)
    arch.close()
    return contenido


def calculo(leer):
    print(leer)

def generarArchivo():
    print("generando ....")

def menuPrincipal():

    while True:
        print("1) Lectura de archivo csv ")
        print("2) Calculo de datos")
        print("3) Generacion de archivo Json")
        print("4) salir del programa")
        opcion = pedirMenuEntrevistas()
       #print(opcion)
        if opcion == 1:
           cont= leerArchivo()
        elif opcion == 2:
           print("calculo de datos")
           calculo(cont)
        elif opcion == 3:
           print("archivo JSON")
           generarArchivo()
        elif opcion == 4:
           break
        else:
           print("La opcion",opcion,"no existe")

if __name__ == '__main__':
    menuPrincipal()