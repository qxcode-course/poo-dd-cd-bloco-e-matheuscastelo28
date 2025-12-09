from abc import ABC, abstractmethod

class Pagamento:
    def __init__(self, valor: int, descriçao: str):
        self.valor = valor 
        self.descriçao = descriçao
    
    def resumo(self) -> str:
        return f" Pagamento de R${self.valor}: {self.descriçao}"
    
    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError ("Falhou: valor invalido")

    @abstractmethod
    def processar(self):
         pass
     
class CartaoCredito(Pagamento):
    def __init__(self, num: int, nome: str, limite:float, valor:int, descriçao: str):
        super().__init__(valor, descriçao)
        self.num = num
        self.nome = nome
        self.limite: float = limite 
        
    def resumo (self):
        return "Cartao de Credito" + super().resumo()
    
    def get_limite(self):
        return self.limite 
        