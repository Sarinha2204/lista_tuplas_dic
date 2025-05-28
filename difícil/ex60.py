'''Implemente um sistema de cadastro de usu´arios com login, utilizando listas de
tuplas.'''

usuarios = []
def cadastrar_usuario(nome, senha):
    usuarios.append((nome, senha))
    print(f"Usuário {nome} cadastrado com sucesso!")
def login(nome, senha):
    if (nome, senha) in usuarios:
        print(f"Usuário {nome} logado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")
def listar_usuarios():
    if usuarios:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario[0]}, Senha: {usuario[1]}")
    else:
        print("Nenhum usuário cadastrado.")
# Exemplo de uso
cadastrar_usuario("sara", "1234")
cadastrar_usuario("luiz", "abcd")
login("raiany", "1234")
login("yasmin", "wrongpassword")
listar_usuarios()
