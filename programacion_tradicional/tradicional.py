#Función para registrar los datos de la mascota
def registrar_mascota():
    nombre = input ("Ingrese el nombre de la mascota: ")
    especie = input ("Ingrese la especie de la mascota: ")
    edad = input ("Ingrese la edad de la mascota: ")
    return nombre, especie, edad
#Función para mostrar la información registrada
def mostrar_mascota(nombre, especie, edad):
    print("Información de la mascota")
    print("Nombre:", nombre)
    print("Especie:", especie)
    print("Edad:", edad)

nombre, especie, edad = registrar_mascota()

mostrar_mascota(nombre, especie, edad)