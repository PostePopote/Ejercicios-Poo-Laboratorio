"""Crear un programa donde:
Crear una clase: Alumno
crear sus atributos: Nombre, Apellido, Edad y Curso
crearle un método: programar (), que imprima  “ el alumno (nombre) está programando”

Crear el objeto Alumno instanciando con el método programar()

Los datos solicitados que el alumno completará, tiene que ser indistinto si es en mayuscula o minuscula"""

# Hago la clase Alumno con sus atributos correspondientes junto a su método
class Alumno:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso

    def programar(self):
        print(f"El alumno {self.nombre} esta programando")

# Utilizo inputs para pedir la informacion y uso el .title() para "estandarizar" lo que se ingrese
name = input("Ingrese el nombre: ").title()
lastN = input("Ingrese el apellido: ").title()
age = int(input("Ingrese la edad: "))
course = input("Ingrese el curso: ").title()

estudiante = Alumno(name, lastN, age, course)
estudiante.programar()