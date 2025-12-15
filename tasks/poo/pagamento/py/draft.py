from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor: float = valor
        self.descricao = descricao

    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor}: {self.descricao}"

    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")

    @abstractmethod
    def processar(self):
        pass


class CartaoCredito(Pagamento):  # acoplamento forte
    def __init__(self, num: int, nome: str, limite: float, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.num = num
        self.nome = nome
        self.limite: float = limite

    def resumo(self):
        return "Cartao de Credito: " + super().resumo()

    def get_limite(self):
        return self.limite

    def processar(self):
        if self.valor > self.limite:
            print("pagamento recusado por limite insuficiente")
            return
        self.limite -= self.valor


class Pix(Pagamento):
    def __init__(self, chave: str, valor: float, descricao: str, saldoDisp: float, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.saldoDisp = saldoDisp
        self.banco = banco

    def resumo(self):
        return "Pix: " + super().resumo()

    def processar(self):
        if self.valor > self.saldoDisp:
            print("Saldo insuficiente para pagamento via Pix")
            return
        if not self.chave:
            print("Chave Pix inválida")
            return
        if not self.banco:
            print("Banco inválido")
            return
        self.saldoDisp -= self.valor
        print(
            f"Pagamento via Pix com a chave: [{self.chave}] realizado pelo banco {self.banco} com sucesso")


class Boleto(Pagamento):
    def __init__(self, codigo_barras: str, vencimento: str, valor: float, descricao: str, saldoDisp: float):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento
        self.saldoDisp = saldoDisp

    def resumo(self):
        return "Boleto: " + super().resumo()

    def processar(self):
        if not self.codigo_barras:
            print("Código de barras inválido")
            return
        if not self.vencimento:
            print("Data de vencimento inválida")
            return
        if self.valor > self.saldoDisp:
            print("Saldo insuficiente para pagamento via Boleto")
            return
        self.saldoDisp -= self.valor
        print(f"Boleto gerado. Aguardando pagamento...")


def processar_pagamentos(pagamentos: Pagamento):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance(pag, CartaoCredito):
            print(pag.get_limite())


pag: Pagamento = CartaoCredito(
    nome="David", descricao="Coxinha", limite=500.00, num=123, valor=0.50)
pagamentos: Pagamento = [pag]
processar_pagamentos(pagamentos)

