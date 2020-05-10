from GameState2 import GameState

class Evaluator():
    def evaluate(self, game_state: GameState , player_now):
        if(game_state.hasWon(player_now)):
            return 10000;
        if (game_state.hasWon(1-player_now)):
            return -10000;

        sign = 1
        if(game_state.player == 1-player_now):
            sign = -1

        value = 0

        #Tinggal memiliki satu tangan, kondisi buruk
        if (game_state.values[game_state.player].__contains__(0)):
            value -= sign*100
        if (game_state.values[1-game_state.player].__contains__(0)):
            value += sign*100

        #mempunyai tangan dengan jari 4 lebih beresiko daripada 1 jari (5 point value)
        for i in range(2):
            value -= sign * game_state.values[game_state.player][i] * 5
            value += sign * game_state.values[1-game_state.player][i] * 5

        #player memiliki state unggul ketika salah satu tangan dapat membunuh musuh 20 point value
        numMakeDead = 0
        for i in range(2):
            player_tmp1 = game_state.values[game_state.player][i]
            for y in range(2):
                player_tmp2 = game_state.values[1-game_state.player][y]
                if (player_tmp1 + player_tmp2 >= 5):
                    numMakeDead += 1
        value += sign * numMakeDead * 20

        return value
