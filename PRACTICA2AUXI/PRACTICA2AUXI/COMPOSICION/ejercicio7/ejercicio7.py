# 7. Crea un POO para una universidad y sus estudiantes. La universidad contiene
# estudiantes, pero los estudiantes pueden existir independientemente de la
# universidad.
# Estudiante< nombre, carrera, semestre>
# Métodos: mostrar_info() (muestra el nombre, carrera y semestre del estudiante)
# Universidad<nombre, estudiantes (lista de objetos de tipo Estudiante)>
# Métodos: agregar_estudiante(estudiante), mostrar_universidad() (muestra el
# nombre de la universidad y la información de todos los estudiantes)
# a) Implementa las clases con sus constructores, getters y setters.
# b) Crea una universidad y agrega varios estudiantes.
# c) Muestra la información de la universidad y sus estudiantes
class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        self.nombre, self.carrera, self.semestre = nombre, carrera, semestre
    def mostrar_info(self):
        print(f"{self.nombre}, Carrera: {self.carrera}, Semestre: {self.semestre}")

class Universidad:
    def __init__(self, nombre):
        self.nombre, self.estudiantes = nombre, []
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    def mostrar_universidad(self):
        print(f"Universidad: {self.nombre}")
        for e in self.estudiantes: 
            e.mostrar_info()

uni = Universidad("UMSA")
uni.agregar_estudiante(Estudiante("Ana", "Informática", 4))
uni.agregar_estudiante(Estudiante("Luis", "Sistemas", 2))
uni.mostrar_universidad()
