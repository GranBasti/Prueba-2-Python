while True:
    try:
        nombre_trabajador = input("Ingrese nombre del trabajador: ")
        if not nombre_trabajador.isspace() and 1 <= len(nombre_trabajador) <= 30:
            break
        else:
            print("Error: Ingresa un nombre real.")
    except ValueError:
        print("Error: Ingresa un valor válido.")

print(f"¡Excelente! Ingresaste el nombre {nombre_trabajador}.")