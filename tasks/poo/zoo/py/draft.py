from abc import ABC, abstractmethod

class Animal (ABC):
    def _init_(self,nome) -> None:
        self.nome = nome 
        
    def apresenta_nome(self, nome: str):
        print(f"eu sou{self.nome}")
        
    
    @abstractmethod
    def fazer_som(self) -> None: 
        pass
    @abstractmethod
    def mover(self) -> None:
        pass
    
def apresentar(animal: Animal):
        animal.fazer_som()
        animal.mover()
        animal.apresentar_nome()
        
        
class Leao(Animal):
    def _init_(self, nome: str) -> None:
        super()._init_(nome)
        
    def fazer_som(self):
        print("graaaaaaaaaam")
    def mover(self):
        print ("caminhando em caminho")
    def apresenta_nome(self, nome):
        pass
    
class Urso(Animal):
    def _init_(self,nome:str) -> None:
        super()._init_(nome)
        
    def fazer_som(self):
        print("UUUUUU")
    def mover(self):
        print("caminhando no gelo em silencio")
    def apresenta_nome(self, nome):
        pass