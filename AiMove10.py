from GameState2 import GameState
from Evaluator import Evaluator

class AiMove():

    def predictMove(self,game_state: GameState):
        util_value, prob_state = self.tapToAll(game_state)

        best_util = None;

        for i in range(len(prob_state)):
            best_util = None;
            if util_value[i] is not None:
                util_value2, prob_state2 = self.tapToAll(prob_state[i])
                print("iter ke i",i)
                for y in range(len(util_value2)):
                    if util_value2[y] is not None:
                        if best_util is None:
                            best_util = util_value2[y]
                        elif best_util > util_value2[y]:
                            best_util = util_value2[y]
                print("Minim UTIL kecil", best_util)


                if best_util is not None and best_util < util_value[i]:
                    print("pindah dari ",util_value[i], " util ke ", best_util)
                    util_value[i] = best_util

        best_finger = None
        best_util = None
        for i in range(len(util_value)):
            if util_value[i] is not None:
                if best_util is None:
                    best_util = util_value[i]
                    best_finger = i
                elif best_util < util_value[i]:
                    best_util = util_value[i]
                    best_finger = i


        print(util_value)
        print("BEST UTIL ", best_util, " finger ", best_finger, " state ", end='')
        prob_state[best_finger].print()
        return best_finger, best_util, prob_state[best_finger]

    def tapToAll(self,game_state: GameState):
        self.eval = Evaluator()

        player_left = game_state.values[0][0]
        player_right = game_state.values[0][1]
        ai_left = game_state.values[1][0]
        ai_right = game_state.values[1][1]

        probability_move = []
        utility_value = [0, 0, 0, 0, 0]

        if(game_state.player == 1): #Ai turn
            probability_move.append(
                GameState(0, (player_left + ai_left) % 5, player_right, ai_left, ai_right))
            probability_move.append(
                GameState(0, player_left, (player_right + ai_left) % 5, ai_left, ai_right))
            probability_move.append(
                GameState(0, (player_left + ai_right) % 5, player_right, ai_left, ai_right))
            probability_move.append(
                GameState(0, player_left, (player_right + ai_right) % 5, ai_left, ai_right))
            if ((ai_left + ai_right) % 2 ==0):
                probability_move.append(
                    GameState(0, player_left, player_right, int((ai_left + ai_right)/2), int((ai_left + ai_right)/2)))
        else: #Player turn
            probability_move.append(
                GameState(1, player_left, player_right, (player_left + ai_left) % 5,ai_right))
            probability_move.append(
                GameState(1, player_left, player_right, (player_right + ai_left) % 5, ai_right))
            probability_move.append(
                GameState(1, player_left, player_right, ai_left, (player_left + ai_right) % 5))
            probability_move.append(
                GameState(1, player_left, player_right, ai_left, (player_right + ai_right) % 5))
            if ((player_left + player_right) % 2 ==0):
                probability_move.append(
                    GameState(1, int((player_left + player_right)/2), int((player_left + player_right)/2), ai_left, ai_right))

        for i in range(len(probability_move)):
            print("i:",i ,end=' \t')
            probability_move[i].print()
            if ai_left == 0:
                utility_value[0] = utility_value[1] = None
            if ai_right == 0:
                utility_value[2] = utility_value[3] = None
            if player_left == 0:
                utility_value[0] = utility_value[2] = None
            if player_right == 0:
                utility_value[1] = utility_value[3] = None


            if ((ai_left+ai_right) %2) != 0 and probability_move[i].player == 0:
                utility_value[4] = None
            if ((player_left+player_right) %2) != 0 and probability_move[i].player == 1:
                utility_value[4] = None

            if utility_value[i] is not None:
                utility_value[i] = self.eval.evaluate(probability_move[i],1)

        print("UTILITY ", utility_value)

        return utility_value, probability_move

