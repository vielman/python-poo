class Usuario:
    def __init__(self,nombre):
        # Metodo constructor
        self.nombre = nombre


    def saludar(self, saludo):
        print(saludo + " " + self.nombre)


cody = Empleado("Vielman")
cody.saludar("Hola! me llamo: ")

