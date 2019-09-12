from registro import *
import random

def menu():
    print("1- Nuevos por precio")
    print("2- Usados por calificación")
    print("3- Distribución geográfica")
    print("4- Total provincial")
    print("5- Precio promedio de usados")
    print("6- Compra ideal")
    print("7- Comprar")
    print("8- Salir")
    print("---------------------------")

def validarMayorQue(min):
    n = int(input("Ingrese la cantidad de publicaciones a buscar: "))
    while n <= min:
        print("Error!")
        n = int(input("Ingrese una cantidad valida: "))
    return n

def crearVector(n):
    vec = [None] * n
    for i in range(len(vec)):
        codigo = random.randint(1, 1000)
        precio = round(random.uniform(1, 100000), 2)
        ubicacion = random.randint(1, 23)
        estado = random.randint(0, 1)
        cantidad = random.randint(0, 1000)
        puntuacion = random.randint(1, 5)
        publicacion = Publicacion(codigo, precio, ubicacion, estado, cantidad, puntuacion)
        vec[i] = publicacion
    return vec


def validarOpcion(msj, min, max):
    opcion = int(input(msj))
    while opcion < min or opcion > max:
        print("Error!")
        opcion = int(input(msj))
    return opcion

def nuevosPorPrecio(vec):
    v = [ ]
    for i in range(len(vec)):
        if vec[i].estado == 0:
            v.append(vec[i])
    return v


def ordenarPorPrecio(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1, n):
            if vec[i].precio > vec[j].precio:
                vec[i], vec[j] = vec[j], vec[i]
    return vec

def ordenarPorCodigo(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1, n):
            if vec[i].codigo > vec[j].codigo:
                vec[i], vec[j] = vec[j], vec[i]

    return vec


def usadosPorCalificacion(vec):
    cont = [0] * 5
    for i in range(len(vec)):
        if vec[i].estado == 1:
            puntuacion = vec[i].puntuacion
            cont[puntuacion-1] += 1
    return cont


def precioPromedioUsados(vec):
    acu = 0
    cont = 0
    for i in range(len(vec)):
        if vec[i].estado == 1:
            acu += vec[i].precio
            cont += 1
    if cont != 0:
        prom = round((acu/cont), 2)
        return prom
    else:
        print("No hay publicaciones usadas")


def precioMayorPromedio(vec, precioprom):
    ban = False
    for i in range(len(vec)):
        if vec[i].estado == 1 and vec[i].precio > precioprom:
            ban = True
            print("---------------------------")
            write(vec[i])
    if ban == False:
        print("No hay publicaciones que superen el precio promedio de usados")


def menorPrecio(vec):
    menor = None
    for i in range(len(vec)):
        if menor == None and vec[i].estado == 0 and vec[i].puntuacion != 1:
            menor = vec[i].precio
            if vec[i].precio < menor and vec[i].estado == 0 and vec[i].puntuacion != 1:
                menor = vec[i].precio
    return  menor


def buscarPorId(vec, cod):
    ban = False
    for i in range(len(vec)):
        if vec[i].codigo == cod:
            ban = True
            print("Stock del producto: {0}".format(vec[i].cantidad))
            cant = int(input("Ingrese la cantidad que desea comprar: "))
            while vec[i].cantidad < cant:
                print("No hay stock suficiente")
                conf = int(input("¿Desea volver al menu o probar con otro producto?(0=volver al menu, 1=otro producto)"))
                if conf == 1:
                    cod = int(input("Ingrese el codigo de la publicacion a buscar: "))
                    cant = 0
                    buscarPorId(vec, cod)
                    break
                elif conf == 0:
                    return
            else:
                confirmacion = int(input("¿Desea realizar la compra?(0=si, 1=no)"))
                if confirmacion == 0:
                    print("Gracias por su compra")
                    vec[i].cantidad -= cant
                    print("Stock actualizado del producto: {0} ".format(vec[i].cantidad))
                else:
                    return

    if ban == False:
        print("Publicacion no encontrada")


def crearMatriz(vec):
    mat = [[0] * 5 for i in range(23)]
    for i in range(len(vec)):
        fil = vec[i].ubicacion -1
        col = vec[i].puntuacion -1
        mat[fil][col] += 1
    return mat

def ubicaciones(num):
    ubicaciones = "Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén"\
        , "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", "Tucumán"
    estados = "Nuevo", "Usado"
    return ubicaciones[num]

def puntuacion(num):
    calificaciones = "Mala", "Regular", "Buena", "Muy buena", "Excelente"
    return calificaciones[num]

def mostrarMatrizLista(mat):
    ban = False
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                if ban == False:
                    print(ubicaciones(i))
                ban = True
                print("\t", puntuacion(j), ":", end=" ")
                print(mat[i][j])
        ban = False
        print()


def mostrarMatriz(mat):
    '''
    for f in range(len(mat[0])):
        print(puntuacion(f), end=" \t ")
    print( )
    print("---------------------------")
    '''
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end= " \t ",)
        print(ubicaciones(i))


def test():
    n = validarMayorQue(0)
    vec = crearVector(n)
    sorted = ordenarPorCodigo(vec)
    for i in range(len(sorted)):
        write(sorted[i])
    opcion = 0
    while opcion != 8:
        print("---------------------------")
        menu()
        opcion = validarOpcion("Ingrese una opcion", 1, 8)
        if opcion == 1:
            v = nuevosPorPrecio(vec)
            sorted = ordenarPorPrecio(v)
            for i in range(len(sorted)):
                write(sorted[i])
        if opcion == 2:
            cont = usadosPorCalificacion(vec)
            for i in range(len(cont)):
                print("Cantidad de publicaciones usadas con puntuacion {0}: ".format(puntuacion(i)), cont[i])

        if opcion == 3:
            mat = crearMatriz(vec)
            forma = int(input("¿Como desea mostrar la matriz?(0: matriz, 1: lista): "))
            if forma == 1:
                mostrarMatrizLista(mat)
            elif forma == 0:
                print("---------------------------")
                mostrarMatriz(mat)

        if opcion == 5:
            precioprom = precioPromedioUsados(vec)
            print("Precio promedio de productos usados: ", precioprom)
            precioMayorPromedio(vec, precioprom)

        if opcion == 6:
            menor = menorPrecio(vec)
            print("El menor precio para un producto de estado nuevo, omitiendo a los vendedores con calificacion mala es de {0}: ".format(menor))

        if opcion == 7:
            cod = int(input("Ingrese el codigo de la publicacion a buscar: "))
            buscarPorId(vec, cod)


if __name__ == "__main__":
    test()

