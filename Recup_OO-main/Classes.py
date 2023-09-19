class Cadastro:
    def __init__(self, n_conta):
        self._nome = None
        self._cpf = None
        self._senha = None
        self._n_conta = n_conta
        self.ncontas = []

    def getCadastro(self):
        return(self._nome, self._n_conta)
    def setCadastro(self):
        try:
            self._nome = input("Digite o nome do cliente: ")
            self._cpf = input("Digite o cpf do cliente: ")
            self._senha = input("Digite a senha do cliente: ")
        except Exception as erro:
            print("Erro ao tentar criar cadastro!")
        if self._nome == None and self._cpf == None and self._n_conta == None:
            print("Cadastro excluido!")
        else:
            print("Cadastro criado com sucesso!")
            self.ncontas.append(self._n_conta)

class ExcluirConta:
    def __init__(self, nome, saldo):
        self.titular = nome
        self.saldo = saldo
   def excluir_conta(self):
        if self.saldo == 0:
            print(f"Conta do titular excluída com sucesso.")
        else:
            print("Não é possível excluir a conta. Certifique-se de que o saldo seja zero.")
            
