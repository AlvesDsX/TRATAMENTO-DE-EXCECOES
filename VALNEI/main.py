from aluno import Aluno
from campeonato import Campeonato
from jogo import Jogo
from professor import ProfessorTecnico, ProfessorMateria
from modalidade import Modalidade
from pessoa import PessoaIFRO
from aulas_turma import Aulas, Turma
from mensagem import Mensagem

#Verificando a consistência da matrícula

def validar_matricula():
    while True:
        try:
            matricula = input("Digite sua matrícula (13 dígitos): ").strip()
            if len(matricula) != 13 or not matricula.isdigit():
                raise ValueError("A matrícula deve conter exatamente 13 dígitos e apenas números.")
            return matricula
        except ValueError as e:                     #TRATAMENTO DE EXCEÇÃO EMBUTIDO
            print(f"\033[3mErro: {e}\033[0m")
        finally:
            print("Validação de matrícula finalizada.")
            
#Verificando a consistência da senha
def validar_senha():
    while True:
        senha = input("\nDigite sua senha (mínimo 8 caracteres, ao menos um número.): ").strip()
        if len(senha) < 8 or not any(char.isdigit() for char in senha):
            print("\033[3mA senha deve ter pelo menos 8 caracteres e conter ao menos um número.\033[0m")
        else:
            return senha

def coletarInformacoesUsers():
    while True:
        nome = input("Digite seu nome: ").strip()
        if len(nome) == 0:
            print("\033[3mO campo nome não pode estar vazio.\033[0m")
        else:
            break

    matricula = validar_matricula()  #Validando a matrícula
    senha = validar_senha()          #Validando a senha

    return {"Nome": nome, "Matrícula": matricula, "Senha": senha}

#Função para justificar a falta   ------>> TRATAMENTO DE EXCEÇÃO

def justificar_falta():
    try:
        aluno_nome = input("Digite o nome do aluno que deseja justificar a falta: ")
        print("\nEscolha o motivo para justificar a sua ausência (somente para jogos escolares):")
        motivos = [
            "1. Participação em Jogo Escolar",
            "2. Treinamento para Jogo Escolar",
            "3. Representação da Escola em Jogo Escolar",
            "4. Participação em Campeonato de Jogos Escolares"
        ]
        
        for motivo in motivos:
            print(motivo)
        
        while True:
            escolha = input("\nDigite o número da opção escolhida: ").strip()
            
            if escolha == '1':
                motivo = "Participação em Jogo Escolar"
                break
            elif escolha == '2':
                motivo = "Treinamento para Jogo Escolar"
                break
            elif escolha == '3':
                motivo = "Representação da Escola em Jogo Escolar"
                break
            elif escolha == '4':
                motivo = "Participação em Campeonato de Jogos Escolares"
                break
            else:
                print("\033[3mOpção inválida. Por favor, escolha uma opção válida.\033[0m")
        
        campeonato_nome = input("Digite o nome do campeonato relacionado: ")
        campeonato = Campeonato(campeonato_nome, "Futsal", "01/01/2024", "31/12/2024")
        data_evento = campeonato.dataInicial
        aluno = Aluno('Josmith', '1234567890123', 'senha123', 'Matutino', 'Futsal')
        destinatario = "Professor"
        mensagem = Mensagem(aluno, destinatario, campeonato, data_evento, motivo)
        mensagem.enviarNotificacao()
        print(f"Justificativa para o aluno {aluno_nome} registrada com sucesso!")
    
    except Exception as e:
        print(f"\033[3mErro ao justificar falta: {e}\033[0m")
    
    finally:
        print("Processo de justificativa finalizado.")
        
        
