import random
from .ability import choose_abilities
from .mae import choose_mae

class Player:
    def __init__(self, name, online=False, numero_carta=14):
        self.name = name
        self.online = online
        self.mae = self._assign_mae(numero_carta) 
        self.fichas = 15
        self.cartas = 3
        self.abilities = self._assign_abilities()
        self.rules = []
        self.exchange_multiplier = 1 # 10 fichas dividido por isso é igual a quantas cartas serão recebidas
        self.advantages = []

    def _assign_abilities(self):
        # Atribui duas habilidades aleatórias ao jogador usando a função do ability.py
        abilities = choose_abilities()
        return {
            "revealed": abilities[0],  # Habilidade revelada para todos
            "secret": abilities[1]  # Habilidade secreta, apenas o jogador sabe
        }
    
    def _assign_mae(self, numero_carta):
        sua_mae = choose_mae(numero_carta)
        return sua_mae

    def reveal_info(self):
        """Exibe as informações do jogador"""
        return {
            "name": self.name,
            "online": self.online,
            "mae": self.mae,
            "abilities": self.abilities,
        }
        

    def take_turn(self):
        """Realiza as ações disponíveis no turno do jogador"""
        # Aqui você pode definir as ações que o jogador pode realizar em seu turno
        pass


