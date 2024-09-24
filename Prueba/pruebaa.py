def main():
    while True:
        print("\nMenú de Conversión de Temperatura")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Salir")
        
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            if celsius < -273.15:
                print("Error: La temperatura no puede ser menor a -273.15°C.")
            else:
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}°C es {fahrenheit}°F")

        elif opcion == "2":
            fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
            if fahrenheit < -459.67:
                print("Error: La temperatura no puede ser menor a -459.67°F.")
            else:
                celsius = (fahrenheit - 32) * 5/9
                print(f"{fahrenheit}°F es {celsius}°C")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor elige una opción entre 1 y 3.")

main()