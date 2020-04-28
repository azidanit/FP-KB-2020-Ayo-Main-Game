from GameState2 import GameState
from Evaluator import Evaluator

class TestGame():
    def testFourBoards(self):
        self.evalutor_state = Evaluator()
        self.game_states= [
            GameState(1, 1, 3, 1, 3),
            GameState(1, 1, 3, 1, 2),
            GameState(1, 1, 3, 0, 1),
            GameState(0, 0, 0, 0, 2)
        ]

        for i in self.game_states:
            gs_rating = self.evalutor_state.evaluate(i, 0)

            print(gs_rating, " ", i.print())

if __name__ == '__main__':
    test_game = TestGame()
    test_game.testFourBoards()