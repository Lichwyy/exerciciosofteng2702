from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    nota: float

    def relacao_com_a_media(self, media):
        if media > self.nota:
            return self.nome+" está abaixo da média"
        elif media < self.nota:
            return self.nome+" está acima da média"
        return self.nome+" está na média"
    
def alunos_e_relacao_com_a_media(lista_alunos: list[Aluno]):
    media = 0
    for aluno in lista_alunos:
        media += aluno.nota
    
    media = media/len(lista_alunos)

    for aluno in lista_alunos:
        print(aluno.relacao_com_a_media(media))

    
lista_de_alunos = list()

for _ in range(3):
    nome = input(f"Nome do Aluno {_+1}: ")
    nota = float(input(f"Nota do {nome}: "))

    lista_de_alunos.append(Aluno(nome, nota))

alunos_e_relacao_com_a_media(lista_de_alunos)
