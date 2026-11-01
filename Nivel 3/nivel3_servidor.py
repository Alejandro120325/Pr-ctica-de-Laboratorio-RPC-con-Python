import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="session")
class CuentaBancaria(object):
    def __init__(self):
        self.saldo = 0.0

    def depositar(self, monto):
        monto = float(monto)
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a cero")
        self.saldo += monto
        return self.saldo

    def retirar(self, monto):
        monto = float(monto)
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a cero")
        self.saldo -= monto
        return self.saldo

    def consultar_saldo(self):
        return self.saldo

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(CuentaBancaria)
ns.register("practica.banco", uri)

print("Servidor bancario listo (Nivel 3)")
daemon.requestLoop()