def menu_principal():
    while True:  # Garantir que sempre volte ao menu em caso de erro
        print("\nBem-vindo ao Sistema de Jogos Externos! - SJEx")
        print("Escolha uma opção:\n")
        print("1. Registrar novo aluno")
        print("2. Registrar novo professor")
        print("3. Criar novo campeonato")
        print("4. Agendar jogo")
        print("5. Justificar falta")
        print("6. Conversar com professor")
        print("7. Sair")
        
        try:
            opcao = input("\nDigite o número da opção desejada: ")
            
            if opcao == '1':
                aluno_info = coletarInformacoesUsers()
                aluno = Aluno(aluno_info['Nome'], aluno_info['Matrícula'], aluno_info['Senha'], 'Matutino', 'Futsal')
                print(f'\n\033[3mAluno \033[1m\033[3m{aluno.nome}\033[0m \033[3mregistrado com sucesso!\033[0m')
            
            elif opcao == '2':
                tipo_professor = input("Digite o tipo de professor (1 para Técnico, 2 para de Matéria): ")
                if tipo_professor == '1':
                    nome = input("Digite o nome do professor técnico: ")
                    matricula = validar_matricula()
                    senha = validar_senha()
                    turma = input("Digite a turma do professor técnico: ")
                    modalidade = input("Digite a modalidade do professor técnico: ")
                    professor = ProfessorTecnico(nome, matricula, senha, turma, modalidade)
                    print(f'\n\033[3mProfessor Técnico \033[1m\033[3m{professor.nome}\033[0m \033[3mregistrado com sucesso!\033[0m')
                elif tipo_professor == '2':
                    nome = input("Digite o nome do professor de matéria: ")
                    matricula = validar_matricula()
                    senha = validar_senha()
                    turma = input("Digite a turma do professor de matéria: ")
                    disciplina = input("Digite a disciplina do professor de matéria: ")
                    professor = ProfessorMateria(nome, matricula, senha, turma, disciplina)
                    print(f'\n\033[3mProfessor de matéria \033[1m\033[3m{professor.nome}\033[0m \033[3mregistrado com sucesso!\033[0m')
            
            elif opcao == '3':
                nome = input("Digite o nome do campeonato: ")
                modalidade = input("Digite a modalidade do campeonato: ")
                data_inicial = input("Digite a data inicial do campeonato (DD/MM/AAAA): ")
                data_final = input("Digite a data final do campeonato (DD/MM/AAAA): ")
                campeonato = Campeonato(nome, modalidade, data_inicial, data_final)
                print(f'Campeonato {campeonato.nomecamp} criado com sucesso!')
            
            elif opcao == '4':
                data = input("Digite a data do jogo (DD/MM/AAAA): ")
                turno = input("Digite o turno do jogo (matutino, vespertino, noturno): ")
                local = input("Digite o local do jogo: ")
                jogo = Jogo(data, turno, local)
                print(f'Jogo marcado para {jogo.data} no local {jogo.local} no turno {jogo.turno}.')
                
                campeonato_nome = input("Digite o nome do campeonato para inscrever o jogo: ")
                campeonato = Campeonato(campeonato_nome, "Futsal", "01/01/2024", "31/12/2024")
                campeonato.adicionarJogo(jogo)
            
            elif opcao == '5':
                justificar_falta()
            
            elif opcao == '6':
                aluno_nome = input("Digite o nome do aluno que deseja conversar com o professor: ")
                aluno = Aluno('João', '1234567890123', 'senha123', 'Matutino', 'Futsal')
                aluno.conversarProf()
            
            elif opcao == '7':
                print("Saindo... Até logo!")
                exit()
            
            else:
                print("\033[3mOpção inválida. Por favor, escolha uma opção válida.\033[0m")
        
        except Exception as e:
            print(f"\033[3mErro inesperado: {e}\033[0m")
        
        finally:
            print("Retornando ao menu principal...")

if __name__ == "__main__":
    menu_principal()

#A NOSSA PRINCIPAL DIFICULDADE FOI COM A PARTE PRINCIPAL DO CÓDIDO.
#ELA SE ENCONTRA INCOMPLETA. NO ENTANTO, FIZEMOS O QUE FOI ALCANCÁVEL EM REALIZAR NO DECORRER NO TEMPO.