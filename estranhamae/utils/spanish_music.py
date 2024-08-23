import random

spanish_musics = [
    "Aserejé - Las Ketchup: A música é famosa por seu refrão incompreensível e divertido.",
    "Macarena - Los Del Río: A canção e sua coreografia são icônicas e têm um toque cômico.",
    "La Cucaracha - Tradição popular: Uma música tradicional engraçada sobre uma barata.",
    "El Baile del Perrito - Wilfrido Vargas: Uma canção com uma dança divertida que imita um cachorro.",
    "El Pollo Frito - Chico Che: A música fala de forma engraçada sobre comer frango frito.",
    "Mi Agüita Amarilla - Los Toreros Muertos: Uma música irreverente com humor ácido sobre um assunto inusitado.",
    "El Gato Volador - El Chombo: Uma canção com uma batida cativante e letras engraçadas sobre um gato voador.",
    "Teclado - Yayo: Uma paródia sobre tocar teclado de forma hilária.",
    "Me Pica el Bagre - Los Auténticos Decadentes: Uma música humorística sobre a fome.",
    "El Hombre Lobo en París - La Unión: A música mistura humor e fantasia com a ideia de um lobisomem em Paris.",
    "No Controles - Olé Olé: Uma canção pop com uma atitude divertida e desafiante.",
    "El Baile de los Gorilas - Melody: Uma música infantil com um ritmo animado e letras engraçadas.",
    "Pica Pica - La Banda del Capitán Canalla: Uma música com um ritmo acelerado e letras cômicas.",
    "Chicle de Amor - Aventura: Uma canção que mistura romance e humor de forma leve.",
    "Los Limones - El Canto del Loco: Uma música divertida sobre situações absurdas e engraçadas.",
]

def choose_random_spanish_music():
    music = ""
    music = random.randint(0,len(spanish_musics) - 1)
    return spanish_musics[music]
