import Pyro4

try:
    mensajeria = Pyro4.Proxy("PYRONAME:practica.mensajeria")
except Exception as e:
    print(f"Error de conexion: {e}")
    exit()

remitente = input("Ingresa tu nombre: ").strip()

while True:
    mensaje = input("Escribe un mensaje (o 'salir' para terminar): ").strip()
    if mensaje.lower() == 'salir':
        break

    respuesta = mensajeria.enviar_mensaje(remitente, mensaje)
    print(f"Servidor respondio: {respuesta}")