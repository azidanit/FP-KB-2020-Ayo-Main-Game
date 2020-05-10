from GameState2 import GameState
from Evaluator import Evaluator

class AiMove():
    layer_tree = 3
    best_state = 0
    best_utility = 0
    which_finger = 0

    def predictMove(self, game_state: GameState):
        self.eval = Evaluator()
        probability_move = [game_state]

        utilityValue = []
        tr2 = []
        tr = probability_move
        if self.eval.evaluate(probability_move[0],1) == 10000:
            print("AI WINNING")
            return -1, 10000, None

        print(" PROB -------")
        tr[0].print()
        # print(" PROB 2-------")
        tr, _, _  = self.tapToAll(tr[0])
        for i in range(len(tr)):
            # self.eval.evaluate(tr[i], 1)
            utilityValue.append(self.eval.evaluate(tr[i], 1))

        # print("BEST ",AiMove.best_utility, "Finger" ,AiMove.which_finger,"\tstate ", end='')
        # AiMove.best_state.print()
        # tr[1].print()
        print("PERTAMA " ,utilityValue)

        for i in range(len(tr)):
            # self.eval.evaluate(tr[i], 1)
            print("ITER KE DUA", i)
            tr[i].print()
            tr2, be_util, be_state = self.tapToAll(tr[i])
            print("berapa kali sih ", be_util)
            if utilityValue[i] > be_util:
                utilityValue[i] = be_util

        print("KEDUA ", utilityValue)

        best_finger = 0
        best_util = 0
        best_state = None
        i = 0
        for i in range(len(utilityValue)):
            if i == 0:
                best_util = utilityValue[i]
            else:
                # print("ACCES ",i," ", utilityValue[i])
                if utilityValue[i] > be_util:
                    best_util = utilityValue[i]
                    best_finger = i

        best_state = tr[best_finger]
        return best_finger, best_util, best_state
        # 0 ai kiri ke kiri
        # 1 ai kiri ke kanan
        # 2 ai kanan ke kiri
        # 3 ai kanan ke kanan
        # 4 ai divide

        # for i in range(len(tr2)):
        #     # self.eval.evaluate(tr[i], 1)
        #     print("ITER KE TIGA", i)
        #     tr[i].print()
        #     tr3, be_util, be_state = self.tapToAll(tr2[i])
        #     print("berapa kali sih2 ", be_util)
        #     if utilityValue[i] < be_util:
        #         utilityValue[i] = be_util
        #
        # print("KETIGA ", utilityValue)
        #
        # for i in range(len(tr)):
        #     # self.eval.evaluate(tr[i], 1)
        #     print("ITER KE EMPAT", i)
        #     tr[i].print()
        #     tr2, be_util, be_state = self.tapToAll(tr[i])
        #     print("berapa kali sih2 ", be_util)
        #     if utilityValue[i] > be_util:
        #         utilityValue[i] = be_util
        #
        # print("KEEMPAT ", utilityValue)


    def tapToAll(self, game_state: GameState):
        probability_move = []
        print(" PROB 2-------")
        player_left = game_state.values[0][0]
        player_right = game_state.values[0][1]

        ai_left = game_state.values[1][0]
        ai_right = game_state.values[1][1]

        blocked_finger = [0,0,0,0,0]
        blocked_finger_pl = [0, 0, 0, 0,0]

        if player_left == 0:
            blocked_finger_pl[0] = 1
            blocked_finger_pl[1] = 1
        if player_right == 0:
            blocked_finger_pl[2] = 1
            blocked_finger_pl[3] = 1
        if ai_left == 0:
            blocked_finger[0] = 1
            blocked_finger[1] = 1
        if ai_right == 0:
            blocked_finger[2] = 1
            blocked_finger[3] = 1

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
                GameState(1, player_left, player_right, ai_left, (player_left + ai_right) % 5))
            probability_move.append(
                GameState(1, player_left, player_right, (player_right + ai_left) % 5, ai_right))
            probability_move.append(
                GameState(1, player_left, player_right, ai_left, (player_right + ai_right) % 5))
            if ((player_left + player_right) % 2 ==0):
                probability_move.append(
                    GameState(1, int((player_left + player_right)/2), int((player_left + player_right)/2), ai_left, ai_right))
        # for i in range(len(probability_move)):
        #     probability_move[i].print()
        # pass
        #
        for i in range(len(probability_move)):
            rating = self.eval.evaluate(probability_move[i],1)
            # if i == 0:
            #     AiMove.best_utility = rating
            #     AiMove.best_state = probability_move[i]
            if probability_move[i].player == 0:
                if i == 0:
                    AiMove.best_utility = -11111
                if rating > AiMove.best_utility and (blocked_finger[i] != 1 and blocked_finger_pl[i] != 1):
                    print("INI MASUK ai", i)
                    AiMove.best_utility = rating
                    AiMove.best_state = probability_move[i]
                    AiMove.which_finger = i
            else:
                if i == 0:
                    AiMove.best_utility = 11111
                print("i : ", i, " block ", blocked_finger_pl[i], "block ai ", blocked_finger[i])
                if rating < AiMove.best_utility and (blocked_finger_pl[i] != 1 and blocked_finger[i] != 1):
                    print("INI MASUK ",i)
                    AiMove.best_utility = rating
                    AiMove.best_state = probability_move[i]
                    AiMove.which_finger = i
            print("utility", rating, end='\t State : ')
            probability_move[i].print()

        print("best from serc: ", AiMove.best_utility)
        return probability_move, AiMove.best_utility, AiMove.best_state
