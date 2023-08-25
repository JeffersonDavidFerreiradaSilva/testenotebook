from model.model_aluno import alunoModel
from view.view_cadastro_aluno import cadastro

class alunoControle:
    def __init__(self):

        self.model = alunoModel()
        self.view = cadastro()
    
    def gravandoAluno(self):
        nome,idade,peso = self.view.pegar_dados_aluno()
        self.model.salvarAluno()
        self.view.mostrar_menssagem("ALUNO CADASTRADO COM SUCESSO! ")