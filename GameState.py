import networkx as nx
# import matplotlib.pyplot as plt

from collections import defaultdict
#PLAYER2 IS AI value = 1
class GameState():
    values = []
    player = -1
    def __init__(self, player, left1, right1, left2, right2):
        self.player1 = 0
        self.player2 = 1
        GameState.values = defaultdict(list)
        GameState.values[0].append(left1)
        GameState.values[0].append(right1)
        GameState.values[1].append(left2)
        GameState.values[1].append(right2)
        GameState.player = player
        print(GameState.values[0])
        print(GameState.values[1])

    def hasWon(self, player_now):
        # print(GameState.values[GameState.player][1])
        return len(GameState.values[1-player_now]) == 1 and GameState.values[1-player_now].__contains__(2)
        # return GameState.values[1-player_now].__contains__()

# if __name__ == '__main__':
#     gs = GameState(1,2,3,5,7)
#     print(gs.hasWon(1))
#     g2 = GameState(1,44,33,22,11)





