import Pyro4
import time

@Pyro4.expose
class ProcesadorDatos(object):
    def procesar_tarea_pesada(self, nombre_tarea, segundos):
        print(f"Iniciando {nombre_tarea}, tomara {segundos} segundos...")
        time.sleep(int(segundos))
        print(f"Termino {nombre_tarea}")
        return f"Resultado de {nombre_tarea} completado con exito"

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(ProcesadorDatos)
ns.register("practica.procesador", uri)

print("Servidor de procesamiento asincrono listo (Nivel 4)")
daemon.requestLoop()