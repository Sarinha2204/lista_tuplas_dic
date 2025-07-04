participantes = [{'nome': 'Sara' ,'email': 'sara@gmail.com','cod_participante': 1,'preferencias_tema': ['Inteligencia artificial']},
                 {'nome': 'Raiany' ,'email': 'raiany@gmail.com','cod_participante': 2,'preferencias_tema': ['Inteligência artificial', 'Análise de Dados']},
                 {'nome': 'Luiz' ,'email': 'luiz@gmail.com','cod_participante': 3,'preferencias_tema': ['Programação', 'Robótica']}]

def Cadastrar_participante(cod, nome, email, preferencias_tema):
    participante = {
        'nome': nome,
        'email': email,
        'cod_participante': cod,
        'preferencias_tema': preferencias_tema
    }
    if consultar_participante(cod):
        return False
    else:
        participantes.append(participante)
        return True

def listar_participantes():
    if len(participantes) == 0:
        print("Nenhum participante cadastrado.")
    else:
        print("Lista de Participantes:")
        for participante in participantes:
            print(f"Código: {participante['cod_participante']}, Nome: {participante['nome']}, email: {participante['email']}, Preferências Temáticas: {participante['preferencias_tema']}")

def consultar_participante(cod_participante):
    for participante in participantes:
        if participante['cod_participante'] == cod_participante:
            return participante
    return None

def remover_participante(cod_participante):
    global participantes
    participantes = [p for p in participantes if p['cod_participante'] != cod_participante]
    print(f"Participante com código {cod_participante} removido com sucesso.")

def atualizar_participante(cod_participante, nome=None, email=None, preferencias=None):
    participante = consultar_participante(cod_participante)
    if participante:
        if nome:
            participante['nome'] = nome
        if email:
            participante['email'] = email
        if preferencias is not None:
            participante['preferencias_tema'] = preferencias
        print(f"Participante com código {cod_participante} atualizado com sucesso.")
    else:
        print(f"Participante com código {cod_participante} não encontrado.")


def listar_participantes_por_evento(cod_evento):
    try:
        cod_evento = int(cod_evento)
    except ValueError:
        print("Código do evento inválido (deve ser um número).")
        return

    participantes_filtrados = [p for p in participantes if 'eventos' in p and cod_evento in p['eventos']]

    if not participantes_filtrados:
        print(f"Nenhum participante encontrado para o evento: {cod_evento}")
    else:
        print(f"Participantes encontrados no evento '{cod_evento}':")
        for participante in participantes_filtrados:
            print(f" - (Código: {participante['cod_participante']}), {participante['nome']}")
            print(f"   E-mail: {participante['email']}")
            preferencias = participante['preferencias_tema']
            if isinstance(preferencias, list):
                print(f"   Preferências: {', '.join(preferencias)}")
            else:
                print(f"   Preferências: {preferencias}")
