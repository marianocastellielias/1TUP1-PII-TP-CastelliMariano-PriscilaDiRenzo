from abc import ABC, abstractmethod
import random
import string



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

    
        

        
        
cursosProfe = []
class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso

    def __str__(self):
        user_profesor = self.titulo + self.anio_egreso
        return user_profesor

    def dictar_curso(self, curso):
        cursoDictadoProfe = input("Ingrese nombre del curso a dictar:\n")
        cursoDictadoProfe.append(cursos_registrados) #se agrega curso a dictar a la lista de cursos para todos
        cursoDictadoProfe.append(cursosProfe)
        print("Curso creado con exito!\n")
        print("Nombre curso:", cursoDictadoProfe, "\n")
        print("Contraseña: ") #contra generada automaticamente
        submenuProfesor()
    

    

class Curso:
    def __init__(self, nombre_curso: str, contrasenia_matriculacion: str):
        self.nombre_curso = nombre_curso
        self.contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self):
        return self.nombre_curso
    
    def generar_contrasenia(self) -> str:
            characters = string.ascii_letters + string.digits
            cod = ''.join(random.choice(characters) for i in range(4))
            return cod
        
        
#Datos de profesores 

profesores_registrados = []
profe1 = Profesor("Alejandra", "Torres", "alejandratorres@gmail.com", "1234", "Profesorado en Informática", "2002")
profe2 = Profesor("Martín", "Del Valle", "martindelvalle@gmail.com", "2345", "Profesorado en Inglés", "2010")
profe3 = Profesor("Ayla", "Montes", "aylamontes@gmail.com", "3456", "Licenciatura en Computación", "2019")

profesores_registrados.append(profe1)
profesores_registrados.append(profe2)
profesores_registrados.append(profe3)

def validar_profesor():
    accesoCorreoProfe = False
    accesoPassProfe = False
    profesor_ingresado = None
    correoProfesor = input("Ingrese su email:")
    for profesor in profesores_registrados:
        if profesor.email == correoProfesor:
            print("Usted está en la base de datos de profesores.")
            contraseña_profesor = input("Ingrese su contraseña")
            if profesor.contrasenia == contraseña_profesor:
                print("Ingreso exitoso!")
                accesoPassProfe = True
                profesor_ingresado = profesor
                break
    
        if not accesoCorreoProfe:
            print("¡El correo ingresado no está registrado en el sistema! Debe darse de alta en el alumnado.") 
            return None
        elif accesoPassProfe == False:
                print("La contraseña ingresada es incorrecta. Por favor, inténtelo de nuevo.")
                return None
        else:
            return profesor_ingresado

def submenuProfesor(dictar_curso):
    print("Ingrese opción:")
    print("1. Dictar curso")
    print("2. Ver curso")
    print("3. Volver al menú principal")
    opProfe = input()

    if opProfe == 1:
        dictar_curso()
    if opProfe == 2:
        for curso in cursosProfe:
            contador = contador + 1
            print("Seleccione curso:")
            print(f"Curso Nº. {contador}: {cursosProfe}\n")
            opElegirCurso = int(input())
            print(cursosProfe[opElegirCurso])


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
def menu_principal(dictar_curso):
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
<<<<<<< HEAD
    if op== 2:
        validar_profesor()
        submenuProfesor(dictar_curso)
=======
    
    if op == 3:
        cursos_registrados.sort(key=lambda curso: curso.nombre_curso)
        print("\n--------------------------\n")
        for x in range(len(cursos_registrados)):
            print("• Materia: ", cursos_registrados[x].nombre_curso, "\n• Carrera: Tecnicatura Universitaria en Programación\n")
            
        print("--------------------------")
        return True

>>>>>>> e2697393af71d67b64adc9fefcbdf234e6ea3e8b
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

    if not acceso_eMail:
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
        print("2. Desmatricularse a un curso")
        print("3. Ver curso")
        print("4. Volver al menú principal")
        rta_alumno = int(input())

        while rta_alumno < 1 or rta_alumno > 4:
            print("Ingrese una opción válida. (1-4)")
            rta_alumno = int(input())
    
        if rta_alumno == 1:
            matriculacion_estudiante(alumno_ingresado1)
        
        if rta_alumno == 2:
            desmatricularse(alumno_ingresado1)

        if rta_alumno == 3:
            ver_Cursos(alumno_ingresado1)
            
        if rta_alumno == 4:
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

def desmatricularse(alumno):

    contador1 = 1

    print("Seleccione curso del cual quiere desmatricularse:")
    for x in alumno.mis_cursos:
        print(str(contador1) + ". " + x.nombre_curso)
        contador1 = contador1 + 1
    
    numero_curso1 = int(input())
    while numero_curso1 < 1 or numero_curso1 > len(alumno.mis_cursos):
        print("Número de curso inválido. Por favor, intenta de nuevo.")
        numero_curso1 = int(input())
    
    del alumno.mis_cursos[numero_curso1-1]




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

