from app import Profesor

#Datos
profesores_registrados = []
profe1 = Profesor("Alejandra", "Torres", "alejandratorres@gmail.com", "1234", "Profesorado en Informática")
profe2 = Profesor("Martín", "Del Valle", "martindelvalle@gmail.com", "2345", "Profesorado en Inglés")
profe3 = Profesor("Ayla", "Montes", "aylamontes@gmail.com", "3456", "Licenciatura en Computación")

profesores_registrados.append(profe1)
profesores_registrados.append(profe2)
profesores_registrados.append(profe3)

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

