nome = input("Digite seu nome de usuario:")
senha = input("Digite sua senha:")

while senha == nome:
    print("Senha invalida! ja esta como nome de usuario, tente novamente com outra.")

    nome = input("Digite seu nome de usuario")
    senha = input("digite uma senha diferente")

    print("Cadastro feito com sucesso!")
