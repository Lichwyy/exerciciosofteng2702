

class Socio:
    def __init__(self, nome: str, porcentagem_da_empresa: float):
        self.nome = nome
        self.porcentagem_da_empresa = porcentagem_da_empresa

    

def calcular_valor_por_porcentagem(valor_total_da_empresa: float, lista_socios: list[Socio]):
    for socio in lista_socios:
        print(f"{socio.nome} possui: R${valor_total_da_empresa*(socio.porcentagem_da_empresa)/100}")


lista_de_socios = [Socio("Sócio 1", 33.33),
                    Socio("Sócio 2", 51),
                    Socio("Socio 3", (100-33.33-51))]

calcular_valor_por_porcentagem(1000, lista_de_socios)