from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Slot, Signal

from Assets.Ui_Form import Ui_Form
from TheGame import TheGame
from GameState2 import GameState


class GameGui(Ui_Form):
    playerTurnSignal = Signal(int)

    def __init__(self, Form):
        super().__init__()
        self.the_game = TheGame()

        self.setupUi(Form)
        self.ingame_frame.hide()
        self.home_frame.raise_()
        self.connectWidget()
        self.initGuiProperty()

        Form.show()

        self.clicked_player = ""
        # self.ai_clicked = None
        # self.the_game.start()

    def connectWidget(self):
        self.start_button.clicked.connect(self.startButtonClicked)
        self.player_left.mousePressEvent = self.playerLeftClicked
        self.player_right.mousePressEvent = self.playerRightClicked
        self.ai_left.mousePressEvent = self.aiLeftClicked
        self.ai_right.mousePressEvent = self.aiRightClicked

        self.playerTurnSignal.connect(self.the_game.playGame)
        self.the_game.resultStateSignal.connect(self.stateResultCallback)

    def initGuiProperty(self):
        self.player_left.setText("")
        self.player_right.setText("")
        self.changePlayerLeftHandTo(1)
        self.changePlayerRightHandTo(1)
        # self.ai_left.setText("")
        # self.ai_right.setText("")

    @Slot(object)
    def stateResultCallback(self, game_state: GameState):
        print("SLOT STATE ")
        game_state.print()
        self.changePlayerLeftHandTo(game_state.values[0][0])
        self.changePlayerRightHandTo(game_state.values[0][1])
        # self.player_left.setText(str(game_state.values[0][0]))
        # self.player_right.setText(str(game_state.values[0][1]))
        self.ai_left.setText(str(game_state.values[1][0]))
        self.ai_right.setText(str(game_state.values[1][1]))

    def changePlayerLeftHandTo(self, number):
        # self.player_left.setPixmap()
        image_hand = QtGui.QPixmap("Assets/Player1/"+str(number)+"Kiri.png")
        self.player_left.setPixmap(image_hand)
        self.player_left.setScaledContents(True)
        pass

    def changePlayerRightHandTo(self, number):
        # self.player_right.setPixmap()
        image_hand = QtGui.QPixmap("Assets/Player1/" + str(number) + "Kanan.png")
        self.player_right.setPixmap(image_hand)
        self.player_right.setScaledContents(True)
        pass

    def playerLeftClicked(self, event):
        if self.clicked_player != "":
            self.playerTurnSignal.emit(4)
            self.clicked_player = ""
        else:
            self.clicked_player = "left"

    def playerRightClicked(self, event):
        if self.clicked_player != "":
            self.playerTurnSignal.emit(4)
            self.clicked_player = ""
        else:
            self.clicked_player = "right"

    def aiLeftClicked(self, event):
        # self.ai_clicked = "left"
        if (self.clicked_player == 'left'):
            self.playerTurnSignal.emit(0)
        elif self.clicked_player == 'right':
            self.playerTurnSignal.emit(3)
        self.clicked_player = ""

    def aiRightClicked(self, event):
        # self.ai_clicked = "right"
        if (self.clicked_player == 'left'):
            self.playerTurnSignal.emit(1)
        elif self.clicked_player == 'right':
            self.playerTurnSignal.emit(2)
        self.clicked_player = ""

    def startButtonClicked(self):
        self.home_frame.hide()
        self.ingame_frame.raise_()
        self.ingame_frame.show()
        # self.the_game.start()

    def exitPressed(self):
        self.the_game.stop()
        self.exit()

    def closeEvent(self, event):
        print("QUIT BROOO")
        self.exitPressed()
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    gui_main = GameGui(Form)
    # gui_main.setupUi(Form)
    # Form.show()
    sys.exit(app.exec_())