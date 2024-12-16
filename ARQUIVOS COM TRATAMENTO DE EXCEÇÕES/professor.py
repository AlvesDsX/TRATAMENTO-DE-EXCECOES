from pessoa import PessoaIFRO, PessoaIFROException
from mensagem import Mensagem  

class ProfessorMateria(PessoaIFRO):
    def __init__(self, nome, matricula, senha, turma, disciplina):
        super().__init__(nome, matricula, senha, turma)
        self.disciplina = disciplina

    @property
    def disciplina(self):
        return self._disciplina

    @disciplina.setter
    def disciplina(self, disciplina):
        if not disciplina or not isinstance(disciplina, str):
            raise PessoaIFROException("O campo 'Disciplina' não pode está vazio e deve conter uma string válida.")
        # O setter pode fazer alguma validação ou transformação se necessário
        self._disciplina = disciplina

    def receberMensagem(self, mensagem):
        try:
            if not isinstance(mensagem, Mensagem):
                raise TypeError("O parâmetro 'mensagem' deve ser uma instância válida de Mensagem")
            
            print(f"Mensagem recebida de {mensagem.remetente} para {mensagem.destinatario}")
            print(f"Motivo: {mensagem.motivo}")
            print(f"Data do Evento: {mensagem.data}")
            print(f"Campeonato: {mensagem.campeonato.nomecamp}")
        except Exception as e:
            print(f"Ocorreu um erro ao receber mensagem: {e}.")

    def abdicarFalta(self, aluno, campeonato):
        try:
            if not aluno or not hasattr(aluno, 'nome'):
                raise ValueError("O objeto 'aluno' deve ter um atributo 'nome'.")
            if not campeonato or not hasattr(campeonato, 'nomecamp'):
                raise ValueError("O objeto 'campeonato' deve ter um atributo 'nomecamp'.")

            # Aqui o professor de matéria pode abdicar da falta do aluno
            print(f"Falta negada para o aluno {aluno.nome} por participação no campeonato {campeonato.nomecamp}")
        except Exception as e:
            print(f"Ocorreu um erro ao abdicar falta: {e}.")


class ProfessorTecnico(PessoaIFRO):
    def __init__(self, nome, matricula, senha, turma, modalidade):
        super().__init__(nome, matricula, senha, turma)
        self.modalidade = modalidade  #A modalidade associada ao professor técnico

    def preencherMensagem(self, professor_materia, aluno, campeonato, data_evento, motivo):
        try:
            if not all([professor_materia, aluno, campeonato, data_evento, motivo]):
                raise ValueError("Todos os parâmetros devem ser fornecidos e válidos.")
            
            if not isinstance(professor_materia, ProfessorMateria):
                raise TypeError("O parâmetro 'professor_materia' deve ser uma instância de ProfessorMateria.")
            # Preenche uma instância de Mensagem com os dados necessários


            mensagem = Mensagem(
                remetente=self.nome,
                destinatario=professor_materia.nome,
                campeonato=campeonato,
                data=data_evento,
                motivo=motivo
            )
            # A mensagem preenchida pode ser retornada ou processada conforme necessário
            return mensagem
        except Exception as e:
            print(f"Ocorreu um erro ao preencher mensagem: {e}.")
            return None

    def notificarProfessor_Materia(self, professor_materia, aluno, campeonato, data_evento, motivo):
        try:
            # Cria e envia uma notificação para o professor de matéria
            mensagem = self.preencherMensagem(professor_materia, aluno, campeonato, data_evento, motivo)
            if mensagem:  # Somente prossegue se a mensagem foi preenchida com sucesso
                professor_materia.receberMensagem(mensagem)
                print(f"Notificação enviada para o professor de {professor_materia.disciplina}: {professor_materia.nome}")
        except Exception as e:
            print(f"Erro ao notificar professor de matéria: {e}")

#PROFESSORTEC e PROFESSORMAT (PESSOAIFRO) OK