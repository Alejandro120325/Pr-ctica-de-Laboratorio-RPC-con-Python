import Pyro4

@Pyro4.expose
class ServicioMensajes(object):
    def enviar_mensaje(self, remitente, mensaje):
        print(f"[{remitente}] dice: {mensaje}")
        return "Mensaje recibido por el servidor"

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(ServicioMensajes)
ns.register("practica.mensajeria", uri)

print("Servidor de mensajeria listo (Nivel 2)")
daemon.requestLoop()