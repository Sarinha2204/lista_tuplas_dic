eventos = []

def Cadastrar_evento(nome, cod_evento, tema_central, limite, status, data_evento):
    evento = {'nome': nome, 'cod_evento': cod_evento, 'tema_central': tema_central, 'limite': limite, 'status': status, 'data_evento': data_evento}
    if consultar_evento(cod_evento):
        return False
    else:
        eventos.append(evento)
        return True
    
def listar_evento():
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
    else:
        print("Lista de Eventos:")
        for evento in eventos:
            print(f" Código: {evento['cod_evento']}, Nome: {evento['nome']}, Tema Central: {evento['tema_central']}, Data de Realização do Evento: {evento['data_evento']}")
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


def cadastrar_participante_em_evento(cod_evento, cod_participante):
    print('           Cadastrar Participante em Evento           ')
    cod_evento = input("Digite o código do evento: ").strip()
    cod_participante = input("Digite o código do participante: ").strip()
    
    sucesso = cadastrar_participante_em_evento(cod_evento, cod_participante)
    
    if sucesso:
        print(f"Participante com código {cod_participante} cadastrado no evento {cod_evento} com sucesso!")
    
    input("Pressione Enter para continuar...")