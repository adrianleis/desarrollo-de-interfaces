# calculadora.py

from operaciones import suma, resta, multiplicacion, division

while True:
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Error: Debes introducir un número válido.")
        continue

    print("Operaciones disponibles:")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")

    operacion = input("Selecciona la operación (1/2/3/4): ")

    if operacion == "1":
        resultado = suma(num1, num2)
    elif operacion == "2":
        resultado = resta(num1, num2)
    elif operacion == "3":
        resultado = multiplicacion(num1, num2)
    elif operacion == "4":
        resultado = division(num1, num2)
    else:
        print("Operación no válida.")
        continue

    print(f"El resultado es: {resultado}")

    seguir = input("¿Quieres realizar otra operación? (s/n): ").lower()
    if seguir != "s":
        print("¡Hasta luego!")