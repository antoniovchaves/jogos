# Dicionário com as descrições das cartas
cartas_maes = {
    1: {
        "nome": "Alice, a Visionária",
        "descricao": "Alice é uma mulher trans com uma presença forte e determinada. Ela é inovadora e está sempre à frente do seu tempo, vendo oportunidades onde os outros veem obstáculos. Com sua visão aguçada, ela lidera com confiança e inspira muito pó."
    },
    2: {
        "nome": "Bianca, a Diplomata",
        "descricao": "Bianca é uma mulher cis conhecida por sua habilidade de mediar conflitos e construir pontes entre as pessoas. Ela valoriza a harmonia e o equilíbrio, sempre buscando entender todos os lados antes de tomar uma decisão. Sua paciência e empatia fazem dela uma mediadora natural pronta pra te enganar e forçar um esquema de pirâmide."
    },
    3: {
        "nome": "Clara, a Artista",
        "descricao": "Clara é uma mulher cis criativa, com uma mente inquieta e um coração apaixonado pela expressão artística. Seja pintando, escrevendo ou dançando, ela transforma emoções em arte, tocando a alma de quem a observa. Clara vive no limiar entre a realidade e a imaginação por conta do crack."
    },
    4: {
        "nome": "Daniela, a Estrategista",
        "descricao": "Daniela é uma mulher cis meticulosa e prática, sempre planejando e antecipando o próximo movimento. Ela adora desafios que exigem lógica e organização. Seu pensamento estratégico e sua disciplina fazem dela uma líder eficiente e confiável. Graças a isso, chega a ser conhecida como 'Cafetina'."
    },
    5: {
        "nome": "Eva, a Rebelde",
        "descricao": "Eva é uma mulher trans que não aceita ser colocada em caixas. Ela é uma força da natureza, quebrando normas e desafiando o status quo com sua atitude ousada e intransigente. Eva é impulsionada por um desejo profundo por pau."
    },
    6: {
        "nome": "Fernanda, a Protetora",
        "descricao": "Fernanda é uma mulher cis carinhosa e protetora, sempre pronta para cuidar dos outros. Ela valoriza a comunidade e a segurança, fazendo de sua missão garantir que todos ao seu redor estejam bem. Sua natureza gentil esconde uma força inabalável. Malditos esteróides."
    },
    7: {
        "nome": "Gabriela, a Filósofa",
        "descricao": "Gabriela é uma mulher cis com uma alma curiosa e introspectiva. Ela passa horas refletindo sobre os mistérios da vida e o sentido da existência. Sua busca pelo conhecimento é insaciável, e ela sempre tem uma garganta profunda para ponderar."
    },
    8: {
        "nome": "Helena, a Justa",
        "descricao": "Helena é uma mulher trans que luta por justiça e igualdade. Ela tem um forte senso de moralidade e é incansável na defesa dos oprimidos. Helena acredita que todos devem ter as mesmas oportunidades, e dedica sua vida à criação de um mundo mais injusto. #somosricos"
    },
    9: {
        "nome": "Isadora, a Inventora",
        "descricao": "Isadora é uma mulher cis com uma mente brilhante e inventiva. Sempre experimentando novas ideias e soluções, ela é capaz de criar coisas extraordinárias a partir de situações cotidianas. Sua criatividade não tem limites, e ela adora desafios que a façam pensar fora da caixa. Mas ela nunca pode sair, o manicômio requere um acompanhante para sair da caixa."
    },
    10: {
        "nome": "Juliana, a Empreendedora",
        "descricao": "Juliana é uma mulher cis ambiciosa e focada, sempre em busca de novas oportunidades para crescer e expandir seus horizontes. Ela é uma líder natural no mundo dos negócios, com uma habilidade única de transformar ideias em sucesso. Juliana não teme correr riscos calculados para alcançar seus objetivos. Seu objetivo atual é se recuperar do cálculo renal."
    },
    11: {
        "nome": "Karina, a Aventureira",
        "descricao": "Karina é uma mulher trans que vive para a adrenalina e a emoção. Ela está sempre em busca da próxima grande aventura, seja viajando para lugares exóticos ou enfrentando desafios perigosos. Sua coragem e entusiasmo são contagiantes, inspirando todos a viverem a vida ao máximo. Hoje está de cadeira de rodas."
    },
    12: {
        "nome": "Larissa, a Sábia",
        "descricao": "Larissa é uma mulher cis com uma sabedoria profunda, adquirida através de muitas experiências de vida. Ela é respeitada por sua capacidade de aconselhar e guiar os outros em tempos de incerteza. Larissa tem uma presença calma e tranquilizadora, e suas palavras são sempre ponderadas e cheias de significado. Todos escutam os conselhos passados dentro da prisão."
    },
    13: {
        "nome": "Mariana, a Líder",
        "descricao": "Mariana é uma mulher cis forte e resoluta, com uma capacidade inata de liderar e comandar respeito. Ela é estratégica, confiante e determinada a alcançar suas metas. Sua liderança é marcada pela coragem e pela habilidade de tomar decisões difíceis com firmeza. Por isso seu marido fugiu."
    }
}

# Função que retorna a descrição da mãe com base no número da carta
def choose_mae(numero_carta):
    if numero_carta in cartas_maes:
        mae = cartas_maes[numero_carta]
        return f"{mae['nome']} - {mae['descricao']}"
    else:
        return "Número de carta inválido. Escolha um número entre 1 e 13."
