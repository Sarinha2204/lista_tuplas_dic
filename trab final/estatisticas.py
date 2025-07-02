from collections import Counter
from participante import participantes 

estatisticas = []

def temas_frequentes(eventos):
    print("\nTemas mais frequentes:")
    temas = [evento['tema_central'] for evento in eventos]
    if not temas:
        print("Nenhum evento cadastrado.")
        return

    contagem = Counter(temas)
    mais_comum = contagem.most_common()

    max_freq = mais_comum[0][1]
    temas_top = [tema for tema, freq in mais_comum if freq == max_freq]

    for tema in temas_top:
        print(f"- {tema} ({max_freq} ocorrências)")


def participantes_mais_ativos():
    print("\nParticipantes mais ativos:")
    mais_eventos = 0
    ativos = []

    for p in participantes:
        eventos_inscritos = p.get('eventos', [])
        qtd = len(eventos_inscritos)
        if qtd > mais_eventos:
            mais_eventos = qtd
            ativos = [p]
        elif qtd == mais_eventos:
            ativos.append(p)

    if mais_eventos == 0:
        print("Nenhum participante está inscrito em eventos.")
    else:
        print(f"Participante(s) com {mais_eventos} evento(s):")
        for p in ativos:
            print(f"- {p['nome']} (Código: {p['cod_participante']})")