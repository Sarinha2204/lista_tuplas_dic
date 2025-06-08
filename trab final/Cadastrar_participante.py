participantes = []

def Cadastrar_participante(nome, evento, cpf):
    participante = {'nome': nome, 'evento': evento, 'cpf': cpf}
    participantes.append(participante)
    
def listar_participantes():
    if len(participantes) == 0:
        print("Nenhum participante cadastrado.")
    else:
        print("Lista de Participantes:")
        for i, participante in enumerate(participantes):
            print(f"{i + 1}. Nome: {participante['nome']}, Matrícula: {participante['matricula']}, Notas: {', '.join(map(str, participante['notas']))}")
def consultar_participante(matricula):
    
    
    for participante in participantes:
        if participante['matricula'] == matricula:
            return participante
    return None