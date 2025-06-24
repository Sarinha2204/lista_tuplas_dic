'''
Para o participante:
Código único de identificação (ID)
Nome completo
E-mail
Preferências temáticas (áreas de interesse)
Eventos inscritos (lista ou referência aos eventos em que está inscrito)
Status da inscrição (opcional, ex: confirmado, pendente)
Dados para comunicação (telefone, se aplicável)
Histórico de participação (eventos anteriores, se for relevante)

Para o evento:
Nome único do evento
Data de realização
Tema central (ex: Inteligência Artificial, Web, Segurança)
Lista de participantes inscritos
Local do evento (se aplicável)
Descrição ou objetivo do evento
Tipo de evento (workshop, palestra, maratona, etc.)
Status do evento (ativo, cancelado, etc.)
Limite de participantes (para controle de vagas)
Informações administrativas (responsáveis, contatos)
Possibilidade de inscrição (aberta, fechada, com aprovação)

def Menu():
    clear()
    print('            Menu            ')
    print("1 - Cadastrar novo Participante")
    print("2 - Cadastrar novo Evento") 
    print("3 - Listar Eventos")
    print("4 - Listar Participantes")
    print("5 - Listar Participantes por Evento")
    print("6 - Remover Evento ou Participante")
    print("7 - Relatório de Participantes")
    print("0 - Sair")
    op = opcao(4)
    
    if op == 1:
        Cadastrar()
    elif op == 2:
        Matricular()
    elif op == 3:
        Consultar()
    elif op == 4:
        Relatorio()
    elif op == 0:
        exit()
        
        
def opcao(limite):
    while True:
        try:
            op = int(input("Digite a opção desejada: "))
            if 0 <= op <= limite:
                return op
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def Cadastrar():
    print('            Menu Cadastro            ')
    print("1 - Participante")
    print("2 - Evento") 
    print("0 - Voltar")
    op = opcao(3)

    if op == 1:
        nome = input("Digite o nome do participante: ")
        cpf = input("Digite o CPF do participante: ")
        evento = input(f"Qual evento o Sr(a) {nome} deseja se inscrever? ")
        Cadastrar_participante(nome, evento, cpf)
        print(f"Participante {nome} cadastrado com sucesso!")
    elif op == 2:
        evento = input("Digite o nome do evento: ")
        matricula = input("Digite a matrícula do professor: ")
        disciplina = input("Digite a disciplina: ")
        cadastrar_professor(nome, matricula, disciplina)
        print(f"Professor {nome} cadastrado com sucesso!")
    elif op == 3:
        nome = input("Digite o nome da turma: ")
        codigo = input("Digite o código da turma: ")
        professor = input("Digite o nome do professor: ")
        turma = {'nome': nome, 'codigo': codigo, 'professor': professor, 'alunos': []}
        cadastrar_turma(turma)
        print(f"Turma {nome} cadastrada com sucesso!")

def Consultar():
    print('++++++++++++ Menu Consultar ++++++++++++')
    print("1 - Aluno")
    print("2 - Professor") 
    print("3 - Turma")
    print("0 - Voltar")
    op = opcao(3)

    if op == 1:
        listar_alunos()
    elif op == 2:
        listar_professores()
    elif op == 3:
        listar_turmas()

def Matricular():
    print('++++++++++++ Menu Matrícula ++++++++++++')
    print("1 - Matricular aluno em turma")
    print("0 - Voltar")
    op = opcao(1)

    if op == 1:
        from aluno import consultar_aluno
        from turma import consultar_turma
        matricula = input("Digite a matrícula do aluno: ")
        aluno = consultar_aluno(matricula)
        if aluno is None:
            print("Aluno não encontrado.")
            return
        codigo = input("Digite o código da turma: ")
        turma = consultar_turma(codigo)
        if turma is None:
            print("Turma não encontrada.")
            return
        turma['alunos'].append(aluno['nome'])
        print(f"Aluno {aluno['nome']} matriculado na turma {turma['nome']}.")

def Relatorio():
    print('++++++++++++ Relatório de Turmas ++++++++++++')
    listar_participantes()
'''

from clear import clear
from participante import Cadastrar_participante, listar_participantes, consultar_participante, remover_participante, atualizar_participante, listar_participantes_por_evento
from evento import Cadastrar_evento, listar_evento, consultar_evento, remover_evento, atualizar_evento, consultar_evento_por_codigo

def Menu():
    while True:
        #clear()
        print('            Menu Principal           ')
        print("1 - Cadastrar novo Participante")
        print("2 - Cadastrar novo Evento") 
        print("3 - Listar Eventos")
        print("4 - Listar Participantes")
        print("5 - Listar Participantes por Evento")
        print("6 - Remover Evento ou Participante")
        print("7 - Atualizar Evento ou Participante")
        print("8 - Consultar Participante por Código")
        print("0 - Sair")
        op = opcao(9)
        
        if op == 1:
            cadastrar_participante()
        elif op == 2:
            cadastrar_evento()
        elif op == 3:
            listar_evento()
        elif op == 4:
            listar_participantes() 
        elif op == 5:
            listar_participantes_por_evento()
        elif op == 6:
            remover()
        elif op == 7:
            atualizar()
        elif op == 8:
            consultar_participante_por_codigo()
        elif op == 9:
            consultar_evento_por_codigo()
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
    codigo = input("Digite o código único do participante: ").strip()
    nome = input("Digite o nome completo: ").strip()
    email = input("Digite o e-mail: ").strip()
    
    sucesso = Cadastrar_participante(codigo, nome, email)
    if sucesso:
        print(f"Participante {nome} cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar participante. Código já existente.")
    input("Pressione Enter para continuar...")
    clear()

def cadastrar_evento():
    print('            Cadastro de Evento            ')
    cod = input("Digite o código do evento: ").strip()
    nome = input("Digite o nome único do evento: ").strip()
    tema_central = input("Digite o tema do evento: ").strip()
    limite = input("Digite o limite de participantes (deixe em branco se não houver): ").strip()
    limite = int(limite) if limite.isdigit() else None
    status = 'ativo' 

    sucesso = Cadastrar_evento(cod, nome, tema_central, limite, status)
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
            atualizar_evento(nome, tema_central=tema_central if tema_central else None, limite=limite, status=status if status else None)
            print("Evento atualizado com sucesso.")
        else:
            print("Evento não encontrado.")
    input("Pressione Enter para continuar...")
    clear()

def consultar_participante_por_codigo():
    codigo = input("Digite o código do participante: ").strip()
    participante = consultar_participante(codigo)
    if participante:
        print(f"Código: {participante['codigo']}")
        print(f"Nome: {participante['nome']}")
        print(f"E-mail: {participante['email']}")
        print(f"Eventos inscritos: {', '.join(participante.get('eventos', []))}")
    else:
        print("Participante não encontrado.")
    input("Pressione Enter para continuar...")
    clear()

def listar_participantes_por_evento():
    cod_evento = input("Digite o código do evento: ").strip()
    listar_participantes_por_evento(cod_evento)
    input("Pressione Enter para continuar...")

def consultar_evento_por_codigo():
    codigo = input("Digite o código do evento: ").strip()
    evento = consultar_evento(codigo)
    if evento:
        print(f"Código: {evento['cod_evento']}")
        print(f"Nome: {evento['nome']}")
        print(f"Tema Central: {evento['tema_central']}")
        print(f"Limite de Participantes: {evento.get('limite', 'Sem limite')}")
        print(f"Status: {evento['status']}")
    else:
        print("Evento não encontrado.")
    input("Pressione Enter para continuar...")
    clear()


if __name__ == "__main__":
    Menu()
