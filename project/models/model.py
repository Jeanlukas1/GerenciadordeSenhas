class Usuario:
    def __init__(self, nome: str, senha: str):
        self.nome = nome
        self.senha = senha
        
class SalvarSenha:
    def __init__(self, nome_site: str, email_site: str, usuario_site: str, senha_site: str):
        self.nome_site = nome_site
        self.email_site = email_site
        self.usuario_site = usuario_site
        self.senha_site = senha_site

