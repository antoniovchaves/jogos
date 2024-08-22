import random
from utils import there_goes
from utils import spanish_music
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

def distribute_abilities(players):
    """Função para distribuir habilidades para cada jogador"""
    for player in players:
        player.abilities = ability.choose_abilities()

def next_player_in_queue(players):
    """Função que retorna o próximo jogador na fila"""
    current_player = players.pop(0)
    players.append(current_player)
    return current_player

def display_turn_info(player):
    """Função para exibir de quem é a vez"""
    print(f"É a vez de {player.name}.")
    display_remaining_rule_time(player)
    print("Opções disponíveis: \nminhas informações(1)\nexchange dos cria(2)\nusar vantagem(3)\npassar a vez(4)")

def get_player_action():
    """Função para obter a ação do jogador"""
    return input("Escolha sua ação: ").strip().lower()

def show_player_info(player):
    """Função para mostrar as informações do jogador"""
    info = player.reveal_info()
    print(f"Nome: {info['name']}\n")
    print(f"Mãe: {info['mae']}\n")
    print(f"Habilidade Revelada: {info['abilities'][0][0]} - {info['abilities'][0][1]}\n")
    print(f"Habilidade Escondida: {info['abilities'][1][0]} - {info['abilities'][1][1]}\n")
    print("Aperte Enter para continuar...")
    input()
    clear_terminal()

def handle_rules(players):
    """Função para realizar a criação de regra ('REGRINHA NOVA, CHAMA')"""
    # Exemplo básico de troca de mães com outro jogador aleatório
    new_rule = input("Insira uma nova regra: ")
    for player in players:
        print(f"- {player.name}")
    target = input("Insira nome do jogador alvo: ")
    turns = random.randint(1,3)
    for player in players:
        if target == player.name:
            player.rules += [new_rule, turns]
    print(f"{target} vai sofrer por {turns} rodadas")
    print("Aperte Enter para continuar...")
    input()
    clear_terminal()

def handle_advantages(player):
    """Função para realizar uso de vantagens"""
    for advantage, i in enumerate(player.advantages):
        print(f"{i + 1} - {advantage}")
    chosen_advantage = int(input("Escolha a vantagem a ser utilizada: "))
    player.advantages.pop(chosen_advantage-1)
    
def handle_there_goes(players):
    print("É HORA DO LÁ VAI O TAPÃO!!!!\n\nO vencedor desse jogo ganha 2 fichas e o perdedor bebe um shot a escolha do início da partida.\n\nO objetivo desta brincadeira é para seleção de um segundo minigame.\n\n:))\n\n")
    chosen_game = input("Qual foi o jogo selecionado? (1-10 e JQK)")
    print(there_goes.there_goes[chosen_game])
    input("Esperando resultado...")
    clear_terminal()
    music = spanish_music.choose_random_spanish_music()
    input(f"O perdedor deve receber um bigode num lugar no corpo desenhado com caneta. Quem recebeu o terceiro bigode, deve fazer uma dança na dança mais espanhol quanto possível para a música {music}")
    
        

def display_remaining_rule_time(player):
    rules = []
    for rule in player.rules:
        turns_left = rule[1] - 1
        if rule[1] == 0:
            print(f"A regra '{rule[0]}' foi removida.")
        else: 
            print(f"Faltam {turns_left} rodadas para a regra '{rule[0]}' acabar.")
            rules.append([rule[0], turns_left])
    player.rules = rules

def pass_turn():
    """Função para passar a vez"""
    print("Você passou a vez.")
    print("Aperte Enter para continuar...")
    input()
    clear_terminal()

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

    surprise_there_goes = random.sample(range(10, 20*len(players)), 6)
    current_people_turn_count = 0

    # Passo 3: Loop principal do jogo
    while not game_over(players):
        if current_people_turn_count % len(players) == 0 and current_people_turn_count // len(players) in surprise_there_goes:
            handle_there_goes(players)
        current_player = next_player_in_queue(players)
        display_turn_info(current_player)
        passed = False
        rule_created = False
        # Exibir opções para o jogador
        while not passed:
            action = get_player_action()
            if action == "minhas informações" or action == "1":
                show_player_info(current_player)
            elif (action == "exchange dos cria" or action == "2" and not rule_created):
                handle_rules(players)
                rule_created = True
            elif action == "usar vantagem" or action == "3":
                handle_advantages(current_player)
            elif action == "passar a vez" or action == "4" or action == "":
                pass_turn()
                passed = True
        
        clear_terminal()

if __name__ == "__main__":
    main()
