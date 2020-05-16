import time
from threading import Thread

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Slot, Signal, QPoint, QPropertyAnimation, QRect, QEasingCurve, QObject
from PySide2.QtGui import Qt, QTransform

from Assets.game_ui_qt import Ui_Form, QGraphicsOpacityEffect, QLabel
from TheGame import TheGame
from GameState2 import GameState

class GameGuiThread(QObject):
    def animateLeftHandDown(self):

        pass

    def animateLeftHandUp(self):

        pass

    def _animateLeftHandUp(self, to_):
        i = 1
        while i < 5:

            i+=1



class GameGui(Ui_Form):
    playerTurnSignal = Signal(int)

    def __init__(self):
        super().__init__()
        self.the_game = TheGame()

        self.setupUi(self)
        self.setFixedSize(384, 670)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.connectWidget()
        self.initGuiProperty()

        self.show()
        self.clicked_player = ""

    def connectWidget(self):
        self.start_button.mousePressEvent = self.startButtonClicked
        self.exit_button.mousePressEvent = self.closeEvent

        self.player_left.mousePressEvent = self.playerLeftClicked
        self.player_right.mousePressEvent = self.playerRightClicked
        self.ai_left.mousePressEvent = self.aiLeftClicked
        self.ai_right.mousePressEvent = self.aiRightClicked

        self.playerTurnSignal.connect(self.the_game.playGame)
        self.the_game.resultStateSignal.connect(self.stateResultCallback)

        self.move_label.mousePressEvent = self.label_moveClicked
        self.move_label.mouseMoveEvent = self.label_moveMove

    def initGuiProperty(self):
        self.oldPos = self.pos()

        self.player_left.setText("")
        self.player_right.setText("")
        self.ai_left.setText("")
        self.ai_right.setText("")
        self.changeAiLeftHandTo(1)
        self.changeAiRightHandTo(1)
        self.changePlayerLeftHandTo(1)
        self.changePlayerRightHandTo(1)

        self.bg_label.setPixmap(QtGui.QPixmap("Assets/Background dll/BG.png"))
        self.logo_label.setPixmap(QtGui.QPixmap("Assets/Background dll/Ayo Main.png"))
        # self.logo_label.setScaledContents(True)
        self.logo_label.setText("")

        logo_start = QtGui.QPixmap("Assets/Background dll/Start.png")
        self.start_button.setPixmap(logo_start)
        # self.start_button.setScaledContents(True)
        self.exit_button.setPixmap(QtGui.QPixmap("Assets/Background dll/Exit.png"))
        # self.exit_button.setScaledContents(True)

        self.ingame_frame.hide()
        self.home_frame.raise_()
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
        # self.ai_left.setText(str(game_state.values[1][0]))
        self.changeAiLeftHandTo(game_state.values[1][0])
        self.changeAiRightHandTo(game_state.values[1][1])

    def changeAiLeftHandTo(self, number):
        # self.player_left.setPixmap()
        image_hand = QtGui.QPixmap("Assets/AiPlayer/"+str(number)+"Kiri.png")
        image_hand = image_hand.transformed(QTransform().scale(1, -1))
        self.ai_left.setPixmap(image_hand)
        self.ai_left.setScaledContents(True)

    def changeAiRightHandTo(self, number):
        # self.player_left.setPixmap()
        image_hand = QtGui.QPixmap("Assets/AiPlayer/"+str(number)+"Kanan.png")
        image_hand = image_hand.transformed(QTransform().scale(1, -1))
        self.ai_right.setPixmap(image_hand)
        self.ai_right.setScaledContents(True)

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

    def moveWidgetTo(self, widget:QLabel, to_x, to_y):
        widget.setGeometry(QRect(widget.x()+to_x, widget.y()+to_y, widget.width(), widget.height()))

    def showHandAnimation(self):
        self.anim_group = QtCore.QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animateWidgetMove(self.player_left, 0, -300, 1000, QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.player_right, 0, -300, 1000, QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.ai_left, 0, 300, 1000, QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.ai_right, 0, 300, 1000, QEasingCurve.InOutExpo))
        self.anim_group.start()

    def showIngameFrame(self):
        self.home_frame.hide()
        self.ingame_frame.show()
        self.ingame_frame.raise_()

        self.moveWidgetTo(self.player_left, 0, 300)
        self.moveWidgetTo(self.player_right, 0, 300)
        self.moveWidgetTo(self.ai_left, 0, -300)
        self.moveWidgetTo(self.ai_right, 0, -300)

        self.showHandAnimation()
        pass

    def animateWidgetMove(self, widget, to_x, to_y, duration, ease):
        anim = QPropertyAnimation(widget, b"geometry")
        anim.setDuration(duration)
        anim.setStartValue(
            QRect(widget.x(), widget.y(), widget.width(), widget.height()))
        anim.setEndValue(QRect(widget.x()+to_x, widget.y() + to_y, widget.width(),
                               widget.height()))
        anim.setEasingCurve(ease)
        # anim.state()
        return anim

    def startButtonAnimation(self):
        # widget.setPixmap
        # self.start_button.setPixmap(QtGui.QPixmap("Assets/Background dll/Start.png")
        #                             .scaledToHeight(75,Qt.TransformationMode.SmoothTransformation))
        # time.sleep(0.1)
        # self.anim.finished.connect(self.showIngameFrame)
        # self.anim.start()
        # self.effect = QGraphicsOpacityEffect()
        # self.start_button.setGraphicsEffect(self.effect)
        #
        # self.anim2 = QPropertyAnimation(self.effect, b"opacity")
        # self.anim2.setDuration(500)
        # # self.anim2.setCurrentTime(-100)
        # self.anim2.setStartValue(1)
        # self.anim2.setEndValue(1)

        self.anim_group = QtCore.QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animateWidgetMove(self.start_button,0,300,1000,QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.exit_button,0,100,1000,QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.logo_label,0,-400,1300,QEasingCurve.InBounce))
        self.anim_group.finished.connect(self.showIngameFrame)
        self.anim_group.start()


    def startButtonClicked(self, event):
        self.startButtonAnimation()

    def label_moveClicked(self, event):
        self.oldPos = event.globalPos()

    def label_moveMove(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        # print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def exitPressed(self):
        # self.exit()
        # print("posisi 3", self.start_button.y())
        pass

    def closeEvent(self, event):
        print("QUIT BROOO")
        self.exitPressed()
        # self.close()
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    gui_main = GameGui()
    # gui_main.setupUi(Form)
    # Form.show()
    sys.exit(app.exec_())