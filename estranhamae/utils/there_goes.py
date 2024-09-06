from .words import generate_mimic_challenge, convert_to_ascii_string
from .validator import validate_chosen_game
from .spanish_music import choose_random_spanish_music

validate_chosen_game = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

there_goes = {
    "0":"""AH CANSARAM DO TAPÃO DOS CRIA FIOS DA TRUTA DO CARAIO TOMA NUCÓ""",
    "1" : f"""
{convert_to_ascii_string("Jogo Batata Quente com timer de 15s.")}

O jogo será jogado de pé em um espaço que não seja possível quebrar nada. 
O jogo termina com o toque do alarme, o celular deve ser colocado virado para baixo para ninguém saber o tempo.

Boa sorte!!
""",
    "2" : f"""
{convert_to_ascii_string("Jogo da confusão")}
                
Esse jogo é descrito por ter o objetivo de responder toda e qualquer pergunta com outra pergunta. 
Aquele incapaz de fazê-lo, perde.

Boa sorte!!
""",
    "3" : f"""
{convert_to_ascii_string("Jogo de escolher o jogo")}
                  
Normalmente usado para escolher a modalidade do jogo, hoje, o jogo de escolher o jogo será usado apenas como jogo.
Aquele que tiver a maior carta da mesa, vence.

Boa sorte!!
""", 
    "4" : f"""
{convert_to_ascii_string("Jogo do pão.........")}
                  
Aqueles que se recusarem a jogar, perdem..

Triste :((
""" , 
    "5" : f"""
{convert_to_ascii_string("Jogo 'S-C-Composto'")}
                  
Cada participante deve falar uma palavra relacionada com a última dita.
Não devem ser usadas palavras iniciadas em S, C, ou palavras compostas.
Aquele incapaz de fazê-lo, perde.

Boa sorte!!
""",
    "6" : f"""
{convert_to_ascii_string("Jogo da Feira")}
                
Cada jogador deve ir a feira comprar algo, os jogadores por conseguintes devem lembrar de todos os itens na lista de compras e adicionar o que comprou sem haver repetição.
Aquele incapaz de fazê-lo, perde.

Boa sorte!!
""",
    "7" : f"""
{convert_to_ascii_string("Jogo Adedanha de Mães")}
                
Será jogado o Adedanha convencional, mas apenas nomes de mulheres que tem cara de mãe serão aceitos.
Aquele que escolher um nome de pessoa jovem demais para o cargo, perde.

Boa sorte!!
""",
    "8" : f"""
{convert_to_ascii_string("Jogo Lá vai o Ganso")}
                
Versão comum do jogo Lá vai o Tapão.
Aquele que se perder de vez onde foi parar o ganso, perde.

Boa sorte!!
""",
    "9" : f"""
{convert_to_ascii_string("Jogo Musical")}
                
Crie uma rima esculachando o filha da puta do teu lado, ele ta doido pra comer sua mãe e você não tem falado nada.
Aquele incapaz de defender a própria mãe vai misturar o que tiver no copo com cerveja pra aprender a ser igual ao pai, se não pode protegê-la, desce a mão nela.

Boa sorte!!
""",
    "10": f"""
{convert_to_ascii_string("Jogo Referência")}
                
Cada participante deverá fazer referência a um programa (qualquer meio de entretenimento) que todos os participantes reconheçam.
Aquele incapaz de fazê-lo, perde.

Boa sorte!!
""",
    "J" : f"""
{convert_to_ascii_string("Jogo do pão.........")}
                  
Aqueles que se recusarem a jogar, perdem..

Triste :((
""",
    "Q" : f"""
{convert_to_ascii_string("Mímica!! Ebaaaaaa")}
                
Aquele que venceu o jogo 'Lá vai o Tapão' fará a mímica. 
A mímica será escolhida pelo sistema, serão palavras aleatórias. 
Restrição:
    - Não pode mexer a boca
    - Não pode apontar
    - Não podem ser usados objetos da casa
Terão de 2 a 4 palavras cada mímica, cada mímica deve ser feita para um palavra por vez.
A cada palavra, terá um participante que acerta e estará livre da próxima palavra.
Aqueles que não acertarem nenhuma palavra, perdem.

Boa sorte!!
""",
    "K" : f"""
{convert_to_ascii_string("Jogo 'S-C-Composto' EXTREEEEEEEEEME")}
                
Cada participante deve falar uma palavra relacionada com a última dita.
Não devem ser usadas palavras com S, C, ou palavras compostas.
Aquele incapaz de fazê-lo, perde.

Boa sorte!!
"""
}

def select_there_goes_game(card):
    input(there_goes[card])
    if card == "Q":
        l_mimic = generate_mimic_challenge()
        print("Mostre essa tela apenas para quem fará a mimica!\n\nDeve ser jogado até todas as palavras serem acertadas!!!")
        input()
        for i, mimic in enumerate(l_mimic):
            input(f"{i + 1} - {mimic}")

def handle_there_goes():
    print(convert_to_ascii_string("Lá vai o tapão"))

    input("É HORA DO LÁ VAI O TAPÃO!!!!\n\nO vencedor desse jogo ganha 2 fichas e o perdedor bebe um shot a escolha do início da partida.\n\nO objetivo desta brincadeira é para seleção de um segundo minigame.\n\n:))\n\n")
    chosen_game = "-1"
    while chosen_game not in validate_chosen_game:
        chosen_game = input("Qual foi o jogo selecionado? (1-10 e JQK)")
    
    select_there_goes_game(chosen_game)

    if chosen_game != "0":
        input("Esperando resultado...")

        print("O perdedor deve receber um bigode num lugar no corpo desenhado com caneta. \n")
        answer = input("Há alguém com o 3o bigode desenhado? (s/n) ")
        if answer == "s":
            music = choose_random_spanish_music()
            input(f"\n\nQuem recebeu o terceiro bigode, deve fazer uma dança na dança mais espanhol quanto possível para a música:\n\n{music}")
