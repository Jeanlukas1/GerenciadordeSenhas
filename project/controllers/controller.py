from models.model import Usuario
from dals.dal import CadastroDal

class VerificarCadastroController:
    @classmethod
    def cadastrar(cls, nome: str, senha: str):
        if len(nome) < 3:
            return False, "Nome deve ter no mínimo 3 caracteres"
        if len(senha) < 5:
            return False, "Senha deve ter no mínimo 5 caracteres"

        usuario = Usuario(nome, senha)
        CadastroDal.salvar_usuario(usuario)
        return True, "Usuário cadastrado com sucesso"
