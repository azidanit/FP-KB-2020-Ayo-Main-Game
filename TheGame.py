from GameState2 import GameState
from Evaluator import Evaluator
from AiMove10 import AiMove
class TheGame():
    def testFourBoards(self):
        self.evalutor_state = Evaluator()

        self.game_states = GameState(0, 1, 1, 1, 1)
        self.Ai = AiMove()
        self.finger = None
        self.util = None
        self.state = None
        self.game_states.print()
        while True:
            if self.game_states.player == 0:
                player_left = self.game_states.values[0][0]
                player_right = self.game_states.values[0][1]
                ai_left = self.game_states.values[1][0]
                ai_right = self.game_states.values[1][1]
                val = input("PERINTAH : ")
                print(val)
                val = int(val)
                if val == 0:
                    # print("Masuk")
                    self.game_states =(
                        GameState(1, player_left, player_right, (player_left + ai_left) % 5, ai_right))
                if val == 1:
                    self.game_states =(
                        GameState(1, player_left, player_right, ai_left, (player_left + ai_right) % 5))
                if val == 2:
                    self.game_states =(
                        GameState(1, player_left, player_right, ai_left, (player_right + ai_right) % 5))
                if val == 3:
                    self.game_states =(
                        GameState(1, player_left, player_right, (player_right + ai_left) % 5, ai_right))
                if val == 4:
                    if ((player_left + player_right) % 2 == 0):
                        self.game_states =(
                            GameState(1, int((player_left + player_right) / 2), int((player_left + player_right) / 2),
                                      ai_left, ai_right))

                print("\n------------------------YOU CHOOSE : ")
                self.game_states.print()
            else:
                print("AI TURN")
                self.finger, self.util, self.state = self.Ai.predictMove(self.game_states)
                self.state.print()
                self.game_states = self.state
                if self.util >= 10000:
                    print("AI WIN, YOU LOOSE!")
                    break
if __name__ == '__main__':
    test_game = TheGame()
    test_game.testFourBoards()