from abc import ABC, abstractmethod
from datetime import date
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
        mensaje = True

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
        self.mis_cursos.append(curso)

    
    def cursos_matriculados(self):
        cursos_profesor = []

        for x in self.mis_cursos:
            cursos_profesor.append(x.nombre_curso)

        return cursos_profesor
    
    def matricular_en_curso(self, curso):
        self.mis_cursos.append(curso)


        
    

class Curso:
    
    codigo = 0

    def __init__(self, nombre_curso: str, contrasenia_matriculacion: str):
        self.nombre_curso = nombre_curso
        self.contrasenia_matriculacion = contrasenia_matriculacion
        Curso.codigo = Curso.codigo + 1
        self.codigo = Curso.codigo
        self.mis_archivos = []
        
        
    def __str__(self):
        return self.nombre_curso
    
    def generar_contrasenia(self) -> str:
            characters = string.ascii_letters + string.digits
            cod = ''.join(random.choice(characters) for i in range(4))
            return cod
    
    def agregar_archivo(self, archivo_nuevo):
        self.mis_archivos.append(archivo_nuevo)
    


    
class Carrera:
    def __init__(self, __nombreCarrera: str, cant_anios: int):
        self.__nombreCarrera = __nombreCarrera
        self.__cant_anios = cant_anios 
        self.materias = []

    def __str__(self) -> str:
        return self.__nombreCarrera
    
    @property
    def get_cant_materias(self):
        return len(self.materias)

    def _registrar_materias(self, materia_a_registrar):
        self.materias.append(materia_a_registrar)


class Archivo:

    cantidad_archivos = 0

    def __init__(self, nombre_archivo:str, fecha: date, formato:str):
        self.nombre_archivo = nombre_archivo
        self.fecha = fecha
        self.formato = formato
        Archivo.cantidad_archivos = Archivo.cantidad_archivos + 1
        self.cantidad_de_archivos = Archivo.cantidad_archivos  
    
    def __str__(self):
        return f'Nombre del archivo: {self.nombre_archivo}, Fecha: {self.fecha}, Formato: {self.formato}'

alumnos_registrados = []
alumno1 = Estudiante("Marcelo", "Gómez", "marcelogomez@gmail.com", "1234", "10001", "2020")
alumno2 = Estudiante("Gascón", "Caruana", "gasconcaruana@gmail.com", "2345", "10002", "2022")
alumno3 = Estudiante("Melanie", "Ávila", "melanieavila@gmail.com", "3456", "10003", "2020")

alumnos_registrados.append(alumno1)
alumnos_registrados.append(alumno2)
alumnos_registrados.append(alumno3)


cursos_registrados = []
#No hay Cursos, ni archivos dados de alta al inicio. El Profe los va agregando.
# Materias de Programación
#curso1 = Curso("InglesI", "1111")
#curso2 = Curso("InglesII", "1112")
#curso3 = Curso("Laboratorio I", "2222")
#curso4 = Curso("Laboratorio II", "2223")
#curso5 = Curso("Programación I", "3333")
#curso6 = Curso("Programación II", "3334")

# Materias de Psicología
#curso7 = Curso("Sociología", "4444")
#curso8 = Curso("Historia", "4445")
#curso9 = Curso("Filosofía", "5555")

# Materias de Filosofía
#curso10 = Curso("Antropología", "5556")
#curso11 = Curso("Lógica", "6666")
#curso12 = Curso("Metafísica", "6667")

#Materias de Derecho
#curso13 = Curso("Legislación", "7777")
#curso14 = Curso("Derecho Penal", "7778")
#curso15 = Curso("Derecho Procesal", "8888")



#cursos_registrados.append(curso1)
#cursos_registrados.append(curso2)
#cursos_registrados.append(curso3)
#cursos_registrados.append(curso4)
#cursos_registrados.append(curso5)
#cursos_registrados.append(curso6)
#cursos_registrados.append(curso7)
#cursos_registrados.append(curso8)
#cursos_registrados.append(curso9)
#cursos_registrados.append(curso10)
#cursos_registrados.append(curso11)
#cursos_registrados.append(curso12)
#cursos_registrados.append(curso13)
#cursos_registrados.append(curso14)
#cursos_registrados.append(curso15)

# Datos de Carreras
#Psicología
carrera1 = Carrera("Psicología", 6)
carrera2 = Carrera("Tecnicatura en Programación", 2)
carrera3 = Carrera("Derecho", 6)
carrera4 = Carrera("Filosofía", 5)


