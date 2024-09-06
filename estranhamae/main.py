import random

from utils import words
from utils import minigames
from utils import there_goes
from utils import challenges
from utils import advantages
from utils import random_ways_to_make_fun_of_someone

from entity import mae
from entity import ability

from entity.player import Player

def create_players():
    """Função para criar os jogadores e permitir nomeá-los"""
    players = []
    num_players = int(input("Quantos jogadores no total (presenciais e online)? "))

    for i in range(num_players):
        name = input(f"Digite o nome do jogador {i+1}: ")
        online = input("Este jogador está online? (s/n): ").lower() == 's'
        players.append(Player(name, online))
    
    return players

def distribute_mothers(players):
    """Função para distribuir as mães para cada jogador"""
    for player in players:
        numero_carta = random.randint(1, 13)
        player.mae = mae.choose_mae(numero_carta)
        player.mae_number = numero_carta

def distribute_abilities(players):
    """Função para distribuir habilidades para cada jogador"""
    for player in players:
        player.abilities = ability.choose_abilities()

def next_player_in_queue(players):
    """Função que retorna o próximo jogador na fila"""
    current_player = players.pop(0)
    players.append(current_player)
    return current_player

def display_turn_info(player, price=5):
    """Função para exibir de quem é a vez"""
    print(words.convert_to_ascii_string(f"É a vez de {player.name}."))
    print("\n\n\n")
    display_remaining_rule_time(player)
    print(f"Opções disponíveis: \n- minhas informações (1)\n- criar uma regra, custa {price} (2)\n- usar vantagem (3)\n- minigame de apostas (4)\n- passar a vez (5)")

def get_player_action():
    """Função para obter a ação do jogador"""
    return input("Escolha sua ação: ").strip().lower()

def show_player_info(player):
    """Função para mostrar as informações do jogador"""
    print(player)
    input("Aperte Enter para continuar...")

def show_secret_player_info(player):
    """Função para mostrar as informações do jogador"""
    info = player.reveal_secret_info()
    print(f"Mãe: {info['mae_number']}\n")
    print(f"Habilidade Secreta: {info['secret_ability']['secret'][0]} - {info['secret_ability']['secret'][1]}\n")
    input("Aperte Enter para esconder essas informações...")

def handle_rules(players):
    """Função para realizar a criação de regra ('REGRINHA NOVA, CHAMA')"""
    print(words.convert_to_ascii_string("Regrinha dos cria"))

    # Exemplo básico de troca de mães com outro jogador aleatório
    new_rule = input("Insira uma nova regra: ")
    if new_rule != "0":
        for player in players:
            print(f"- {player.name}")
        target = input("Insira nome do jogador alvo: ")
        turns = random.randint(1,3)
        for player in players:
            if target == player.name:
                player.rules.append([new_rule, turns])
        print(f"{target} vai sofrer por {turns} rodadas")
    input("Aperte Enter para continuar...")

def handle_coin_in(current_player, players):
    print(words.convert_to_ascii_string("saideira da rodada"))
    print("\n\n\n")

    coin_in = input("Jogue uma ficha no copo do cria!! Acertou??? (s/n)")

    if coin_in == "s":
        for player in players:
            if player.name != current_player.name:
                print(f"- {player.name}")
        selected_player = input("Quem foi desafiado?")
        for player in players:
            if player.name == selected_player:
                challenges.choose_challenges(player, current_player)
    else:
        random_phrase = random_ways_to_make_fun_of_someone.choose_random_phrase()
        print(random_phrase)

def display_remaining_rule_time(player):
    rules = []
    for rule in player.rules:
        print(rule)
        turns_left = int(rule[1]) - 1
        if rule[1] == 0:
            print(f"A regra '{rule[0]}' foi removida.")
        else: 
            print(f"Faltam {turns_left} rodadas para a regra '{rule[0]}' acabar.")
            rules.append([rule[0], turns_left])
    player.rules = rules

def pass_turn():
    """Função para passar a vez"""
    print("Você passou a vez.")
    input("Aperte Enter para continuar...")

def game_over(current_people_turn_count, game_size):
    """Função para verificar se o jogo acabou (Placeholder)"""
    # Adicionar lógica do fim de jogo, por exemplo, quando um jogador ganha ou atinge um critério específico
    if current_people_turn_count >= game_size:
        return True
    return False

def main():
    # Passo 1: Menu inicial para nomear jogadores
    players = create_players()

    # Passo 2: Distribuir mães e habilidades
    distribute_mothers(players)
    distribute_abilities(players)

    # Passo 2.5: Inicializador de variáveis necessárias
    n_players = len(players)
    game_size = int(input("Quantas rodadas querem jogar???") or "20") * n_players 
    random_there_goes_turns = int(game_size * 0.4)
    surprise_there_goes = random.sample(range(n_players, game_size), random_there_goes_turns)
    current_people_turn_count = 0
    rule_price = 3

    # Passo 3: Loop principal do jogo
    while not game_over(current_people_turn_count, game_size):

        # Verifica se é uma rodada de Lá vai o Tapão
        if current_people_turn_count in surprise_there_goes:
            there_goes.handle_there_goes()

        # Inicia variáveis para a rodada atual
        current_player = next_player_in_queue(players)
        passed = False
        rule_created = False

        # Exibir opções para o jogador
        while not passed:
            display_turn_info(current_player, rule_price)
            action = get_player_action()
            words.clear_terminal()

            # Mostra informações exclusivas para o jogador
            if action == "0":
                show_secret_player_info(current_player)

            # Exibe informações gerais do jogador
            elif action == "minhas informações" or action == "1":
                show_player_info(current_player)

            # Cria uma nova regra direcionada para um jogador - pode ser para si mesmo
            elif (action == "criar regra" or action == "2" and not rule_created):
                handle_rules(players)
                rule_price += 1
                rule_created = True

            # Exibe e faz com que o jogador use uma vantagem listada
            elif action == "usar vantagem" or action == "3":
                advantages.handle_advantages(current_player)

            # Chama um minigame no Mario Party ou qualquer outra forma de entretenimento para 4 jogadores
            elif action == "minigame de apostas" or action == "4":
                minigames.handle_minigame_bet(players)

            # Passa a vez e regula o jogo de ficha em um copo
            elif action == "passar a vez" or action == "5" or action == "":
                handle_coin_in(current_player, players)
                pass_turn()
                passed = True

            words.clear_terminal()
            
        # Aumenta contador de rodadas por pessoa
        current_people_turn_count += 1
        
        words.clear_terminal()

if __name__ == "__main__":
    main()
