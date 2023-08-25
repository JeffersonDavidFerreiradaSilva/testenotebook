class cadastro:
    @staticmethod
    def pegar_dados_aluno():
        nome = input("DIGITE SEU NOME: ")
        idade = int(input("DIGITE SUA IDADE: "))
        peso = float(input("DIGITE SEU PESO: "))
        return nome, idade, peso
    @staticmethod
    def mostrar_menssagem(menssagem):
        print(menssagem)   
        print("---"*10)     