from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.entrada = 0

    def getId(self):
        return self.id

    def getTipo(self):
        return self.tipo

    def setEntrada(self, nova_entrada: int):
        self.entrada = nova_entrada

    @abstractmethod
    def calcularValor(self, tempo_saida: int) -> float:
        pass

    def toString(self) -> str:
        return (
            f"{self.tipo:>10}".replace(" ", "_") + " : " +
            f"{self.id:>10}".replace(" ", "_") + " : " +
            str(self.entrada)
        )

    def __str__(self):
        return self.toString()
    
class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")

    def calcularValor(self, tempo_saida: int) -> float:
        return 3.0

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularValor(self, tempo_saida: int) -> float:
        minutos = tempo_saida - self.entrada
        return minutos / 20


class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def calcularValor(self, tempo_saida: int) -> float:
        minutos = tempo_saida - self.entrada
        valor = minutos / 10
        return 5.0 if valor < 5 else valor
    
class Estacionamento:
    def __init__(self):
        self.veiculos: list[Veiculo] = []
        self.hora_atual = 0

    def tempo(self, minutos: int):
        self.hora_atual += minutos

    def estacionar(self, tipo: str, id: str):
        if self.buscar(id):
            print("fail: veiculo ja existe")
            return

        if tipo == "bike":
            v = Bike(id)
        elif tipo == "moto":
            v = Moto(id)
        elif tipo == "carro":
            v = Carro(id)
        else:
            print("fail: tipo invalido")
            return

        v.setEntrada(self.hora_atual)
        self.veiculos.append(v)

    def buscar(self, id: str):
        for v in self.veiculos:
            if v.getId() == id:
                return v
        return None

    def pagar(self, id: str):
        veiculo = self.buscar(id)
        if veiculo is None:
            print("fail: veiculo nao encontrado")
            return

        tempo_saida = self.hora_atual
        valor = veiculo.calcularValor(tempo_saida)

        print(
            f"{veiculo.getTipo()} chegou {veiculo.entrada} "
            f"saiu {tempo_saida}. Pagar R$ {valor:.2f}"
        )

        self.veiculos.remove(veiculo)

    def show(self):
        for v in self.veiculos:
            print(v)
        print(f"Hora atual: {self.hora_atual}")
def main():
    estacionamento = Estacionamento()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "tempo":
            estacionamento.tempo(int(args[1]))

        elif args[0] == "estacionar":
            estacionamento.estacionar(args[1], args[2])

        elif args[0] == "pagar":
            estacionamento.pagar(args[1])

        elif args[0] == "show":
            estacionamento.show()

        else:
            print("fail: comando invalido")


main()
