class Mensagem:
    def __init__(self, remetente, destinatario, campeonato, data, motivo):
        self.remetente = remetente                #Aluno que irá justificar a sua falta     '------> Professor Técnico(by: Vava)'
        self.destinatario = destinatario          #A quem irá se dirigir, o qual irá receber a notifcação por parte do remetente
        self.campeonato = campeonato              #Campeonato que irá intervir no horário de aula
        self.data = data                          # Data do evento
        self.motivo = motivo                      # Motivo da justificativa
        
    def enviarNotificacao(self):
        try:
            print(f"Notificação de {self.remetente.nome} para {self.destinatario}:")
            print(f"Campeonato: {self.campeonato.nomecamp}")  # Pode gerar erro se 'nomecamp' não existir
            if self.data:
                print(f"Data do evento: {self.data}")
            print(f"Motivo: {self.motivo}")
        except AttributeError as e:
            print(f"Erro ao enviar notificação: {e}")
        finally:
            print("Processo de envio de notificação concluído.")

    def preencherMensagem(self, motivo):
        try:
            if not motivo:
                raise ValueError("O motivo fornecido está vazio ou inválido.")
            self.motivo = motivo
            print("Mensagem esclarecida com o devido motivo:", self.motivo)
        except ValueError as e:
            print(f"Erro ao preencher a mensagem: {e}")
        finally:
            print("Finalizado o preenchimento da mensagem.")

    def compararHorarios(self, horarios_aula):
        if self.data in horarios_aula:
            print("Conflito detectado entre horários de aula e evento.")
            return True
        print("Nenhum conflito de horário detectado.")
        return False
    
#MENSAGEM OK