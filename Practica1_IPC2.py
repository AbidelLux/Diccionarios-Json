
import json
cont = ""
dic1 = {}

def pedirMenuEntrevistas():

    print("Elegir una opcion ingresando un numero entero")
    opc = 0
    correcionOpc = True
    while(correcionOpc):
        try:
            num = int(input("Introducir opcion: "))
            correcionOpc = False
        except ValueError:
            print("Por favor ingresar un numero entero")
    return num


def leerArchivo():
    ruta = input("Ingresar ruta del archivo: ")
    arch = open(ruta, 'r')
    print("cargando archivo "+ruta)
    contenido = arch.read()

    arch.close()
    return contenido


def calculo(leer):
    posicionID = 0
    posicionPuesto=0
    posicionEdad =0
    posicionSalario =0
    separador = "\n"
    lista = leer.split(separador)
    contador =0
    for i in lista[0].split(","):
        contador = contador+1
        if i == "ID":
            posicionID =contador-1
            #(posicionID)
        elif i == "EDAD":
            posicionEdad = contador-1
        elif i == "PUESTO":
            posicionPuesto = contador-1
        elif i == "SALARIO":
            posicionSalario = contador-1
        elif i == "NOMBRE":
            posicionNombre = contador-1
        elif i == "APELLIDO":
            posicionApellido = contador-1
        #print(i)
    contador2 =0
    for j in lista:
        #print(dic1)
        lista2 = lista[contador2].split(",")
        #print(lista2)
        if contador2 ==1:
            dic1 = {int(lista2[posicionID]):{"NOMBRE":lista2[posicionNombre],"APELLIDO":lista2[posicionApellido],"EDAD":int(lista2[posicionEdad]),"PUESTO":lista2[posicionPuesto],"SALARIO":int(lista2[posicionSalario])}}
            #print(lista2[posicionEdad])
        elif contador2 >1:

            dic1[int(lista2[posicionID])] = {"NOMBRE":lista2[posicionNombre],"APELLIDO":lista2[posicionApellido],"EDAD":int(lista2[posicionEdad]),"PUESTO":lista2[posicionPuesto],"SALARIO":int(lista2[posicionSalario])}
            #print(dic1)

        contador2=contador2+1

        #if j == lista[0]:
        #   contador2 = contador2 -1
        #   print("")
    #print(dic1)

    #print(leer)

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