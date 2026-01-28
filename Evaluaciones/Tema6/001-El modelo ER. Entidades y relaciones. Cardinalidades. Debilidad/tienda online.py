class Cliente:
    def __init__(self, id, nombre, apellidos, email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio


class Pedido:
    def __init__(self, id, fecha, cliente):
        self.id = id
        self.fecha = fecha
        self.cliente = cliente   # referencia a un objeto Cliente


class LineaPedido:
    def __init__(self, id, pedido, producto):
        self.id = id
        self.pedido = pedido     # referencia a un objeto Pedido
        self.producto = producto # referencia a un objeto Producto