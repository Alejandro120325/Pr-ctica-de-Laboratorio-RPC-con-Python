import Pyro4
import time

try:
    procesador = Pyro4.Proxy("PYRONAME:practica.procesador")
except Exception as e:
    print(f"Error de conexion: {e}")
    exit()

print("Enviando tarea pesada al servidor...")

# En versiones modernas de Pyro4 se usa Pyro4.Future apuntando directo al metodo
procesar_async = Pyro4.Future(procesador.procesar_tarea_pesada)
future_result = procesar_async("Analisis_de_Datos", 10)

print("La tarea se esta procesando en el servidor.")
print("Mientras tanto, el cliente puede hacer otras cosas...")

contador = 1
while not future_result.ready:
    print(f"Cliente trabajando en otra cosa... (segundo {contador})")
    time.sleep(1)
    contador += 1

print("\nLa tarea del servidor ya termino")
print("Resultado:", future_result.value)