class Conta():
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo do titular {} é {}".format(self.__titular, self.__saldo))
        
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Saque efetuado.")
        else:
            print("Saldo insuficiente.")

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = (self.__saldo + self.__limite)
        return (valor_a_sacar <= valor_disponivel)

    def transfere(self, valor, obj_destino):
        self.saca(valor)
        obj_destino.deposita(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self):
        return self.__limite

    @staticmethod
    def codigo_banco():
        return "001"
