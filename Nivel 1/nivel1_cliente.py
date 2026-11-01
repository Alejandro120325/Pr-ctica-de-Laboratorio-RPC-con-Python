import Pyro4

def obtener_numero(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            return float(entrada)
        except ValueError:
            print(" Error, ingrese un numero valido (ej: 10 o 5.5). Intente de nuevo.\n")

# Conexión directa pidiendo la URI generada por el servidor
uri_servidor = input("Pega aquí la URI que generó el servidor: ").strip()

try:
    calc = Pyro4.Proxy(uri_servidor)
except Exception as e:
    print(f"Error al conectar con la URI: {e}")
    exit()

while True:
    print("\n***** CALCULADORA *****")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == '5':
        print("Saliendo del programa")
        break

    if opcion not in ['1', '2', '3', '4']:
        print(" Opcion no valida. Elija un numero entre 1 y 5.")
        continue

    num1 = obtener_numero("Ingrese el primer numero: ")
    num2 = obtener_numero("Ingrese el segundo numero: ")

    try:
        if opcion == '1':
            resultado = calc.sumar(num1, num2)
            print(f"\nResultado: {num1} + {num2} = {resultado}")
        elif opcion == '2':
            resultado = calc.restar(num1, num2)
            print(f"\nResultado: {num1} - {num2} = {resultado}")
        elif opcion == '3':
            resultado = calc.multiplicar(num1, num2)
            print(f"\nResultado: {num1} * {num2} = {resultado}")
        elif opcion == '4':
            resultado = calc.dividir(num1, num2)
            print(f"\nResultado: {num1} / {num2} = {resultado}")
    except Exception as error:
        print(f"\n Error en el servidor: {error}")