#carrera2._registrar_materias(curso1)
#carrera2._registrar_materias(curso2)
#carrera2._registrar_materias(curso3)
#carrera2._registrar_materias(curso4)
#carrera2._registrar_materias(curso5)
#carrera2._registrar_materias(curso6)

#carrera1._registrar_materias(curso7)
#carrera1._registrar_materias(curso8)
#carrera1._registrar_materias(curso9)

#carrera4._registrar_materias(curso10)
#carrera4._registrar_materias(curso11)
#carrera4._registrar_materias(curso12)

#carrera3._registrar_materias(curso13)
#carrera3._registrar_materias(curso14)
#carrera3._registrar_materias(curso15)






#Datos de profesores 

profesores_registrados = []
profe1 = Profesor("Alejandra", "Torres", "alejandratorres@gmail.com", "1234", "Profesorado en Informática", "2002")
profe2 = Profesor("Martín", "Del Valle", "martindelvalle@gmail.com", "2345", "Profesorado en Inglés", "2010")
profe3 = Profesor("Ayla", "Montes", "aylamontes@gmail.com", "3456", "Licenciatura en Computación", "2019")

profesores_registrados.append(profe1)
profesores_registrados.append(profe2)
profesores_registrados.append(profe3)


   
def ingreso_carrera():
    print("Ingrese su carrera:")
    print("1-Tecnicatura en Programación")
    print("2-Psicología")
    print("3-Filosofía")
    print("4-Derecho")
    global op_carrera
    op_carrera = int(input())




def validar_profesor():
    accesoCorreoProfe = False
    accesoPassProfe = False
    profesor_ingresado = None
    correoProfesor = input("Ingrese su email:")
    for profesor in profesores_registrados:
        if profesor.email == correoProfesor:
            accesoCorreoProfe = True
            print("Usted está en la base de datos de profesores.")
            contrasenia_profesor = str(input("Ingrese su contraseña"))
            if profesor.contrasenia == contrasenia_profesor:
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
 
def submenuProfesor(profesor_ingresado2):
    continuar2 = True
    while continuar2 == True:
        print("Ingrese opción:")
        print("1. Dictar curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")
        opProfe = int(input())

        if opProfe == 1:
            dictar_curso(profesor_ingresado2)
        if opProfe == 2:
            ver_Cursos(profesor_ingresado2)

        #for curso in cursosProfe:
        #    contador = contador + 1
        #    print("Seleccione curso:")
        #    print(f"Curso Nº. {contador}: {cursosProfe}\n")
        #    opElegirCurso = int(input())
        #    print(cursosProfe[opElegirCurso])
        if opProfe == 3:
            menu_principal()
            continuar2 = False

