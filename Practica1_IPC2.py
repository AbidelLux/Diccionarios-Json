import json
cont = ""
dic1 = {}
dicCalculo = {}
dicAux ={}

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
    posicionID = 0
    posicionPuesto=0
    posicionEdad =0
    posicionSalario =0
    separador = "\n"
    lista = contenido.split(separador)
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

    for c in dic1.keys():
        print(str(c)+",",dic1[c]['NOMBRE']+",",dic1[c]['APELLIDO']+",",str(dic1[c]['EDAD'])+",",dic1[c]['PUESTO']+",",str(dic1[c]['SALARIO']))

        #if j == lista[0]:
        #   contador2 = contador2 -1
        #   print("")
    #print(dic1)
    return dic1


def calculo(dicEntrante):
    if dicEntrante == {}:
        print("Por Favor ingresar un archivo en la opcion 1")
    else:
        #Graba en dicAux los puestos existentes
        for i in dicEntrante.keys():
            dicAux[dicEntrante[i]['PUESTO']]={'Candidatos':0,"Edad Promedio":0,"Prentencion Salarial":0}
        #Calculo de suma de todas las edades, suma de todos los salario, conteo de candidatos
        for a in dicAux.keys():
            for b in dicEntrante.keys():
                if dicEntrante[b]['PUESTO'] == a:
                    dicAux[a]['Candidatos'] = dicAux[a]['Candidatos'] +1
                    dicAux[a]['Edad Promedio'] = dicEntrante[b]['EDAD'] + dicAux[a]['Edad Promedio']
                    dicAux[a]['Prentencion Salarial'] = dicEntrante[b]['SALARIO'] + dicAux[a]['Prentencion Salarial']
        #Calcular promedio de Edad y de salarios
        for c in dicAux.keys():
                dicAux[c]['Edad Promedio'] = dicAux[c]['Edad Promedio'] / dicAux[c]['Candidatos']
                dicAux[c]['Prentencion Salarial'] = dicAux[c]['Prentencion Salarial'] / dicAux[c]['Candidatos']


        print(dicAux)
    return dicAux

def generarArchivo(archivo):
    print("generando ....")
    with open('archivo.json','w') as file:
        json.dump(archivo,file,indent=3)

def menuPrincipal():
    cont={}
    final = {}
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
           final=calculo(cont)
        elif opcion == 3:
           print("archivo JSON")
           generarArchivo(final)

        elif opcion == 4:
           break
        else:
           print("La opcion",opcion,"no existe")

if __name__ == '__main__':
    menuPrincipal()