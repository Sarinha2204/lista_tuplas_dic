eventos = []

def Cadastrar_evento(nome, cod_evento, tema_central, limite, status):
    evento = {'nome': nome, 'cod_evento': cod_evento, 'tema_central': tema_central, 'limite': limite, 'status': status}
    eventos.append(evento)
    
def listar_evento():
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
    else:
        print("Lista de Eventos:")
        for i, evento in enumerate(eventos):
            print(f"{i + 1}. Nome: {evento['nome']}, Código: {evento['cod_evento']}")
def consultar_evento(cod_evento):
    for evento in eventos:
        if evento['cod_evento'] == cod_evento:
            return evento
    return None

def remover_evento(cod_evento):
    global eventos
    eventos = [e for e in eventos if e['cod_evento'] != cod_evento]
    print(f"Evento com código {cod_evento} removido com sucesso.")
    
def atualizar_evento(cod_evento, nome=None, evento=None, cpf=None):
    evento = consultar_evento(cod_evento)
    if evento:
        if nome:
            evento['nome'] = nome
        if evento:
            evento['evento'] = evento
        if cpf:
            evento['cpf'] = cpf
        print(f"Evento com código {cod_evento} atualizado com sucesso.")
    else:
        print(f"Evento com código {cod_evento} não encontrado.")

def listar_eventos_por_tema(tema_central):
    eventos_filtrados = [evento for evento in eventos if evento['tema_central'] == tema_central]
    if not eventos_filtrados:
        print(f"Nenhum evento encontrado para o tema: {tema_central}")
    else:
        print(f"Eventos encontrados para o tema '{tema_central}':")
        for evento in eventos_filtrados:
            print(f" - {evento['nome']} (Código: {evento['cod_evento']})")

def consultar_eventos_por_status(status):
    eventos_filtrados = [evento for evento in eventos if evento['status'] == status]
    if not eventos_filtrados:
        print(f"Nenhum evento encontrado com o status: {status}")
    else:
        print(f"Eventos encontrados com o status '{status}':")
        for evento in eventos_filtrados:
            print(f" - {evento['nome']} (Código: {evento['cod_evento']})")