def dictar_curso(profesoringresado3):
    
    curso_temporal = Curso("", "")
    cursoDictadoProfe = input("Ingrese nombre del curso a dictar:\n")
    contrasenia_generada = curso_temporal.generar_contrasenia()
    curso_creado = Curso(cursoDictadoProfe, contrasenia_generada) 
    cursos_registrados.append(curso_creado)
    profesoringresado3.dictar_curso(curso_creado)
    print("Curso creado con exito!\n")
    print("Nombre curso:", cursoDictadoProfe, "\n")
    print("Contraseña: ", contrasenia_generada)

    if op_carrera == 1:
        carrera2._registrar_materias(curso_creado)
    elif op_carrera == 2:
        carrera1._registrar_materias(curso_creado)
    elif op_carrera == 3:
        carrera4._registrar_materias(curso_creado)
    else:
        carrera3._registrar_materias(curso_creado)

    

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

    global identificador
    if op == 1:
        alumno_ingresado1 = validar_estudiante()
        
        
        identificador = "Alumno"

        if alumno_ingresado1 != None:
            submenu_alumno(alumno_ingresado1)
            return True
        else:
            pass
        return True
    if op== 2:
        profesor_ingresado1 = validar_profesor()

        
        identificador = "Profesor"
        
        if profesor_ingresado1 != None: #cambio
            submenuProfesor(profesor_ingresado1)
            return True
        else:
            pass
        return True

    if op == 3:

        if len(cursos_registrados) == 0:
            print("No se encontraron cursos registrados.")
            return True
        
        
        for x in cursos_registrados:
            print("• Materia:", x.nombre_curso)
            nombre_curso_guardado = x.nombre_curso
            for i in carrera1.materias:
                if i.nombre_curso == nombre_curso_guardado:
                    print("• Carrera:", carrera1.__str__(), "\n")
            for j in carrera2.materias:
                if j.nombre_curso == nombre_curso_guardado:
                    print("• Carrera:", carrera2.__str__(), "\n") 
            for z in carrera3.materias:
                if z.nombre_curso == nombre_curso_guardado:
                    print("• Carrera:", carrera3.__str__(), "\n")
            for h in carrera4.materias:
                if h.nombre_curso == nombre_curso_guardado:
                    print("• Carrera:", carrera4.__str__(), "\n")

            
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
    
    if len(cursos_registrados) == 0:
        print("No se encontraron cursos registrados.")
        return True
    
    Matriculacion = False
    print("Cursos disponibles:")

    if op_carrera == 2:
        for i in range(len(carrera1.materias)):
            print(i+1, ". ", carrera1.materias[i])
            indice = i
        eleccion_curso = int(input()) - 1
        pass
    elif op_carrera == 3:
        for i in range(len(carrera4.materias)):
            print(i+1, ". ", carrera4.materias[i])
            indice = i
        eleccion_curso = int(input()) - 1
        pass
    elif op_carrera == 4:
        for i in range(len(carrera3.materias)):
            print(i+1, ". ", carrera3.materias[i])
            indice = i
        eleccion_curso = int(input()) - 1
        pass
    elif op_carrera == 1:
        for i in range(len(carrera2.materias)):
            print(i+1, ". ", carrera2.materias[i])
            indice = i
        eleccion_curso = int(input()) - 1
        pass
        #for i in range(len(cursos_registrados)):
        #    print(i+1, ". ", cursos_registrados[i].nombre_curso)
        #    indice = i
    
    
    while eleccion_curso < 0 or eleccion_curso > indice:
        print("Seleccione un curso válido.")
        eleccion_curso = int(input()) - 1

    password_curso = str(input("Ingrese contraseña de matriculación: "))

    for i in range(len(cursos_registrados)):
        if password_curso == cursos_registrados[i].contrasenia_matriculacion:
            Matriculacion = True

    if Matriculacion == True:
        if op_carrera == 1:
            alumno_ingresado1.matricular_en_curso(carrera2.materias[eleccion_curso])
        elif op_carrera == 2:
            alumno_ingresado1.matricular_en_curso(carrera1.materias[eleccion_curso])
        elif op_carrera == 3:
            alumno_ingresado1.matricular_en_curso(carrera4.materias[eleccion_curso])
        elif op_carrera == 4:
            alumno_ingresado1.matricular_en_curso(carrera3.materias[eleccion_curso])
    else:
        print("La contraseña es incorrecta, reinténtelo.")
        return None

def desmatricularse(alumno):

    if len(cursos_registrados) == 0:
            print("No se encontraron cursos registrados.")
            return None

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
    if len(cursos) == 0:
        print("No se encontraron cursos registrados.")
        return None
    else:
        print("Mis cursos:")
        for x in cursos:
            print(str(contador) + ". " + x)
            contador = contador + 1

        numero_curso = int(input())
        while numero_curso < 1 or numero_curso > len(cursos):
            print("Número de curso inválido. Por favor, intenta de nuevo.")
            numero_curso = int(input())
    
        numero_curso = cursos[numero_curso-1]
        

        #curso_elegido = Curso(numero_curso, )
        if identificador == "Profesor":
            print("• Nombre:", numero_curso)

            for x in cursos_registrados:
                if x.nombre_curso == numero_curso:
                    print("• Contraseña", x.contrasenia_matriculacion)
                    print("• Código:", x.codigo)
                    print("• Cantidad de archivos", len(x.mis_archivos))

            archivo_adjunto = int(input("\n¿Desea agregar un archivo adjunto?\n1-Si\n2-No\n"))
            if archivo_adjunto == 1:
                nombre_archivo = str(input("Ingrese nombre del archivo"))
                formato_archivo = str(input("Ingrese formato del archivo (Ej: PDF, Zip, etc..)"))
                fecha_de_archivo = date.today()
                nuevo_archivo = Archivo(nombre_archivo, fecha_de_archivo, formato_archivo)

            
                for j in cursos_registrados:
                    if j.nombre_curso == numero_curso:
                        j.agregar_archivo(nuevo_archivo)
                        archivos_ordenados = sorted(j.mis_archivos)

                

        elif identificador == "Alumno":
            for x in cursos_registrados:
                if x.nombre_curso == numero_curso:
                    print("Archivos de:", numero_curso)
                    for archivo in x.mis_archivos:
                        print(archivo.__str__())



        
        return None

