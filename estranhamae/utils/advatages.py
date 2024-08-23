import random

advantages = [
    "Recupere a sua mãe, mas receba 2 regras dos próximos 2 jogadores.",
    "Ganhe 3 cartas.",
    "Negue imediatamente a criação de uma regra sobre você.",
    "Negue imediatamente a criação de uma regra sobre você.",
    "Negue imediatamente a criação de uma regra sobre você.",
    "Negue imediatamente a criação de uma regra sobre você.",
    "Negue imediatamente a criação de uma regra sobre você.",
    "Joga na cara do mais novo - aquele que acertou no copo deve jogar na cara do mais gordo.",
    "Troque de posição - ao jogar um minigame, você pode trocar de posição com uma pessoa acima ou uma pessoa abaixo.",
    "Crie uma regra gratuitamente.",
    "Crie uma regra gratuitamente.",
    "Crie uma regra gratuitamente.",
    "Crie uma regra gratuitamente.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ganhe 5 fichas.",
    "Ao ganhar um minigame, sua troca de fichas x cartas será 3 fichas para 1 carta.",
    "Pegue uma carta virada para baixo e receba a quantidade de fichas que representa (o 3 te dá 3, o rei de dá 13, coringa não fará nada).",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Troque a mãe de todos de lugar.",
    "Escolha um item para valer 40 fichas, fique com ele, mas outras vantagens darão a possibilidade de roubar de você.",
    "Roube qualquer item de qualquer jogador.",
    "Roube qualquer item de qualquer jogador.",
    "Roube qualquer item de qualquer jogador.",
    "Roube qualquer item de qualquer jogador.",
    "Roube qualquer item de qualquer jogador.",
    "Roube qualquer item de qualquer jogador.",
    "Roube qualquer item de qualquer jogador.",
    "Roube qualquer item de qualquer jogador.",
    "Família LGS!! Receba uma segunda mãe!!",
    "Se você for adotado, troque suas fichas por cartas (até 4 cartas).",
    "Se você for adotado, troque suas fichas por cartas (até 4 cartas).",
    "Se você for adotado, troque suas fichas por cartas (até 4 cartas).",
    "Se você for adotado, troque suas fichas por cartas (até 4 cartas).",
    "Se você for adotado, troque suas fichas por cartas (até 4 cartas).",
    "Médico!! Faça uma mãe virar pai (ele foi comprar cigarro, todas as mães representadas por aquela carta são descartadas). Essa vantagem pode fazer um pai virar mãe novamente.",
    "Use 3 fichas como munição para lançar no copo de alguém ao desafiá-lo. Devem as 3 serem lançadas ao mesmo tempo. Só aumento de chance de fazer o desafio, não deverá ser feito 3 vezes.",
    "Lambidinha dos cria - se você lamber o cotovelo de alguém sem ser percebido, roube todas as fichas que ela tiver (atitude de roubar só deve ser feita 1 rodada depois da lambida sem ser percebido).",
    "Advocacia, meu pau na sua tia - jogue um pau (ficha) de olhos vendados e tonto em alguém a sua escolha, se acertar a pessoa que gostaria, ganhe mais uma mãe.",
    "Deu mole é vapo - te dá direito a atrapalhar um jogador durante um minigame (você não pode estar jogando também - vantagem 'aliança'). ",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "Escolha um jogador para jogar um minigame de olhos vendados.",
    "CARLOS Y TU ABUELA - Escolha 2 jogadores para representarem uma avó e um galanteador mexicano na tentativa de convencer a avó para lhe dar algum dinheiro (dura o jogo todo até ser feita a transferência de pelo menos 2 cartas).",
    "CARLOS Y TU ABUELA - Escolha 2 jogadores para representarem uma avó e um galanteador mexicano na tentativa de convencer a avó para lhe dar algum dinheiro (dura o jogo todo até ser feita a transferência de pelo menos 2 cartas).",
    "CARLOS Y TU ABUELA - Escolha 2 jogadores para representarem uma avó e um galanteador mexicano na tentativa de convencer a avó para lhe dar algum dinheiro (dura o jogo todo até ser feita a transferência de pelo menos 2 cartas).",
    "CHING CHONG - prenda os olhos de outro jogador com durex para que fique 'Ching Chong' por 3 rodadas.",
    "CHING CHONG - prenda os olhos de outro jogador com durex para que fique 'Ching Chong' por 3 rodadas.",
    "Agachadinha dos cria - a cada 5 segundos na posição de cócoras, ganhe 1 ficha (até 1 minuto = 15 fichas)",
    "Agachadinha dos cria - a cada 5 segundos na posição de cócoras, ganhe 1 ficha (até 1 minuto = 15 fichas)",
    "Agachadinha dos cria - a cada 5 segundos na posição de cócoras, ganhe 1 ficha (até 1 minuto = 15 fichas)",
    "Agachadinha dos cria - a cada 5 segundos na posição de cócoras, ganhe 1 ficha (até 1 minuto = 15 fichas)",
]

def get_random_advantage():
    index = random.randint(0, len(advantages)-1)
    return advantages[index]