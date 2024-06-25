

# def decorador_saludo(func):
#     def envoltura():
#         print("Hola!")
#         func().
#         print("Adiós!")
#     return envoltura
# @decorador_saludo
# def saludo():
#     print("¿Cómo estás?")
# saludo()


# class Perro:
#     def __init__(self, nombre):
#         self._nombre = nombre
#     @property
#     def nombre(self):
#         return self._nombre
#     @nombre.setter
#     def nombre(self, valor):
#         self._nombre = valor
# perrito = Perro("Fido")
# print(perrito.nombre)  
# perrito.nombre = "Rex"
# print(perrito.nombre)  


def registrar_transaccion(func):
    def envoltura(self, *args, **kwargs):
        resultado = func(self, *args, **kwargs)
        self._registro.append(f"{func.__name__}: {args[0]}")
        return resultado
    return envoltura

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial
        self._registro = []
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        raise AttributeError("No se puede modificar el saldo directamente")
    @property
    def registro(self):
        return self._registro
    @registrar_transaccion
    def depositar(self, monto):
        self._saldo += monto
    @registrar_transaccion
    def retirar(self, monto):
        if monto > self._saldo:
            raise ValueError("Fondos insuficientes")
        self._saldo -= monto
cuenta = CuentaBancaria("Juan Perez", 1000)
cuenta.depositar(500)
cuenta.retirar(200)

print(f"Saldo: {cuenta.saldo}")
print("Registro de transacciones:", cuenta.registro)
