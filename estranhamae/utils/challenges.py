import random
from .advantages import get_random_advantage
from .words import convert_to_ascii_string

challenges = [
    "Cante uma música sem se esquecer da letra.",
    "Faça uma dancinha engraçada por 30 segundos.",
    "Imite um animal de sua escolha por 1 minuto.",
    "Leia um trecho de um livro em voz alta com uma voz engraçada.",
    "Tire uma selfie com uma expressão facial engraçada.",
    "Imite um famoso por 1 minuto.",
    "Desenhe um retrato de um dos outros jogadores com os olhos fechados.",
    "Faça 20 polichinelos.",
    "Conte uma piada e faça todos rirem.",
    "Tire 5 fotos diferentes em poses engraçadas.",
    "Fale sem parar por 2 minutos sobre um assunto aleatório.",
    "Coloque um pouco de comida em uma colher e ande até um ponto específico sem deixar cair.",
    "Leia uma frase em um idioma que você não conhece.",
    "Dance como se ninguém estivesse vendo por 1 minuto.",
    "Mostre seu talento oculto.",
    "Faça uma cara de espanto e mantenha-a por 1 minuto.",
    "Realize uma imitação de um personagem famoso.",
    "Descreva uma situação fictícia e faça os outros jogadores adivinharem o que aconteceu.",
    "Crie uma história curta com 3 palavras fornecidas pelos outros jogadores.",
    "Simule uma situação de emergência e explique o que faria.",
    "Cante uma música de um filme infantil.",
    "Faça uma expressão facial com 3 emoções diferentes em 30 segundos.",
    "Crie uma coreografia para uma música popular e a execute.",
    "Encontre um objeto e faça uma apresentação de vendas para ele.",
    "Imite um ator famoso em uma cena de filme.",
    "Jogue um jogo de adivinhação com um tema escolhido por você.",
    "Ensaie um discurso de um minuto sobre um assunto aleatório.",
    "Cante no estilo de uma banda ou cantor específico.",
    "Leia uma passagem de um livro ou artigo de jornal com um sotaque diferente.",
    "Mostre um truque de mágica simples.",
    "Dance uma música famosa sem música.",
    "Faça uma entrevista fictícia com um personagem imaginário.",
    "Crie um poema de 4 linhas sobre um tema fornecido.",
    "Faça um desfile de moda improvisado.",
    "Imite um animal marinho por 1 minuto.",
    "Fale sobre um hobby seu e convide os outros a experimentarem-no.",
    "Desenhe um mapa do seu lugar favorito sem olhar.",
    "Faça uma piada usando apenas trocadilhos.",
    "Crie um jogo de palavras com um tema específico.",
    "Cante uma música enquanto faz caretas.",
    "Mostre uma habilidade ou talento único que você tem.",
    "Faça uma performance de um musical famoso.",
    "Leia uma citação inspiradora em voz alta com muita emoção.",
    "Crie um desafio físico, como pular em um pé só por 1 minuto.",
    "Realize uma imitação de um famoso de uma época antiga.",
    "Faça uma apresentação de vendas para um produto fictício.",
    "Descreva uma viagem imaginária em detalhes.",
    "Imite um super-herói e execute um de seus poderes.",
    "Faça um desenho cômico de um dos outros jogadores.",
    "Crie uma música com 3 palavras fornecidas pelos outros jogadores.",
    "Fale sobre um tema específico sem parar por 1 minuto.",
    "Simule uma situação de entrevista de emprego.",
    "Faça uma performance de um estilo musical diferente.",
    "Mostre um truque de mágica que você conhece.",
    "Demonstre um esporte ou atividade física com um objeto comum.",
    "Crie uma coreografia com uma música famosa.",
    "Imite um personagem de desenho animado.",
    "Leia um trecho de um poema em um estilo dramático.",
    "Dance uma música sem som com o ritmo que você escolher.",
    "Crie um anúncio de um produto fictício.",
    "Conte uma história curta usando apenas 5 palavras.",
    "Desenhe um retrato engraçado de um dos jogadores.",
    "Imite um personagem histórico em uma cena fictícia.",
    "Faça uma apresentação de vendas para um objeto cotidiano.",
    "Realize uma imitação de um animal exótico.",
    "Cante uma música em um idioma estrangeiro.",
    "Crie uma história com um final surpreendente.",
    "Descreva um evento imaginário como se fosse um repórter.",
    "Imite uma situação de um programa de TV popular.",
    "Dance como um robô por 1 minuto.",
    "Faça uma performance de um monólogo teatral.",
    "Crie uma coreografia de dança com uma música conhecida.",
    "Mostre um truque de habilidade com um objeto comum.",
    "Faça uma leitura dramática de uma cena de um filme.",
    "Crie um poema usando apenas 3 palavras fornecidas pelos outros jogadores.",
    "Realize uma performance de um estilo de dança diferente.",
    "Conte uma história engraçada com 3 palavras fornecidas.",
    "Imite uma cena de um filme de comédia.",
    "Desenhe algo usando apenas uma cor.",
    "Faça uma apresentação criativa de um produto fictício.",
    "Demonstre um truque de mágica simples.",
    "Crie uma dança com passos inventados.",
    "Faça uma performance dramática de um poema conhecido.",
    "Conte uma história imaginária com um tema escolhido.",
    "Imite um estilo musical famoso.",
    "Leia uma cena de um livro com emoção exagerada.",
    "Crie um anúncio engraçado para um produto inventado.",
    "Faça uma coreografia de dança usando apenas movimentos lentos.",
    "Imite um famoso em uma situação incomum.",
    "Crie uma história curta com um tema específico.",
    "Realize uma performance de um musical fictício.",
    "Demonstre uma habilidade única com um objeto do cotidiano.",
    "Imite um personagem de um filme clássico.",
    "Cante uma música em um estilo diferente do original.",
    "Desenhe um retrato com uma técnica artística diferente.",
    "Faça uma performance de um estilo de dança incomum.",
    "Crie uma apresentação dramática de um evento imaginário.",
    "Simule uma situação de um programa de variedades.",
    "Conte uma história fictícia usando apenas 5 frases.",
    "Desenhe um cenário imaginário em 2 minutos.",
    "Crie um truque de mágica com objetos comuns.",
    "Imite um personagem de um filme famoso em uma cena nova.",
    "Dance como se estivesse em um videoclipe dos anos 80.",
    "Realize uma performance de uma cena de um musical popular.",
    "Crie uma coreografia com passos improvisados.",
    "Demonstre um truque de habilidade física simples.",
    "Conte uma história engraçada com 3 palavras aleatórias.",
    "Faça uma imitação de um famoso em uma situação cotidiana.",
    "Leia um trecho de um livro com um sotaque diferente.",
    "Imite um personagem de um desenho animado em uma nova situação.",
    "Crie uma apresentação criativa de um produto inusitado.",
    "Desenhe um retrato de um dos jogadores usando uma técnica diferente.",
    "Realize uma performance dramática de uma cena de comédia.",
    "Faça uma coreografia de dança inspirada em uma cultura diferente.",
    "Imite um estilo de música que você não conhece bem.",
    "Crie uma história curta com um final inesperado.",
    "Desenhe algo usando apenas formas geométricas.",
    "Faça uma performance de um monólogo teatral improvisado.",
    "Imite um famoso em uma cena de um filme de ação.",
    "Conte uma piada usando apenas uma única palavra.",
    "Crie uma apresentação de vendas para um item imaginário.",
    "Realize uma dança inspirada em um filme popular.",
    "Descreva um evento imaginário como se fosse um repórter de TV.",
    "Cante uma música com um estilo de vocal diferente.",
    "Faça uma performance de uma cena de um programa de comédia.",
    "Imite um famoso em uma situação de um jogo de tabuleiro.",
    "Crie uma coreografia de dança com passos improvisados.",
    "Desenhe um objeto cotidiano como se fosse uma obra de arte.",
    "Conte uma história curta com um tema inusitado.",
    "Imite um personagem histórico em uma situação moderna.",
    "Faça uma apresentação criativa de um produto fictício.",
    "Realize uma performance dramática de um poema conhecido.",
    "Crie uma história fictícia usando apenas 5 palavras.",
    "Desenhe algo usando uma técnica artística incomum.",
    "Imite um estilo musical popular em uma situação nova.",
    "Faça uma coreografia de dança inspirada em uma década passada.",
    "Conte uma história engraçada com 3 palavras fornecidas.",
    "Descreva uma viagem imaginária como se fosse um diário.",
    "Imite um famoso em uma situação de um filme de suspense.",
    "Faça uma performance de uma cena de um drama popular.",
    "Crie uma apresentação criativa para um produto inventado.",
    "Desenhe um retrato de um dos jogadores com um estilo artístico diferente.",
    "Realize uma performance de um estilo de dança tradicional.",
    "Conte uma piada usando apenas expressões faciais.",
    "Imite um personagem fictício em uma nova situação.",
    "Crie uma história curta com um tema de fantasia.",
]

def choose_challenges(player, current_player):
    print(convert_to_ascii_string("Vou desafiar voce"))

    c_i = random.sample(range(len(challenges)), 2)
    print("Seus desafios são:")
    for i in c_i:
        print(challenges[i])
    advantage = get_random_advantage()
    print(f"Sua recompensa será: \n{advantage}")
    answer = input("Realizou os deafios? (s/n) ")
    if answer == "s":
        player.advantages.append(advantage)
        current_player.advantages.append(advantage)
    else:
        print(":((")
    