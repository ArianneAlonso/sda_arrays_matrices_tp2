alumnos = []

def guardar_alumno():
    nombre = input("nombre del alumno: ")
    edad = input("edad del alumno: ")
    nota = input("nota del alumno: ")

    if not nombre or not edad or not nota:
        print("faltan datos, por favor complete todos los campos.")
        return

    # subarreglo [nombre, edad, nota]
    alumnos.append([nombre, int(edad), float(nota)])

    print("Alumno guardado correctamente.")

def terminar_registro():
    if len(alumnos) == 0:
        print("No hay datos registrados.")
        return

    # lista de como fueron ingresando
    print("Lista de Alumnos Registrados:")
    for alumno in alumnos:
        print("Nombre: ", alumno[0], "Edad: ", alumno[1], "Nota: ", alumno[2])

    # lista por nota (de mayor a menor)
    alumnos.sort(key=lambda x: x[2], reverse=True)
    print("Lista ordenada por nota (de mayor a menor):")
    for alumno in alumnos:
        print("Nombre: ", alumno[0], "Edad: ", alumno[1], "Nota: ", alumno[2])

def main():
    # se guarda un alumno si o si
    guardar_alumno()

    while True:
        print("¿Deseas seguir guardando más alumnos o terminar el programa?")
        print("1. Guardar otro alumno")
        print("2. Terminar registro y mostrar resultados")
        print("3. Salir")

        opcion = input("Seleccione una opción (1, 2 o 3): ")

        if opcion == "1":
            guardar_alumno()
        elif opcion == "2":
            terminar_registro()
            break
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
            
if __name__ == "__main__":
    main()
    
