from typing import List
from aluno import Aluno

class Modalidade():
    def __init__(self, modalidade: str):
        self.modalidade = modalidade
        self.time = List[Aluno] = []

    def adicionarAluno(self, aluno: Aluno):
        try:
            if not isinstance(aluno, Aluno):
                raise TypeError("Somente objetos do tipo 'Aluno' podem ser adicionados ao time.")
            
            if aluno in self.time:
                print(f"Aluno {aluno.nome} já está no time de {self.modalidade}.")

            else:
                self.time.append(aluno)
                print(f'Aluno {aluno.nome} foi adicionado ao time de {self.modalidade}.')
        except TypeError as e:
                        print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def visualizarTime(self):
        try:
            if not self.time:
                 print(f"Não há alunos no time de {self.modalidade}.")
                 return []
            
            for aluno in self.time:
                print(f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}")
            return self.time
        except Exception as e:
            print(f"Ocorreu um erro ao visualizar o time: {e}")
    
#MODALIDADE OK