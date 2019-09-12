class Publicacion:
    def __init__(self, codigo, precio, ubicacion, estado, cantidad, puntuacion):
        self.codigo = codigo
        self.precio = precio
        self.ubicacion = ubicacion
        self.estado = estado
        self.cantidad = cantidad
        self. puntuacion = puntuacion

def write(publicacion):
    print("------------------------")
    print("-Codigo de publicacion: ", publicacion.codigo)
    print("-Precio: ", publicacion.precio)
    print("-Ubicacion geografica: ", publicacion.ubicacion)
    print("-Estado: ", publicacion.estado)
    print("-Cantidad disponible: ", publicacion.cantidad)
    print("-Puntuacion del vendedor: ", publicacion.puntuacion)
