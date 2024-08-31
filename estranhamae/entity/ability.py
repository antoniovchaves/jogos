import random

# Dicionário com as habilidades e suas descrições
abilities = {
    "Espião": "Permite ver a mãe de um oponente antes de atacar.",
    "Furtividade": "Pode atacar duas vezes em um turno.",
    "Infiltrador": "Ignora uma defesa do oponente ao tentar pegar a mãe.",
    "Ladrão de Cartas": "Rouba uma carta de outro jogador.",
    "Destruidor de Esconderijos": "Escolhe dois jogadores ao atacar. Só leve uma mãe se ganhar.",
    "Manipulador": "Força um jogador a descartar uma carta.",
    "Espião Aprimorado": "Veja as habilidades secretas de um jogador.",
    "Caçador de Mães": "Ao errar o roubo, recebe uma ficha de consolo.",
    "Batedor": "Se o ataque falhar, ganha um bônus de +2 fichas no próximo ataque.",
    "Trinca Cartas": "Permite trocar 3 cartas por 35 fichas.",
    "Escudo Protetor": "Protege sua mãe de dois ataques consecutivos.",
    "Ilusionista": "Move sua mãe para um novo esconderijo após uma tentativa de ataque bem-sucedida.",
    "Defesa Dupla": "Pode defender duas vezes em um turno.",
    "Troca de Lugar": "Troca a mãe com outro jogador de forma aleatória.",
    "Escudo Temporal": "Protege sua mãe por duas rodadas. Não será possível roubar sua mãe.",
    "Barreira Espelhada": "Se defendido com sucesso, o atacante perde 2 fichas.",
    "Camuflagem": "Escolha dois esconderijos ao esconder sua mãe. Troque todas as 3 mães envolvidas de lugar.",
    "Bunker": "Sua mãe não pode ser trocada por fichas até o final dao jogo.",
    "Disfarce": "Escolha outro jogador para receber o ataque no seu lugar. Deve gastar 5 fichas para isso.",
    "Esconda-se Bem": "Pode esconder a mãe novamente depois de vencer um embate.",
    "Troca Rápida": "Permite trocar fichas por cartas a uma taxa reduzida. Ganhe 2 fichas a mais do que o normal.",
    "Mercador": "Ganhe 2 fichas adicionais por cada transação feita. Isso inclui conversão para carta",
    "Corretor de Mães": "Permite vender a mãe de outro jogador por 5 fichas.",
    "Investidor": "Dobre o número de fichas recebidas ao final da rodada.",
    "Mercenário": "Pague 10 fichas para forçar um jogador a mostrar sua habilidade secreta.",
    "Desconto": "Todas as ações que custam fichas têm um desconto de 2 fichas.",
    "Leilão de Mães": "Organiza um leilão de mães entre os jogadores. Apenas usado na 8a rodada.",
    "Empresário": "Converta cartas em fichas a uma taxa aumentada. Uma carta extra por rodada ao feita a troca.",
    "Banca Roubada": "Ganhe fichas adicionais (1-10) ao ganhar uma mãe em um ataque bem-sucedido.",
    "Jogada de Mestre": "Ganhe uma ação extra por cada 5 fichas gastas em uma rodada."
}


def choose_abilities():
    selected = random.sample(list(abilities.items()), 2)
    # Remove as habilidades escolhidas do dicionário principal
    formation = {}

    for i, ability in enumerate(selected):
        if i == 0:
            formation["revealed"] = ability
        if i == 1:
            formation["secret"] = ability
        del abilities[ability[0]]
    return formation
