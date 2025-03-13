from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    altura: float
    peso: float


    def calcular_imc(self):
        return self.peso/(self.altura**2)
    
def definir_peso_anormal(lista_pessoas: list[Pessoa]):
    for pessoa in lista_pessoas:
        if pessoa.calcular_imc() <= 24.9 and pessoa.calcular_imc() >= 18.5:
            print(f"{pessoa.nome} está no peso normal")
        else:
            print(f"{pessoa.nome} está fora do peso normal")

    
lista_de_pessoas = list()

for _ in range(3):
    nome = input(f"Nome da pessoa {_+1}: ")
    altura = float(input(f"Altura do/a {nome}: "))
    peso = float(input(f"Peso do/a {nome}: "))

    lista_de_pessoas.append(Pessoa(nome, altura, peso))

definir_peso_anormal(lista_de_pessoas)
