eventos = []

def Cadastrar_evento(nome, evento, cpf):
    evento = {'nome': nome, 'evento': evento, 'cpf': cpf}
    eventos.append(evento)
    
def listar_evento():
    if len(eventos) == 0:
        print("Nenhum participante cadastrado.")
    else:
        print("Lista de Eventos:")
        for i, evento in enumerate(eventos):
            print(f"{i + 1}. Nome: {evento['nome']}, Matrícula: {evento['matricula']}, Notas: {', '.join(map(str, evento['notas']))}")
def consultar_evento(matricula):
    for evento in eventos:
        if evento['matricula'] == matricula:
            return evento
    return None
