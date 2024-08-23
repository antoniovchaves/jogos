def minigame_points(players, minigame_type):
    podium = {}
    total_coins = 0
    for player in players:
        position = input(f"Colocação de {player.name}: ")
        print(f"Antigo excange de {player.name}: {player.exchange_multiplier}")
        match minigame_type:
            case "1": # coins
                coins = int(input(f"Quantas moedas {player.name} pegou? "))
                podium[player.name] = coins
                total_coins += coins
            case "2": # cada um por si
                player.exchange_multiplier += (5 - int(position)) // 2
            case "3":
                player.exchange_multiplier += (2 - int(position)) // 2
            case "4":
                player.exchange_multiplier += (1 - int(position)) // 2
    if minigame_type == "1":
        multiplier = 4 / total_coins
        for player in players:            
            player.exchange_multiplier += int(multiplier * podium[player.name])
