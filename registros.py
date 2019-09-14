class Publicacion:
    def __init__(self, codigo, precio, ubicacion, estado, cantidad, puntuacion):
        self.codigo = codigo
        self.precio = precio
        self.ubicacion = ubicacion
        self.estado = estado
        self.cantidad = cantidad
        self. puntuacion = puntuacion

def write(publicacion):
    ubicaciones = "Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén"\
        , "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", "Tucumán"
    estados = "Nuevo", "Usado"
    calificaciones = "Mala", "Regular", "Buena", "Muy buena", "Excelente"
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    renglon = ""
    renglon += "Codigo: "'{:<10}'.format(publicacion.codigo)
    renglon += "Precio: ""$" '{:<20}'.format(publicacion.precio)
    renglon += "Ubicacion: "'{:>10}'.format('{:21.20}'.format(ubicaciones[publicacion.ubicacion-1]))
    renglon += "Estado: "'{:<20}'.format(estados[publicacion.estado])
    renglon += "Cantidad: "'{:<20}'.format(publicacion.cantidad)
    renglon += "Puntuacion: "'{:<20}'.format(calificaciones[publicacion.puntuacion-1])
    print(renglon)

