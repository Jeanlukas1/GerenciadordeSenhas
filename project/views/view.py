from controllers.controller import VerificarCadastroController

def iniciar_menu():
    while True:
        print("="*60)
        print("Bem-vindo ao Sistema de Gerenciamento de Senhas")
        print("1 - Cadastrar usuário")
        print("2 - Sair")
        print("="*60)

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido")
            continue

        if opcao == 1:
            nome = input("Nome: ")
            senha = input("Senha: ")

            sucesso, mensagem = VerificarCadastroController.cadastrar(nome, senha)
            print(mensagem)

        elif opcao == 2:
            print("Saindo...")
            break
        else:
            print("Opção inválida")
