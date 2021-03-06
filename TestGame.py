from GameState2 import GameState
from Evaluator import Evaluator
from AiMove11 import AiMove2
class TestGame():
    def testFourBoards(self):
        self.evalutor_state = Evaluator()

        self.game_states= [
            # GameState(1, 0, 1, 1, 2)

            # GameState(1, 0, 1, 4, 2)
            GameState(1, 1, 2, 4, 1),
            # GameState(0, 0, 1, 2, 4),
            #
            # GameState(1, 3, 3, 0, 4),
            # GameState(1, 3, 3, 0, 2),
            #
            # GameState(1, 0, 3, 0, 4),
            # GameState(1, 0, 3, 0, 2),
            #
            # GameState(1, 0, 1, 3, 4),
            # GameState(1, 0, 1, 0, 2),

        ]
        for i in self.game_states:
            gs_rating = self.evalutor_state.evaluate(i, 1)
            print("utility : ",gs_rating, end='\t state: ')
            i.print()

        Ai = AiMove2()
        Ai.predictMove(self.game_states[0])
if __name__ == '__main__':
    test_game = TestGame()
    test_game.testFourBoards()