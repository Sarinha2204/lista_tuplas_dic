participantes = []

def Cadastrar_participante(cod, nome, email):
    participante = {'nome': nome, 'email': email, 'cod_participante': cod}
    if consultar_participante(cod):  # Verifica se o código já existe
        print(f"Participante com código {cod} já cadastrado.")
    else:
        participantes.append(participante)  # Adiciona apenas se o código for novo
        print(f"Participante {nome} cadastrado com sucesso!")


def listar_participantes():
    if len(participantes) == 0:
        print("Nenhum participante cadastrado.")
    else:
        print("Lista de Participantes:")
        for i, participante in enumerate(participantes):
            print(f"{i + 1}. Código: {participante['cod_participante']}, Nome: {participante['nome']}, email: {participante['email']}")

def consultar_participante(cod_participante):
    for participante in participantes:
        if participante['cod_participante'] == cod_participante:
            return participante
    return None

def remover_participante(cod_participante):
    global participantes
    participantes = [p for p in participantes if p['cod_participante'] != cod_participante]
    print(f"Participante com código {cod_participante} removido com sucesso.")

def atualizar_participante(cod_participante, nome=None, evento=None, cpf=None):
    participante = consultar_participante(cod_participante)
    if participante:
        if nome:
            participante['nome'] = nome
        if evento:
            participante['evento'] = evento
        if cpf:
            participante['cpf'] = cpf
        print(f"Participante com código {cod_participante} atualizado com sucesso.")
    else:
        print(f"Participante com código {cod_participante} não encontrado.")

def listar_participantes_por_evento(evento):
    participantes_filtrados = [p for p in participantes if p['evento'] == evento]
    if not participantes_filtrados:
        print(f"Nenhum participante encontrado para o evento: {evento}")
    else:
        print(f"Participantes encontrados para o evento '{evento}':")
        for participante in participantes_filtrados:
            print(f" - {participante['nome']} (Código: {participante['cod_participante']})")
            