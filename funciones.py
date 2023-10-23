from abc import ABC, abstractmethod


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
    
class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int, anio_inscripcion: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.legajo = legajo
        self.anio_inscripcion = anio_inscripcion

    def __str__(self):
        user_alumno = self.legajo + self.anio_inscripcion
        return user_alumno

    def validar_credenciales(self, email_ingresado: str, contrasenia_ingresada: str) -> bool:
        validado = False

        if self.email == email_ingresado and self.contrasenia == contrasenia_ingresada:
            validado = True

        return validado

    def matricular_en_curso(self, curso):
        validaciones_previas = True
        mensaje = False

        for i in self.mis_cursos:
            if i == curso:
                print("Ya estás matriculado en este curso.")
                validaciones_previas = False
                
                

        
        if validaciones_previas == True:
            self.mis_cursos.append(curso)
            if mensaje == True:
                print("Ha sido matriculado con éxito!")


    def cursos_matriculados(self):
        cursos_estudiante = []

        for x in self.mis_cursos:
            cursos_estudiante.append(x.nombre_curso)

        return cursos_estudiante     


class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso

    def __str__(self):
        user_profesor = self.titulo + self.anio_egreso
        return user_profesor

    def dictar_curso(self, curso):
        raise NotImplementedError() #Todavía no lo hice..

    

class Curso:
    def __init__(self, nombre_curso: str, contrasenia_matriculacion: str):
        self.nombre_curso = nombre_curso
        self.contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self):
        return self.nombre_curso
    
    def generar_contrasenia(self) -> str:
        raise NotImplementedError() #Todavía no lo hice.
        
        
#Datos

#profesores_registrados = []
#profe1 = Profesor("Alejandra", "Torres", "alejandratorres@gmail.com", "1234", "Profesorado en Informática")
#profe2 = Profesor("Martín", "Del Valle", "martindelvalle@gmail.com", "2345", "Profesorado en Inglés")
#profe3 = Profesor("Ayla", "Montes", "aylamontes@gmail.com", "3456", "Licenciatura en Computación")

#profesores_registrados.append(profe1)
#profesores_registrados.append(profe2)
#profesores_registrados.append(profe3)

alumnos_registrados = []
alumno1 = Estudiante("Marcelo", "Gómez", "marcelogomez@gmail.com", "1234", "10001", "2020")
alumno2 = Estudiante("Gascón", "Caruana", "gasconcaruana@gmail.com", "2345", "10002", "2022")
alumno3 = Estudiante("Melanie", "Ávila", "melanieavila@gmail.com", "3456", "10003", "2020")

alumnos_registrados.append(alumno1)
alumnos_registrados.append(alumno2)
alumnos_registrados.append(alumno3)

cursos_registrados = []
curso1 = Curso("InglesI", "1111")
curso2 = Curso("InglesII", "1112")
curso3 = Curso("Laboratorio I", "2222")
curso4 = Curso("Laboratorio II", "2223")
curso5 = Curso("Programación I", "3333")
curso6 = Curso("Programación II", "3334")

cursos_registrados.append(curso1)
cursos_registrados.append(curso2)
cursos_registrados.append(curso3)
cursos_registrados.append(curso4)
cursos_registrados.append(curso5)
cursos_registrados.append(curso6)

alumno1.matricular_en_curso(curso1)
alumno1.matricular_en_curso(curso2)
alumno2.matricular_en_curso(curso3)
alumno2.matricular_en_curso(curso4)
alumno3.matricular_en_curso(curso5)
alumno3.matricular_en_curso(curso6)

#Funciones
def menu_principal():
    print("\nIngrese una opción del menú")
    print("1. Ingresar cómo alumno")
    print("2. Ingresar cómo profesor")
    print("3. Ver cursos")
    print("4. Salir")
    op = int(input())
    while op < 1 or op > 4:
        print("Ingrese una opción válida. (1-4)")
        op = int(input())

    if op == 1:
        alumno_ingresado1 = validar_estudiante()
        
        if alumno_ingresado1 != None:
            submenu_alumno(alumno_ingresado1)
            return True
        else:
            pass
        return True
    if op == 4:
        return False


def validar_estudiante():
    acceso_eMail = False
    acceso_Password = False
    alumno_ingresado = None
    
    eMail = str(input("Ingrese su email: "))
    for alumno in alumnos_registrados:
        if alumno.email == eMail:
            acceso_eMail = True
            contrasenia1 = str(input("Ingrese su contraseña: "))
            if alumno.contrasenia == contrasenia1:
                acceso_Password = True
                alumno_ingresado = alumno
                break

    if acceso_eMail == False:
        print("¡El correo ingresado no está registrado en el sistema! Debe darse de alta en el alumnado.") 
        return None
    
    elif acceso_Password == False:
        print("La contraseña ingresada es incorrecta. Por favor, inténtelo de nuevo.")
        return None

    else:
        return alumno_ingresado


def submenu_alumno(alumno_ingresado1):

    continuar1 = True
    while continuar1 == True:
        print("\n1. Matricularse a un curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")
        rta_alumno = int(input())

        while rta_alumno < 1 or rta_alumno > 3:
            print("Ingrese una opción válida. (1-3)")
            rta_alumno = int(input())
    
        if rta_alumno == 1:
            matriculacion_estudiante(alumno_ingresado1)
            
        if rta_alumno == 2:
            ver_Cursos(alumno_ingresado1)
            
        if rta_alumno == 3:
            continuar1 = False




def matriculacion_estudiante(alumno_ingresado1):
    Matriculacion = False
    print("Cursos disponibles:")
    for i in range(len(cursos_registrados)):
        print(i+1, ". ", cursos_registrados[i].nombre_curso)
        indice = i
    
    eleccion_curso = int(input()) - 1
    while eleccion_curso < 0 or eleccion_curso > indice:
        print("Seleccione un curso válido.")
        eleccion_curso = int(input()) - 1

    password_curso = str(input("Ingrese contraseña de matriculación: "))

    for i in range(len(cursos_registrados)):
        if password_curso == cursos_registrados[i].contrasenia_matriculacion:
            Matriculacion = True

    if Matriculacion == True:
        alumno_ingresado1.matricular_en_curso(cursos_registrados[eleccion_curso])
    else:
        print("La contraseña es incorrecta, reinténtelo.")
        return None

def ver_Cursos(alumno):
    cursos = alumno.cursos_matriculados()
    contador = 1
    print("Mis cursos:")
    for x in cursos:
        print(str(contador) + ". " + x)
        contador = contador + 1

    numero_curso = int(input())
    while numero_curso < 1 or numero_curso > len(cursos):
        print("Número de curso inválido. Por favor, intenta de nuevo.")
        numero_curso = int(input())

    numero_curso = cursos[numero_curso-1]

    print("Archivos de", numero_curso, ":")
    print("tpi.pdf")
    print("practica1.pdf")
    return None