senha_certa = "123456"
usuario_certo = "yasmin@empresa.com"

u = input("Informe username: ")
if u == usuario_certo:
    p = input("Informe o password: ")
    if p == senha_certa:
        print("Credenciais válidas")
    else:
        print("Senha inválida")
else:
    print("Usuário inválido") 