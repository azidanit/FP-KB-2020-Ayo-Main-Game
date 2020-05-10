from GameState2 import GameState
from Evaluator import Evaluator

class AiMove():
    layer_tree = 2
    best_state = 0
    best_utility = 0
    which_finger = 0
    def predictMove(self, game_state: GameState):
        self.eval = Evaluator()
        probability_move = [game_state]

        tr = probability_move
        print(" PROB -------")
        tr[0].print()
        # print(" PROB 2-------")
        tr = self.tapToAll(tr[0])

        print("BEST ",AiMove.best_utility, "Finger" ,AiMove.which_finger,"\tstate ", end='')
        AiMove.best_state.print()

    def tapToAll(self, game_state: GameState):
        probability_move = []
        print(" PROB 2-------")
        player_left = game_state.values[0][0]
        player_right = game_state.values[0][1]

        ai_left = game_state.values[1][0]
        ai_right = game_state.values[1][1]

        if(game_state.player == 1): #Ai turn
            probability_move.append(
                GameState(0, 0 if (player_left + ai_left) >= 5 else player_left + ai_left, player_right, ai_left, ai_right))
            probability_move.append(
                GameState(0, player_left, 0 if (player_right + ai_left) >= 5 else player_right + ai_left, ai_left, ai_right))
            probability_move.append(
                GameState(0, 0 if (player_left + ai_right) >= 5 else player_left + ai_right, player_right, ai_left, ai_right))
            probability_move.append(
                GameState(0, player_left, 0 if (player_right + ai_right) >= 5 else player_right + ai_right, ai_left, ai_right))
        else: #Player turn
            probability_move.append(
                GameState(1, player_left, player_right, 0 if (player_left + ai_left) >= 5 else player_left + ai_left,ai_right))
            probability_move.append(
                GameState(1, player_left, player_right, 0 if (player_right + ai_left) >= 5 else player_right + ai_left, ai_right))
            probability_move.append(
                GameState(1, player_left, player_right, ai_left, 0 if (player_left + ai_right) >= 5 else player_left + ai_right))
            probability_move.append(
                GameState(1, player_left, player_right, ai_left, 0 if (player_right + ai_right) >= 5 else player_right + ai_right))

        # for i in range(len(probability_move)):
        #     probability_move[i].print()
        # pass
        #
        for i in range(len(probability_move)):
            rating = self.eval.evaluate(probability_move[i], 1)
            if rating > AiMove.best_utility:
                AiMove.best_utility = rating
                AiMove.best_state = probability_move[i]
                AiMove.which_finger = i
            print("utility", rating, end='\t State : ')
            probability_move[i].print()

        # print(" PROB 2-------")
        if(AiMove.layer_tree <= 3):
            AiMove.layer_tree+=1
            for i  in range(len(probability_move)):
                print(" PROB -------")
                probability_move[i].print()
                print("utility", self.eval.evaluate(probability_move[i],probability_move[i].player))
                self.tapToAll(probability_move[i])

        return probability_move