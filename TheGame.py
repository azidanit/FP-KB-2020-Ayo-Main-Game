import time
from threading import Lock

from PySide2.QtCore import QObject, QThread, Slot, Signal, QTimer

from GameState2 import GameState
from Evaluator import Evaluator
from AiMove10 import AiMove
# from Assets.

class TheGame(QObject):
    resultGameSignal = Signal(int)
    resultStateSignal = Signal(object)
    resultAiSignal = Signal(object)
    resultPlayerSignal = Signal(object)
    resultLoseSignal = Signal(object)
    animateAiSignal = Signal(int)

    def __init__(self):
        super().__init__()
        self.is_game_running = False
        self.game_mtx = Lock()
        self.game_states = GameState(0, 1, 1, 1, 1)

    def resetState(self):
        self.game_mtx.acquire()
        self.game_states = GameState(0, 1, 1, 1, 1)
        self.game_mtx.release()

    @Slot(int)
    def playGame(self, val):
        self.evalutor_state = Evaluator()
        print("------------------PLAY PALY------YOU CHOOSE : ")
        self.Ai = AiMove()
        self.finger = None
        self.util = None
        self.state = None
        self.game_states.print()
        # while self.is_game_running:
        if self.game_states.player == 0:
            player_left = self.game_states.values[0][0]
            player_right = self.game_states.values[0][1]
            ai_left = self.game_states.values[1][0]
            ai_right = self.game_states.values[1][1]
            # val = input("masukan")
            self.game_mtx.acquire()
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
            self.game_mtx.release()
            print("\n------------------------YOU CHOOSE : ")
            self.game_states.print()

            self.resultPlayerSignal.emit(self.game_states)


    def playGameAi(self):
        print("AI TURN")
        self.finger, self.util, self.state = self.Ai.predictMove(self.game_states)
        self.state.print()

        self.game_states = self.state
        print("--------FINGER AI ",self.finger)
        if self.util >= 10000:
            print("AI WIN, YOU LOOSE!")
            self.game_states.values[2].append(self.finger)

            self.resultAiSignal.emit(self.game_states)

            self.resultLoseSignal.emit(self.game_states)
        else:
            # self.animateAiSignal.emit(self.finger)
            self.game_states.values[2].append(self.finger)

            self.resultAiSignal.emit(self.game_states)

# if __name__ == '__main__':
#     test_game = TheGame()
#     test_game.testFourBoards()