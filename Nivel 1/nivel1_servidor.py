import Pyro4

@Pyro4.expose
class Calculadora(object):
    def sumar(self, a, b):
        return float(a) + float(b)

    def restar(self, a, b):
        return float(a) - float(b)

    def multiplicar(self, a, b):
        return float(a) * float(b)

    def dividir(self, a, b):
        if float(b) == 0:
            raise ValueError("No se puede dividir para cero.")
        return float(a) / float(b)

# Configuración SIN Name Server (Directo por URI)
daemon = Pyro4.Daemon()
uri = daemon.register(Calculadora)

print("Calculadora lista.")
print(f"URI DEL SERVIDOR (Copia y pega esto en el cliente): {uri}")

daemon.requestLoop()