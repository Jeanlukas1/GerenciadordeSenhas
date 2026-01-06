from models.model import Usuario

class CadastroDal:
    @classmethod
    def salvar_usuario(cls, usuario: Usuario):
        with open("cadastro.txt", "a", encoding="utf-8") as arq:
            arq.write(f"Usuário: {usuario.nome} | Senha: {usuario.senha}\n")

    @classmethod
    def listar_usuarios(cls):
        try:
            with open("cadastro.txt", "r", encoding="utf-8") as arq:
                return arq.readlines()
        except FileNotFoundError:
            return []
