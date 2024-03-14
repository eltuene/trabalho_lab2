from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, ano, marca, preco_por_dia):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.preco_por_dia = preco_por_dia

    @abstractmethod
    def calcular_aluguel(self):
        pass
    
    def __str__(self):
        return f"{self.marca} {self.modelo}, {self.ano} - R${self.preco_por_dia} por dia"

class Carro(Veiculo):
    def calcular_aluguel(self):
        return self.preco_por_dia * 1.1

class Moto(Veiculo):
    def calcular_aluguel(self):
        return self.preco_por_dia * 1.05

class Caminhao(Veiculo):
    def calcular_aluguel(self):
        return self.preco_por_dia * 1.2

class SistemaAluguel:
    @staticmethod
    def alugar_veiculo(veiculo, dias):
        return veiculo.calcular_aluguel() * dias
    @staticmethod
    def listar_veiculos(veiculos):
        for veiculo in veiculos:
            print(veiculo)

if __name__ == "__main__":
    carro = Carro("Fusca", 1970, "VW", 100)
    moto = Moto("Motinha", 2000, "Honda", 50)
    caminhao = Caminhao("Do Lixo", 2015, "Volvo", 200)
    SistemaAluguel.listar_veiculos([carro, moto, caminhao])