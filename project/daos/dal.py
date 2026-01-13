from models.model import Usuario
# from models.model import SalvarSenha

class CadastroDal:
    @classmethod
    def salvar_usuario(cls, usuario: Usuario):
        with open("cadastro.txt", "a", encoding="utf-8") as arq:
            arq.write(f"Usuário: {usuario.nome} | Senha: {usuario.senha}\n")

    # @classmethod
    # def listar_usuarios(cls):
    #     lista_objetos_usuario = []
        
    #     try:
    #         with open("cadastro.txt", "r", encoding="utf-8") as arq:
    #             for linha in arq:
    #                 # A linha é: "Usuário: joao | Senha: 123"
    #                 # Vamos limpar e quebrar os dados
    #                 linha_limpa = linha.strip()
    #                 dados = linha_limpa.split(' | ') # Separa em ['Usuário: joao', 'Senha: 123']
                    
    #                 if len(dados) == 2:
    #                     # Extrai só o valor (removendo "Usuário: " e "Senha: ")
    #                     nome = dados[0].replace("Usuário: ", "")
    #                     senha = dados[1].replace("Senha: ", "")
                        
    #                     # Recria o objeto Usuario (O Model!)
    #                     novo_usuario = Usuario(nome, senha)
    #                     lista_objetos_usuario.append(novo_usuario)
            
    #         return lista_objetos_usuario # Devolve lista de OBJETOS, não de texto
            
    #     except FileNotFoundError:
    #         return []

# class CadastroSenhaSiteDal:
#     @classmethod
#     def salvar_senha(cls, salva_senha: SalvarSenha):
#         with open("senhas.txt", "a", encoding="UTF-8") as arq:
#             arq.write(f"Nome do Site: {salva_senha.nome_site} |")