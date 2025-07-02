from clear import clear
from participante import Cadastrar_participante, listar_participantes, consultar_participante, remover_participante, atualizar_participante, listar_participantes_por_evento
from evento import Cadastrar_evento, listar_evento, consultar_evento, remover_evento, atualizar_evento, consultar_eventos_por_status, cadastrar_participante_em_evento
from estatisticas import temas_frequentes, participantes_mais_ativos


def Menu():
    while True:
        #clear()
        print('            Menu Principal           ')
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Remover")
        print("4 - Atualizar Informações")
        print("5 - Consultar")
        print("6 - Verificar Estatísticas ")
        print("0 - Sair")
        op = opcao(6)

        if op == 1:
            cadastrar()
        elif op == 2:
            listar()
        elif op == 3:
            remover()
        elif op == 4:
            atualizar()
        elif op == 5:
            consultar()
        elif op == 6:
            estatisticas()
        elif op == 0:
            break


def cadastrar():
    while True:
        print('            Cadastro            ')
        print("1 - Cadastrar Participante")
        print("2 - Cadastrar Evento")
        print("3 - Cadastrar Participante em Evento")
        print("0 - Voltar")
        op = opcao(3)

        if op == 1:
            cadastrar_participante()
        elif op == 2:
            cadastrar_evento()
        elif op == 3:
            cadastrar_participante_em_evento()
        elif op == 0:
            break


def listar():
    while True:
        print('            Listar            ')
        print("1 - Listar Eventos")
        print("2 - Listar Participantes")
        print("3 - Listar Participantes por Evento")
        print("0 - Voltar")
        op = opcao(3)

        if op == 1:
            listar_evento()
        elif op == 2:
            listar_participantes()
        elif op == 3:
            listar_participantes_por_evento()
        elif op == 0:
            break


def consultar():
    while True:
        print('            Consultar            ')
        print("1 - Consultar Participante por Código")
        print("2 - Consultar Eventos por Código")
        print("3 - Consultar Eventos por Status")
        print("0 - Voltar")
        op = opcao(3)

        if op == 1:
            consultar_participante()
        elif op == 2:
            consultar_evento_por_codigo()
        elif op == 3:
            consultar_eventos_por_status()
        elif op == 0:
            break



def opcao(limite):
    while True:
        try:
            op = int(input("Digite a opção desejada: "))
            if 0 <= op <= limite:
                return op
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def cadastrar_participante():
    print('            Cadastro de Participante            ')
    codigo = input("Digite o código do participante: ").strip()
    nome = input("Digite o nome completo: ").strip()
    email = input("Digite o e-mail: ").strip()
    preferencias = input("Digite as preferências temáticas (separadas por vírgula): ").strip()

    sucesso = Cadastrar_participante(codigo, nome, email, preferencias_tema=[p.strip() for p in preferencias.split(',')])
    if sucesso:
        print(f"Participante {nome} cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar participante. Código já existente.")
    input("Pressione Enter para continuar...")
    clear()

def cadastrar_evento():
    print('            Cadastro de Evento            ')
    cod_evento = input("Digite o código do evento: ")
    nome = input("Digite o nome único do evento: ")
    tema_central = input("Digite o tema do evento: ")
    tipo_evento  = input("Digite o tipo de evento: ")
    data_realizacao = input("Digite a data de realização do evento (DD/MM/AAAA): ")
    limite = input("Digite o limite de participantes (deixe em branco se não houver): ").strip()
    limite = int(limite) if limite.isdigit() else None
    status = 'ativo' 

    sucesso = Cadastrar_evento(cod_evento, nome, tema_central, tipo_evento, limite, status, data_realizacao)
    if sucesso:
        print(f"Evento {nome} cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar evento. Nome já existente.")
    input("Pressione Enter para continuar...")
    clear()


def remover():
    print('            Remover            ')
    print("1 - Remover Participante")
    print("2 - Remover Evento")
    print("0 - Voltar")
    op = opcao(2)
    if op == 1:
        cod_participante = input("Digite o código do participante que deseja remover: ").strip()
        sucesso = remover_participante(cod_participante)
        if sucesso:
            print("Participante removido com sucesso.")
        else:
            print("Participante não encontrado.")
    elif op == 2:
        cod_evento = input("Digite o código do evento que deseja remover: ").strip()
        sucesso = remover_evento(cod_evento)
        if sucesso:
            print("Evento removido com sucesso.")
        else:
            print("Evento não encontrado.")
    input("Pressione Enter para continuar...")
    clear()

