from abc import ABC, abstractmethod

class PessoaIFROException(Exception):  #Classe com execeção personalizada para PessoaIFRO ao invés de usar ValueError
   def __init__(self, mensagem):    
      super().__init__(mensagem)

class PessoaIFRO(ABC):
  def __init__(self, nome, matricula, senha, turma):
    try:
        self.nome = nome              #será verificado com o setter
        self.matricula = matricula    #será verificado com o setter
        self.senha = senha            #será verificado com o setter
        self.turma = turma            #será verificado com o setter
    except PessoaIFROException as e:
        print(f"Ocorreu um erro ao criar objeto PessoaIFRO: {e}")
        raise

  @property
  def nome(self):
      return self._nome

  @nome.setter
  def nome(self, nome):
      if len(nome.strip()) > 0: #Verificação do nome, remove os espaços e analisa o comprimento do nome e quant. de strings
        self._nome = nome
      else:
          raise PessoaIFROException("\033[3mO nome não pode está vazio.\033[0m")
 
  @property
  def matricula(self):
      return self._matricula

  @matricula.setter
  def matricula(self, matricula):
      if matricula.isdigit() and len(matricula) == 13: #Verificando se a matrícula contém N° IR inteiros > 0 e se o seu comprimento é igual a 13.
        self._matricula = matricula
      else:
          raise PessoaIFROException("\033[3mA matrícula deve conter exatamente 13 dígitos*\033[0m")

  @property
  def senha(self):
      return self._senha

  @senha.setter
  def senha(self, senha):
      if len(senha) >= 8 and any(c.isdigit() for c in senha):
        self._senha = senha
      else:
          raise PessoaIFROException("\033[3mA senha deve conter pelo menos 8 caracteres com ao menos um número*\033[0m")
      
  @property
  def turma(self):
     return self._turma
  
  @turma.setter
  def turma(self, turma):
     if len(turma.strip()) > 0: #Verificando se o que for escrito for > 0 caracteres para validar que o campo não fique vazio.
        self._turma = turma
     else: 
        raise PessoaIFROException('O campo "Turma" não pode estar vazio.')
      
  def verificar_senha(self, senha):
      return self._senha == senha
  
  @classmethod
  def registrar(cls):
    try:
        nome = input("Favor, digite o seu nome: ").strip()
        matricula = input("Digite sua matrícula (13 dígitos): ").strip()
        senha = input("Digite sua senha (mínimo 8 caracteres): ").strip()
        turma = input("Digite sua turma: ").strip()

        return cls(nome, matricula, senha, turma)
    except PessoaIFROException as e:
       print(f"Erro ao registrar usuários: {e}")
    except Exception as e:
       print(f"Erro inesperado. {e}")
    finally:
       print("Operação de registro finalizada!")

if __name__ == "__main__":
   try:
      pessoa = PessoaIFRO.registrar()
      print("Usuário criado com sucesso!")
   except Exception:
      print("Ocorreu uma falha ao criar usuário.")
      
#PESSOAIFRO(ABC) OK