from .words import convert_to_ascii_string

def minigame_points(players, minigame_type):
    podium = {}
    total_coins = 0
    for player in players:
        position = input(f"Colocação de {player.name} ('0' se não jogou): ")
        if position != "0":
            match minigame_type:
                case "1": # coins
                    coins = int(input(f"Quantas moedas {player.name} pegou? "))
                    podium[player.name] = coins
                    total_coins += coins
                case "2": # cada um por si
                    player.exchange_multiplier += (6 - int(position)) // 2
                case "3":
                    player.exchange_multiplier += (3 - int(position)) // 2
                case "4":
                    player.exchange_multiplier += (1 - int(position)) // 2
    if minigame_type == "1":
        multiplier = 4 / total_coins
        for player in players:            
            player.exchange_multiplier += int(multiplier * podium[player.name])

def handle_minigame_bet(players):
    print(convert_to_ascii_string("mlk, vamo de minigame"))
    print("\n\n\n")

    minigame_type = input("Qual foi o tipo de minigame?\n- moedas (1)\n- cada um por si (2)\n- duplasquinha (3)\n- covardia 3 contra 1 (4)\nInsira aqui: ")
    minigame_points(players, minigame_type)