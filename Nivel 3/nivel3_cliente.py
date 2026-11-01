import Pyro4

try:
    banco = Pyro4.Proxy("PYRONAME:practica.banco")
except Exception as e:
    print(f"Error de conexion: {e}")
    exit()

while True:
    print("\n--- BANCO DISTRIBUIDO ---")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Elige una opcion: ").strip()

    if opcion == '4':
        print("Saliendo del banco")
        banco._pyroRelease() # Libera el proxy para cerrar la sesion
        break

    try:
        if opcion == '1':
            print(f"Saldo actual: ${banco.consultar_saldo()}")
        elif opcion == '2':
            monto = input("Monto a depositar: ")
            nuevo_saldo = banco.depositar(monto)
            print(f"Deposito exitoso. Nuevo saldo: ${nuevo_saldo}")
        elif opcion == '3':
            monto = input("Monto a retirar: ")
            nuevo_saldo = banco.retirar(monto)
            print(f"Retiro exitoso. Nuevo saldo: ${nuevo_saldo}")
        else:
            print("Opcion invalida")
    except Exception as e:
        print(f"Error en la operacion: {e}")