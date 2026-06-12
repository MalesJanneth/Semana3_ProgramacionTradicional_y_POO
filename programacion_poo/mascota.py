#Clase mascota
class Mascota:
    #Constructor
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    #Metodo para mostrar información
    def mostrar_informacion(self):
        print("Nombre: ", self.nombre)
        print("Especie: ", self.especie)
        print("Edad: ", self.edad)
    #Método para realizar una accion
    def hacer_sonido(self):
        print("La mascota esta haciendo un sonido")