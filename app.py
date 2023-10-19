from abc import ABC, abstractmethod
from funciones import profesores_registrados


class Usuario (ABC):
    
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasenia = contrasenia
        self.mis_cursos = [] 

    @abstractmethod
    def __str__(self):
        user = self.nombre + self.apellido + self.email
        return user
    
    @abstractmethod
    def validar_credenciales(self, email_ingresado: str, contrasenia_ingresada: str) -> bool:
        validado = False

        if self.email == email_ingresado and self.contrasenia == contrasenia_ingresada:
            validado = True

        return validado


class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso

    def __str__(self):
        user_profesor = self.titulo + self.anio_egreso
        return user_profesor

    def dictar_curso(self, curso):
        raise NotImplementedError() #Todavía no lo hice.

class Curso:
    def __init__(self, nombre_curso: str, contrasenia_matriculacion: str):
        self.nombre_curso = nombre_curso
        self.contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self):
        return self.nombre_curso
    
    def generar_contrasenia(self) -> str:
        raise NotImplementedError() #Todavía no lo hice.
        
        