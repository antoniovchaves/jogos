import random
from utils import there_goes
from utils import spanish_music
from utils import challenges
from utils import validator
from utils import minigames
from entity import ability
from entity import mae
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
    print(f"É a vez de {player.name}.")
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
    print(f"Habilidade Secreta: {info['secret_ability'][1][0]} - {info['secret_ability'][1][1]}\n")
    input("Aperte Enter para esconder essas informações...")
    clear_terminal()
    display_turn_info(player)

def handle_rules(players):
    """Função para realizar a criação de regra ('REGRINHA NOVA, CHAMA')"""
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

def handle_advantages(player):
    """Função para realizar uso de vantagens"""
    if len(player.advantages) > 0:
        for i, advantage in enumerate(player.advantages):
            print(f"{i + 1} - {advantage}")
        chosen_advantage = int(input("Escolha a vantagem a ser utilizada: ") or "-1")
        if chosen_advantage > 0:
            player.advantages.pop(chosen_advantage-1)
    else:
        input("Sem vantagens disponíveis...")
    
def handle_there_goes():
    input("É HORA DO LÁ VAI O TAPÃO!!!!\n\nO vencedor desse jogo ganha 2 fichas e o perdedor bebe um shot a escolha do início da partida.\n\nO objetivo desta brincadeira é para seleção de um segundo minigame.\n\n:))\n\n")
    chosen_game = "-1"
    while chosen_game not in validator.validate_chosen_game:
        chosen_game = input("Qual foi o jogo selecionado? (1-10 e JQK)")
    
    there_goes.select_there_goes_game(chosen_game)

    if chosen_game != "0":
        input("Esperando resultado...")

        print("O perdedor deve receber um bigode num lugar no corpo desenhado com caneta. \n")
        answer = input("Há alguém com o 3o bigode desenhado? (s/n) ")
        if answer == "s":
            music = spanish_music.choose_random_spanish_music()
            input(f"\n\nQuem recebeu o terceiro bigode, deve fazer uma dança na dança mais espanhol quanto possível para a música:\n\n{music}")
    
def handle_coin_in(current_player, players):
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
        print("yolo, se fodeo...")
    
def handle_minigame_bet(players):
    minigame_type = input("Qual foi o tipo de minigame?\n- moedas (1)\n- cada um por si (2)\n- duplasquinha (3)\n- covardia 3 contra 1 (4)\nInsira aqui: ")
    minigames.minigame_points(players, minigame_type)

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

def clear_terminal():
    """Função para limpar o terminal (simplesmente imprime várias linhas em branco)"""
    print("\n" * 100)

def game_over(players):
    """Função para verificar se o jogo acabou (Placeholder)"""
    # Adicionar lógica do fim de jogo, por exemplo, quando um jogador ganha ou atinge um critério específico
    return False

def main():
    # Passo 1: Menu inicial para nomear jogadores
    players = create_players()

    # Passo 2: Distribuir mães e habilidades
    distribute_mothers(players)
    distribute_abilities(players)

    surprise_there_goes = random.sample(range(len(players), 20*len(players)), 6)
    current_people_turn_count = 0
    rule_price = 3

    # Passo 3: Loop principal do jogo
    while not game_over(players):
        if current_people_turn_count in surprise_there_goes:
            handle_there_goes()
        current_player = next_player_in_queue(players)
        display_turn_info(current_player, rule_price)
        passed = False
        rule_created = False
        # Exibir opções para o jogador
        while not passed:
            action = get_player_action()
            if action == "0":
                show_secret_player_info(current_player)
            elif action == "minhas informações" or action == "1":
                show_player_info(current_player)
            elif (action == "criar regra" or action == "2" and not rule_created):
                handle_rules(players)
                rule_price += 1
                rule_created = True
            elif action == "usar vantagem" or action == "3":
                handle_advantages(current_player)
            elif action == "minigame de apostas" or action == "4":
                handle_minigame_bet(players)
            elif action == "passar a vez" or action == "5" or action == "":
                handle_coin_in(current_player, players)
                pass_turn()
                passed = True

        current_people_turn_count += 1
        
        clear_terminal()

if __name__ == "__main__":
    main()
