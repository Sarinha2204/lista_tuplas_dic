from participante import consultar_participante

eventos = [{'nome': 'Programando Inteligência Artificial', 'cod_evento': 1, 'tema_central': 'Inteligência Artificial','tipo_evento': 'palestra', 'limite': 50, 'status': 'ativo', 'data_evento': '10/10/2025'},
           {'nome': 'Linguagem de Marcação através de Inteligência Artificial', 'cod_evento': 2, 'tema_central': 'Inteligência Artificial','tipo_evento': 'WorskShop', 'limite': 25, 'status': 'ativo', 'data_evento': '22/07/2025'},
           {'nome': 'Como fazer a programação na Robótica', 'cod_evento': 3, 'tema_central': 'Inteligência Artificial','tipo_evento': 'WorskShop', 'limite': 25, 'status': 'ativo', 'data_evento': '22/07/2025'}
]

def Cadastrar_evento(nome, cod_evento, tema_central, tipo_evento, limite, status, data_evento):
    evento = {'nome': nome, 'cod_evento': cod_evento, 'tema_central': tema_central,'tipo_evento': tipo_evento, 'limite': limite, 'status': status, 'data_evento': data_evento}
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
    
def atualizar_evento(cod_evento, nome=None, tema_central=None, tipo_evento=None, limite=None, status=None, data_evento=None):
    evento = consultar_evento(cod_evento)
    if not evento:
        print(f"Evento com código {cod_evento} não encontrado.")
        return

    if nome:
        evento['nome'] = nome
    if tema_central:
        evento['tema_central'] = tema_central
    if tipo_evento:
        evento['tipo_evento'] = tipo_evento
    if limite is not None:
        evento['limite'] = limite
    if status:
        evento['status'] = status
    if data_evento:
        evento['data_evento'] = data_evento

    print(f"Evento '{evento['nome']}' atualizado com sucesso.")


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


def cadastrar_participante_em_evento():
    print('           Cadastrar Participante em Evento           ')

    cod_evento_input = input("Digite o código do evento: ").strip()
    cod_participante_input = input("Digite o código do participante: ").strip()

    if not cod_evento_input.isdigit() or not cod_participante_input.isdigit():
        print("Código inválido! Ambos devem ser números.")
        return False

    cod_evento = int(cod_evento_input)
    cod_participante = int(cod_participante_input)
    
    evento = consultar_evento(cod_evento)
    participante = consultar_participante(cod_participante)

    if not evento or not participante:
        print("Evento ou participante não encontrado.")
        return False

    if 'participantes' not in evento:
        evento['participantes'] = []
    if cod_participante not in evento['participantes']:
        evento['participantes'].append(cod_participante)

    if 'eventos' not in participante:
        participante['eventos'] = []
    if cod_evento not in participante['eventos']:
        participante['eventos'].append(cod_evento)

    print("Participante cadastrado no evento com sucesso.")
    return True
