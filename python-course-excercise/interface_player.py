from abc import ABC, abstractmethod
import random

class Player(ABC):

    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self) -> tuple[int, int]:
        random_choice = random.choice(self.moves)
        new_position = self.position[0] + random_choice[0], self.position[1] + random_choice[1]
        self.position = new_position
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
        (0, 1),   # arriba
        (0, -1),  # abajo
        (-1, 0),  # izquierda
        (1, 0)    # derecha
        ]

    def level_up(self):
        new_moves = [
        (-1, 1),    # diagonal arriba derecha
        (-1, -1),   # diagonal arriba izquierda
        (1, -1),    # diagonal abajo izquierda
        (1, 1)      # diagonal abajo derecha
        ]
        self.moves = self.moves + new_moves
    
