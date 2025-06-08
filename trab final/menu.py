from clear import clear

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