def atualizar():
    print('            Atualizar            ')
    print("1 - Atualizar Participante")
    print("2 - Atualizar Evento")
    print("0 - Voltar")
    op = opcao(2)
    if op == 1:
        cod_participante = input("Digite o código do participante: ").strip()
        participante = consultar_participante(cod_participante)
        if participante:
            print(f"Atualizando participante: {participante['nome']}")
            email = input("Novo e-mail (deixe em branco para manter): ").strip()
            preferencias = input("Novas preferências temáticas (separadas por vírgula, deixe em branco para manter): ").strip()
            prefs = [p.strip() for p in preferencias.split(',')] if preferencias else None
            atualizar_participante(cod_participante, email=email if email else None, preferencias=prefs)
            print("Participante atualizado com sucesso.")
        else:
            print("Participante não encontrado.")
    elif op == 2:
        nome = input("Digite o nome do evento: ").strip()
        evento = consultar_evento(nome)
        if evento:
            print(f"Atualizando evento: {evento['nome']}")
            tema_central = input("Novo tema (deixe em branco para manter): ").strip()
            limite = input("Novo limite de participantes (deixe em branco para manter): ").strip()
            limite = int(limite) if limite.isdigit() else None
            status = input("Novo status (ativo, cancelado, deixe em branco para manter): ").strip()
            data_realizacao = input("Nova data de realização (DD/MM/AAAA, deixe em branco para manter): ").strip()
            atualizar_evento(nome, tema_central=tema_central if tema_central else None, limite=limite, status=status if status else None, data_realizacao=data_realizacao if data_realizacao else None)
            print("Evento atualizado com sucesso.")
        else:
            print("Evento não encontrado.") 
    
def estatisticas():
    print('            Estatísticas dos Eventos e Participantes            ')
    print("1 - Temas mais frequentes")
    print("2 - Participantes mais ativos")
    print("0 - Voltar")
    op = opcao(2)
    if op == 1:
        temas_frequentes()
    elif op == 2:
        participantes_mais_ativos()
    else:
        pass
    input("Precione Enter para continuar...")
    clear()


def Consultar_participante(cod_participante):
    cod_participante = input("Digite o código do participante: ").strip()
    participante = consultar_participante(cod_participante)
    if participante:
        print(f"Código: {participante['cod_participante']}")
        print(f"Nome: {participante['nome']}")
        print(f"E-mail: {participante['email']}")
        print(f"Preferências Temáticas: {', '.join(participante['preferencias_tema'])}")
        print(f"Eventos inscritos: {', '.join(participante.get('eventos', []))}")
    else:
        print("Participante não encontrado.")
    input("Pressione Enter para continuar...")
    clear()


def consultar_evento_por_codigo():
    cod = int(input("Digite o código do evento: "))
    evento = consultar_evento(cod)
    if evento:
        print(f"Código: {evento['cod']}")
        print(f"Nome: {evento['nome']}")
        print(f"Data de Realização: {evento['data_realizacao']}")
        print(f"Limite de Participantes: {evento['limite']}")
        print(f"Status: {evento['status']}")
    else:
        print("Evento não encontrado.")
    input("Pressione Enter para continuar...")
    clear()


def verificar_em_evento(cod_evento):
    if cod_evento in cadastrar_evento:
        return cadastrar_evento[cod_evento]


def listar_participantes_em_evento():
    cod_evento = int(input("Digite o código do evento: "))
    if verificar_em_evento(cod_evento):
        print("Evento: ", cadastrar_evento[cod_evento]['nome'])
        listar_participantes(cod_evento)
    else: 
        print("Evento não encontrado.")
    input("Pressione Enter para continuar...")
    clear()

def consultar_evento_por_status():
    status = input("Digite o status do evento (ativo, cancelado): ").strip()
    consultar_eventos_por_status(status)
    input("Pressione Enter para continuar...")
    clear()


