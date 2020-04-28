from collections import defaultdict

class GameState():
    values = []
    def __init__(self, player, left1, right1, left2, right2):
        self.player1 = 0
        self.player2 = 1
        self.values = defaultdict(list)
        self.values[0].append(left1)
        self.values[0].append(right1)
        self.values[1].append(left2)
        self.values[1].append(right2)
        self.player = player
        # print(GameState.values[0])
        # print(GameState.values[1])

    def hasWon(self, player_now):
        # print(GameState.values[GameState.player][1])
        # print("Dieksekusi", len(self.values[1-player_now]))
        return self.values[1-player_now][0] == 0 and self.values[1-player_now][1] == 0
        # return GameState.values[1-player_now].__contains__()

    def print(self):
        print(self.player, " ", self.values[0], " ", self.values[1])


# if __name__ == '__main__':
#     gs = GameState(1,2,3,5,7)
#     print(gs.hasWon(1))
#     g2 = GameState(1,44,33,22,11)





