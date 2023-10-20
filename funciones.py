from app import Profesor, Estudiante, Curso

#Datos
profesores_registrados = []
profe1 = Profesor("Alejandra", "Torres", "alejandratorres@gmail.com", "1234", "Profesorado en Informática")
profe2 = Profesor("Martín", "Del Valle", "martindelvalle@gmail.com", "2345", "Profesorado en Inglés")
profe3 = Profesor("Ayla", "Montes", "aylamontes@gmail.com", "3456", "Licenciatura en Computación")

profesores_registrados.append(profe1)
profesores_registrados.append(profe2)
profesores_registrados.append(profe3)

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

#Funciones
def menu_principal():
    print("¡Bienvenido! Ingrese una opción del menú")
    print("1. Ingresar cómo alumno")
    print("2. Ingresar cómo profesor")
    print("3. Ver cursos")
    print("4. Salir")
    op = int(input)
    while op < 1 or op > 4:
        print("Ingrese una opción válida. (1-4)")
        op = int(input())
    return op

def validar_estudiante():
    acceso_eMail = False
    acceso_Password = False
    acceso = False

    eMail = str(input("Ingrese su email: "))
    for alumno_ingresado in alumnos_registrados:
        if eMail == alumno_ingresado.email:
            acceso_eMail = True
        if acceso_eMail == True:
            password = str(input("Ingrese su contraseña: "))
            if password == alumno_ingresado.contrasenia:
                acceso_Password = True

    if acceso_eMail == False:
        print("¡El correo ingresado no está registrado en el sistema! Debe darse de alta en el alumnado.") 
        return None
    
    elif acceso_eMail == True and acceso_Password == True:
        return alumno_ingresado

alumno_ingresado1 = validar_estudiante()

def submenu_alumno():
    print("1. Matricularse a un curso")
    print("2. Ver curso")
    print("3. Volver al menú principal")
    rta_alumno = int(input())

    while rta_alumno < 1 or rta_alumno > 3:
        print("Ingrese una opción válida. (1-4)")
        rta_alumno = int(input())
    return rta_alumno


def matriculacion_estudiante():
    Matriculacion = False
    print("Cursos disponibles:")
    for x in cursos_registrados in range(0, cursos_registrados, 1):
        print(x+1, ". ", x.nombre_curso)
    
    eleccion_curso = int(input()) - 1
    password_curso = str(input("Ingrese contraseña de matriculación: "))

    for x in cursos_registrados in range(0, cursos_registrados, 1):
        if password_curso == x.contrasenia_matriculacion:
            Matriculacion = True

    if Matriculacion == True:
        alumno_ingresado1.matricular_en_curso(cursos_registrados[eleccion_curso])

