from GameState2 import GameState
from Evaluator import Evaluator

class AiMove2():
    def __init__(self):
        self.evaluator = Evaluator()
        self.all_depth = 3
        self.finger = 0
        self.is_win = None

    def predictMove(self, game_state: GameState):
        # util_value, prob_state = self.tapToAll(game_state)
        # prob_state_iter = prob_state.copy()
        # best_util = None
        # best_state = []
        # finger = 0
        # best_util, all_next_state, finger = self.findMove(game_state, 0, best_util, finger)
        # print("FIRST ANSWER  : ", finger, " util: ",best_util, " ",end='')
        # all_next_state[finger].print()
        # print("-------------------------------")
        # self.findAllMove(game_state,1)
        print("HASIL : ",self.minimax(game_state,self.all_depth))
        print("FINGER : ",self.finger)
        print("FINGER WIN : ", self.is_win)
        if self.is_win is None:
            return self.finger
        else:
            return self.is_win
        pass

    def minimax(self, game_state: GameState, depth):
        # print("USING RECURSIVE")
        now_util = self.evaluator.evaluate(game_state,1)
        if depth == 0:
            return now_util
        finger = 0
        if game_state.player == 1: #MAX
            print("MAXING ",depth)
            max_utility = -111111
            result_util, probability_move, result_finger, utility_value = self.findMove(game_state, 0, None, 0)
            for i in range(len(probability_move)):
                if utility_value[i] is not None:
                    print("FROM ", max_utility)
                    util = self.minimax(probability_move[i], depth-1)
                    print("IS ", util)
                    max_utility = max(max_utility, util)
                    print("To ", max_utility)
                    if max_utility == util and depth == self.all_depth:
                        self.finger = i
                        if max_utility >= 10000 and self.is_win is None:
                            self.is_win = i
                        print("change finger to ",i, "from dept ",depth)

            return max_utility

        else:
            print("MINIM ",depth)
            min_utility = 111111
            result_util, probability_move, result_finger, utility_value = self.findMove(game_state, 0, None,0)
            for i in range(len(probability_move)):
                if utility_value[i] is not None:
                    util = self.minimax(probability_move[i], depth - 1)
                    min_utility = min(min_utility, util)
                    # print("CHANGE MINIM FROM ",min)
                    # if min_utility == util and (self.all_depth == depth + 1):
                    #     self.finger = i
                    #     print("change finger to ",i)
            return min_utility



    def findAllMove(self, game_state: GameState, iter_i):
        best_util = None
        all_next_state = []
        all_util = []
        finger = 0
        best_util, all_next_state, finger, all_util = self.findMove(game_state, 0, best_util, finger)
        print("--FAM ANSWER  : ", finger, " util: ", best_util, " ", end='')
        all_next_state[finger].print()
        print("-------------------------------")

        if iter_i == 0:
            return
        elif iter_i == 1:
            for i in range(len(all_next_state)):
                if all_util[i] is not None:
                    temp_util = self.findMove(all_next_state[i],1,None,0)
                    if temp_util is not None:
                        if all_next_state[i].player == 1:
                            if all_util[i] < temp_util:
                                all_util[i] = temp_util
                        else:
                            if all_util[i] > temp_util:
                                all_util[i] = temp_util
                        # else:
        else:
            pass

        best_util = None
        for i in range(len(all_util)):

            if all_util[i] is not None:
                if best_util is None:
                    best_util = all_util[i]
                if all_util[i] > best_util:
                    finger = i
                    best_util = all_util[i]
        print("--FAM ANSWER 2 : ", finger, " util: ", best_util, " ", end='')
        all_next_state[finger].print()
        print(all_util)
        print("-------------------------------")

    def findMove(self, game_state: GameState, iter_i, result_util, result_finger):

        self.eval = Evaluator()

        player_left = game_state.values[0][0]
        player_right = game_state.values[0][1]
        ai_left = game_state.values[1][0]
        ai_right = game_state.values[1][1]

        probability_move = []
        utility_value = [0, 0, 0, 0, 0]

        if (game_state.player == 1):  # Ai turn
            probability_move.append(
                GameState(0, (player_left + ai_left) % 5, player_right, ai_left, ai_right))
            probability_move.append(
                GameState(0, player_left, (player_right + ai_left) % 5, ai_left, ai_right))
            probability_move.append(
                GameState(0, (player_left + ai_right) % 5, player_right, ai_left, ai_right))
            probability_move.append(
                GameState(0, player_left, (player_right + ai_right) % 5, ai_left, ai_right))
            if ((ai_left + ai_right) % 2 == 0):
                probability_move.append(
                    GameState(0, player_left, player_right, int((ai_left + ai_right) / 2),
                              int((ai_left + ai_right) / 2)))
        else:  # Player turn
            probability_move.append(
                GameState(1, player_left, player_right, (player_left + ai_left) % 5, ai_right))
            probability_move.append(
                GameState(1, player_left, player_right, (player_right + ai_left) % 5, ai_right))
            probability_move.append(
                GameState(1, player_left, player_right, ai_left, (player_left + ai_right) % 5))
            probability_move.append(
                GameState(1, player_left, player_right, ai_left, (player_right + ai_right) % 5))
            if ((player_left + player_right) % 2 == 0):
                probability_move.append(
                    GameState(1, int((player_left + player_right) / 2), int((player_left + player_right) / 2), ai_left,
                              ai_right))
        pass

        if ai_left == 0:
            utility_value[0] = utility_value[1] = None
        if ai_right == 0:
            utility_value[2] = utility_value[3] = None
        if player_left == 0:
            utility_value[0] = utility_value[2] = None
        if player_right == 0:
            utility_value[1] = utility_value[3] = None

        for i in range(len(probability_move)):
            print("i:",i ,end=' \t')
            probability_move[i].print()

            if ((ai_left == ai_right) or (((ai_left+ai_right) %2)!=0))  and probability_move[i].player == 0:
                utility_value[4] = None
            if ((player_left == player_right) or ((player_left+player_right) %2) != 0) and probability_move[i].player == 1:
                utility_value[4] = None
            if utility_value[i] is not None:
                utility_value[i] = self.eval.evaluate(probability_move[i],1)

        print("UTILITY ", utility_value)

        for i in range(len(utility_value)):
            if utility_value[i] is not None:
                if result_util is None:
                    result_util = utility_value[i]
                    result_finger = i
                elif probability_move[i].player == 0:
                    if result_util < utility_value[i]:
                        result_util = utility_value[i]
                        result_finger = i
                else:
                    if result_util > utility_value[i]:
                        result_util = utility_value[i]
                        result_finger = i

        print("MAX UTIL ",result_util, " iter:", iter_i)
        # return  result_util, probability_move[result_finger], result_finger
        if iter_i == 0:
            return result_util, probability_move, result_finger, utility_value
        elif iter_i == 1:
            print("REUSL UTIL : ",result_util)
            return result_util
        else:
            for i in range(len(utility_value)):
                if utility_value[i] is not None:
                    self.findAllMove(probability_move[i],iter_i-1)

            # return self.findMove(probability_move[result_finger],iter_i-1,result_util,result_finger)

