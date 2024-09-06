import random

random_phrases = [
    "Parabéns, campeão! Quase fez nada!",
    "Isso aí! Tá só aquecendo, né?",
    "Melhor ter ficado dormindo, hein?",
    "Quem precisa de habilidade quando se tem azar?",
    "Sorte? Não por aqui, irmão!",
    "Parece que o talento tirou folga hoje!",
    "Essa foi pro currículo das derrotas, hein!",
    "Mestre do fail! Não é pra qualquer um.",
    "Jogou bonito... bonito pra quem tá vendo de fora!",
    "Yoloooo, se fodeooo!",
    "A habilidade mandou um abraço e falou que volta amanhã.",
    "Uma vitória por ano já tá bom, né?",
    "Tá treinando como não fazer, né?",
    "Se fosse pra errar mais, só errando duas vezes!",
    "Que desastre maravilhoso de assistir!",
    "Se tivesse um prêmio pra pior jogada... seria seu!",
    "Mandou muito mal, parabéns!",
    "Vai dar aula de erro depois dessa, certeza!",
    "Esqueceu de ligar o modo pro player?",
    "Essa foi digna de um tutorial: 'Como perder com estilo'.",
    "O azar te abraçou com força dessa vez!",
    "Se continuar assim, vira coach de fracasso.",
    "Nem precisa tentar de novo, o erro foi perfeito!",
    "Essa jogada... só orgulhou sua mãe... ou não.",
    "Sua habilidade tá de férias ou só foi passear?",
    "A próxima você acerta... ou erra com ainda mais classe!",
    "Erro épico! Só quem é mestre consegue.",
    "Se fosse um campeonato de erros, já era campeão!",
    "Hoje não é seu dia... nem sua semana... nem seu mês!",
    "Opa, passou perto... do completo desastre!"
]

def choose_random_phrase():
    random_ind = random.randint(0, len(random_phrases))
    return random_phrases[random_ind]