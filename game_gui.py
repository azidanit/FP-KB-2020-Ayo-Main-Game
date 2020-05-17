import time
from threading import Thread

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Slot, Signal, QPoint, QPropertyAnimation, QRect, QEasingCurve, QObject, QTimer
from PySide2.QtGui import Qt, QTransform, QImage, QPixmap
from PySide2.QtMultimedia import QSound

from Assets.game_ui_qt import Ui_Form, QGraphicsOpacityEffect, QLabel
from TheGame import TheGame
from GameState2 import GameState

class GameGuiThread(QObject):
    changePixmapPLeft = Signal(QPixmap)
    changePixmapPRight = Signal(QPixmap)
    changePixmapALeft = Signal(QPixmap)
    changePixmapARight = Signal(QPixmap)

    def animatePLeftHandDown(self, from_):

        pass

    def _animatePLeftHandDown(self, from_):
        pass

    def animatePLeftHandUp(self, to_):
        animate_thread = Thread(target=self._animateLeftHandUp, args=(to_,))
        animate_thread.start()
        pass

    def _animatePLeftHandUp(self, to_):
        i = 1
        while i < 5:
            img_hand = QPixmap("Assets/PlayerKiri/pkiri0"+str(to_)+"f"+str(i)+".png")
            self.changePixmapPLeft.emit(img_hand)
            i+=1
            time.sleep(0.1)



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
        self.move_label.mousePressEvent = self.label_moveClicked
        self.move_label.mouseMoveEvent = self.label_moveMove
        self.move_label.setEnabled(True)
        self.start_button.mousePressEvent = self.startButtonClicked
        self.exit_button.mousePressEvent = self.closeEvent

        self.play_again_label.mousePressEvent = self.playAgainClicked
        self.menu_label.mousePressEvent = self.menuClicked

        self.player_left.mousePressEvent = self.playerLeftClicked
        self.player_right.mousePressEvent = self.playerRightClicked
        self.ai_left.mousePressEvent = self.aiLeftClicked
        self.ai_right.mousePressEvent = self.aiRightClicked

        self.exit_button_ingame.mousePressEvent = self.menuClicked
        # self.player_left.enterEvent = self.hoverPlayerLeft
        # self.player_left.leaveEvent = self.unHoverPLayerLeft

        self.playerTurnSignal.connect(self.the_game.playGame)
        self.the_game.resultStateSignal.connect(self.stateResultCallback)
        self.the_game.resultAiSignal.connect(self.stateResultCallbackAi)
        self.the_game.resultPlayerSignal.connect(self.stateResultCallbackPlayer)
        self.the_game.resultLoseSignal.connect(self.playerLose)


        self.move_label.raise_()

    def hoverPlayerLeft(self, event):
        self.scaleWidgetTo(self.player_left,1.2)
        self.moveWidgetTo(self.player_left,0,-50)

    def unHoverPLayerLeft(self, event):
        self.scaleWidgetTo(self.player_left, 1/1.2)
        self.moveWidgetTo(self.player_left, 0, 50)
        pass

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

        self.lose_label.setPixmap(QPixmap("Assets/Background dll/YouLose.png"))
        self.lose_label.setAlignment(Qt.AlignHCenter)
        self.menu_label.setPixmap(QPixmap("Assets/Background dll/Exit.png"))
        self.menu_label.setAlignment(Qt.AlignHCenter)
        self.lose_frame.setStyleSheet("background-color:rgba(22,22,22,0.6)")
        self.lose_label.setStyleSheet("background-color:rgba(22,22,22,0)")
        self.menu_label.setStyleSheet("background-color:rgba(22,22,22,0)")
        self.play_again_label.setStyleSheet("background-color:rgba(22,22,22,0)")
        self.play_again_label.hide()
        self.lose_frame.hide()
        # self.moveWidgetTo(self.lose_frame,0,-800)

        self.ingame_frame.hide()
        self.home_frame.raise_()
        self.move_label.raise_()
        # self.ai_left.setText("")
        # self.ai_right.setText("")
        self.moveWidgetTo(self.status_game_label,400,0)
        self.exit_button_ingame.setPixmap(QPixmap("Assets/Background dll/Exit.png"))
        self.exit_button_ingame.setScaledContents(True)
        self.exit_button_ingame.hide()

        self.audio_main_menu = QSound("Assets/Audio/menu.wav")
        # self.audio_main_menu.
        self.audio_main_menu.setLoops(QSound.Infinite)
        self.audio_main_menu.play()

        self.audio_lose = QSound("Assets/Audio/lose.wav")
        self.audio_lose.setLoops(False)
        # self.audio_lose.play()

        # self.move_label.setStyleSheet("background-color:rgb(22,22,22)")

    @Slot(object)
    def stateResultCallback(self, game_state: GameState):
        print("SLOT STATE ")
        # time.sleep(1)
        # game_state.print()
        # self.changeAiLeftHandTo(game_state.values[1][0])
        # self.changeAiRightHandTo(game_state.values[1][1])
        #
        # # time.sleep(2)
        # self.stateResultCallbackAi(game_state)

    def showLoseFrame(self):
        self.lose_frame.show()
        self.lose_frame.raise_()
        # self.animMoveWidget(self.lose_frame,0,800,700,QEasingCurve.InExpo)
        pass



    @Slot(object)
    def playerLose(self, game_state):
        self.audio_main_menu.stop()
        self.audio_lose.play()
        self.changeAiLeftHandTo(game_state.values[1][0])
        self.changeAiRightHandTo(game_state.values[1][1])
        self.changePlayerLeftHandTo(game_state.values[0][0])
        self.changePlayerRightHandTo(game_state.values[0][1])
        self.status_game_label.setText("YOU LOSE!")
        print("KALAH GAME GUI")
        self.status_game_label.setPixmap(None)
        self.showLoseFrame()

    @Slot(object)
    def stateResultCallbackPlayer(self, game_state: GameState):
        print("SLOT STATE ")
        # time.sleep(1)
        game_state.print()
        self.changeAiLeftHandTo(game_state.values[1][0])
        self.changeAiRightHandTo(game_state.values[1][1])
        self.changePlayerLeftHandTo(game_state.values[0][0])
        self.changePlayerRightHandTo(game_state.values[0][1])
        self.turnStatusShow(1)

    def resetAiLeftHand(self):
        self.animMoveWidget(self.ai_left, 0, -175, 300, QEasingCurve.InExpo, self.changeAllHandImage)
        pass

    def resetAiRightHand(self):
        self.animMoveWidget(self.ai_right, 0, -175, 300, QEasingCurve.InExpo, self.changeAllHandImage)
        pass

    def resetAiLeftHand2(self):
        self.animMoveWidget(self.ai_left, -100, -175, 300, QEasingCurve.InExpo, self.changeAllHandImage)

    def resetAiRightHand2(self):
        self.animMoveWidget(self.ai_right, 100, -175, 300, QEasingCurve.InExpo, self.changeAllHandImage)

    def resetDivideAiHand(self):
        self.anim_devide = QtCore.QParallelAnimationGroup()
        self.anim_devide.addAnimation(self.animateWidgetMove(self.ai_left, -25, 0, 240, QEasingCurve.OutExpo))
        self.anim_devide.addAnimation(self.animateWidgetMove(self.ai_right, 25, 0, 240, QEasingCurve.OutExpo))
        self.anim_devide.finished.connect(self.changeAllHandImage)
        self.anim_devide.start()

    def animateAiHand(self, number):
        if number == 0:
            self.animMoveWidget(self.ai_left,0,175,300,QEasingCurve.InExpo,self.resetAiLeftHand)
        elif number == 1:
            self.animMoveWidget(self.ai_left,100,175,300,QEasingCurve.InExpo,self.resetAiLeftHand2)
        elif number == 2:
            self.animMoveWidget(self.ai_right, -100, 175, 300, QEasingCurve.InExpo, self.resetAiRightHand2)
        elif number == 3:
            self.animMoveWidget(self.ai_right, 0, 175, 300, QEasingCurve.InExpo, self.resetAiRightHand)
        elif number == 4:
            self.anim3 = QtCore.QParallelAnimationGroup()
            self.anim3.addAnimation(self.animateWidgetMove(self.ai_left,25,0,240,QEasingCurve.InExpo))
            self.anim3.addAnimation(self.animateWidgetMove(self.ai_right,-25,0,240,QEasingCurve.InExpo))
            self.anim3.finished.connect(self.resetDivideAiHand)
            self.anim3.start()

    @Slot(object)
    def stateResultCallbackAi(self, game_state: GameState):
        print("CALLBACKKK AI : ", game_state.values[2][0])
        self.game_state_tmp = game_state
        self.animateAiHand(game_state.values[2][0])
        # self.changeAiLeftHandTo(game_state.values[1][0])
        # self.changeAiRightHandTo(game_state.values[1][1])
        # self.changePlayerLeftHandTo(game_state.values[0][0])
        # self.changePlayerRightHandTo(game_state.values[0][1])
        self.turnStatusShow(0)

    def changeAllHandImage(self):
        game_state = self.game_state_tmp
        self.changeAiLeftHandTo(game_state.values[1][0])
        self.changeAiRightHandTo(game_state.values[1][1])
        self.changePlayerLeftHandTo(game_state.values[0][0])
        self.changePlayerRightHandTo(game_state.values[0][1])
        # self.turnStatusShow(0)

    @Slot(QPixmap)
    def setLeftPlayerHandImage(self, img):
        pass

    @Slot(QPixmap)
    def setRightPlayerHandImage(self, img):
        pass

    @Slot(QPixmap)
    def setLeftAiHandImage(self, img):
        pass

    @Slot(QPixmap)
    def setRightAiHandImage(self, img):
        pass

    def changeAiLeftHandTo(self, number):
        # self.player_left.setPixmap()
        # image_hand = QtGui.QPixmap("Assets/AiPlayer/"+str(number)+"Kiri.png")
        image_hand = QtGui.QPixmap("Assets/AiKiri/akiri0" + str(number) + "f4.png")
        image_hand = image_hand.transformed(QTransform().scale(1, -1))
        self.ai_left.setPixmap(image_hand)
        # self.ai_left.setScaledContents(True)

    def changeAiRightHandTo(self, number):
        # self.player_left.setPixmap()
        # image_hand = QtGui.QPixmap("Assets/AiPlayer/"+str(number)+"Kanan.png")
        image_hand = QtGui.QPixmap("Assets/AiKanan/akanan0" + str(number) + "f4.png")
        image_hand = image_hand.transformed(QTransform().scale(1, -1))
        self.ai_right.setPixmap(image_hand)
        self.ai_right.setScaledContents(True)

    def changePlayerLeftHandTo(self, number):
        # self.player_left.setPixmap()
        # image_hand = QtGui.QPixmap("Assets/Player1/"+str(number)+"Kiri.png")
        image_hand = QtGui.QPixmap("Assets/PlayerKiri/pkiri0"+str(number)+"f4.png")
        self.player_left.setPixmap(image_hand)
        self.player_left.setScaledContents(True)
        pass

    def changePlayerRightHandTo(self, number):
        # self.player_right.setPixmap()
        # image_hand = QtGui.QPixmap("Assets/Player1/" + str(number) + "Kanan.png")
        image_hand = QtGui.QPixmap("Assets/PlayerKanan/pkanan0"+str(number)+"f4.png")
        self.player_right.setPixmap(image_hand)
        self.player_right.setScaledContents(True)
        pass

    def playerLeftClicked(self, event):

        if self.clicked_player != "" and self.the_game.game_states.values[0][0] != self.the_game.game_states.values[0][1]:
            self.animMoveWidget(self.player_right,to_x=0, to_y=25,duration=400,ease=QEasingCurve.OutExpo, finished_=None)
            self.playerTurnSignal.emit(4)
            self.clicked_player = ""

        else:
            # self.player_left.setGeometry()
            # self.hoverPlayerLeft("")
            self.anim = self.animateWidgetMove(self.player_left,0,-25,400,QEasingCurve.OutExpo)
            self.anim.start()
            self.clicked_player = "left"
        print("CLICKED PLAYER ", self.clicked_player)

    def playerRightClicked(self, event):
        if self.clicked_player != "":
            self.animMoveWidget(self.player_left, to_x=0, to_y=25, duration=400, ease=QEasingCurve.OutExpo, finished_=None)
            self.playerTurnSignal.emit(4)
            self.clicked_player = ""
        else:
            self.anim = self.animateWidgetMove(self.player_right, 0, -25, 250, QEasingCurve.OutExpo)
            self.anim.start()
            self.clicked_player = "right"
        print("CLICKED PLAYER ", self.clicked_player)

    def resetPlayerLeft(self):
        self.anim = self.animateWidgetMove(self.player_left, 0, 175, 350, QEasingCurve.OutExpo)
        self.anim.start()

    def resetPlayerRight(self):
        self.anim = self.animateWidgetMove(self.player_right, 100, 175, 350, QEasingCurve.OutExpo)
        self.anim.start()

    def resetPlayerLeft2(self):
        self.anim = self.animateWidgetMove(self.player_left, -100, 175, 350, QEasingCurve.OutExpo)
        self.anim.start()

    def resetPlayerRight2(self):
        self.anim = self.animateWidgetMove(self.player_right, 0, 175, 350, QEasingCurve.OutExpo)
        self.anim.start()

    def animMoveWidget(self, widget:QLabel, to_x, to_y, duration, ease:QEasingCurve, finished_):
        self.anim = self.animateWidgetMove(widget, to_x, to_y, duration, ease)
        if finished_ is not None:
            print("sini")
            self.anim.finished.connect(finished_)
        self.anim.start()

    def aiLeftClicked(self, event):
        # self.ai_clicked = "left"
        print("CLICKED AI LEFT")

        if (self.clicked_player == 'left'):
            self.anim = self.animateWidgetMove(self.player_left, 0, -150, 450, QEasingCurve.OutExpo)
            self.anim.finished.connect(self.resetPlayerLeft)
            self.anim.start()
            self.playerTurnSignal.emit(0)
        elif self.clicked_player == 'right':
            self.anim = self.animateWidgetMove(self.player_right, -100, -150, 450, QEasingCurve.OutExpo)
            self.anim.finished.connect(self.resetPlayerRight)
            self.anim.start()
            self.playerTurnSignal.emit(3)

        self.clicked_player = ""

    def aiRightClicked(self, event):
        print("CLICKED AI RIGHT")
        # self.ai_clicked = "right"
        if (self.clicked_player == 'left'):
            self.anim = self.animateWidgetMove(self.player_left, 100, -150, 450, QEasingCurve.OutExpo)
            self.anim.finished.connect(self.resetPlayerLeft2)
            self.anim.start()
            self.playerTurnSignal.emit(1)
            print("CLICKED AI EMIT 1")
        elif self.clicked_player == 'right':
            self.anim = self.animateWidgetMove(self.player_right, 0, -150, 450, QEasingCurve.OutExpo)
            self.anim.finished.connect(self.resetPlayerRight2)
            self.anim.start()
            self.playerTurnSignal.emit(2)
        self.clicked_player = ""

    def _animateTurnStatus2(self):
        self.anim_groupstate = QtCore.QParallelAnimationGroup()

        self.anim_groupstate.addAnimation(self.animateWidgetMove(self.status_game_label, 400, 0, 1000, QEasingCurve.InExpo))
        if self.the_game.game_states.player == 1:
            print("MASUK SINI CUIY11")
            self.anim_groupstate.finished.connect(self.the_game.playGameAi)
        else:
            print("MASUK SINI CUIY")
        self.anim_groupstate.start()
        pass

    def animateTurnStatus(self):
        self.anim_groupstatus = QtCore.QParallelAnimationGroup()
        # print("MASUK SINI CUIY")
        self.anim_groupstatus.addAnimation(self.animateWidgetMove(self.status_game_label,400,0,300,QEasingCurve.OutExpo))
        self.anim_groupstatus.finished.connect(self._animateTurnStatus2)
        self.anim_groupstatus.start()
        pass

    @Slot(int)
    def turnStatusShow(self, turn):
        if turn == 1 :
            turn_img = QPixmap("Assets/Background dll/AITurn.png")
        else:
            turn_img = QPixmap("Assets/Background dll/YourTurn.png")

        self.moveWidgetTo(self.status_game_label,-800,0)
        self.status_game_label.setPixmap(turn_img)
        self.status_game_label.setText("")
        self.status_game_label.show()
        self.status_game_label.raise_()

        self.animateTurnStatus()

    def scaleWidgetTo(self, widget:QLabel, to_s):
        widget.setGeometry(QRect(widget.x(), widget.y(), widget.width()*to_s, widget.height()*to_s))

    def moveWidgetTo(self, widget:QLabel, to_x, to_y):
        widget.setGeometry(QRect(widget.x()+to_x, widget.y()+to_y, widget.width(), widget.height()))

    def showHandAnimation(self):
        self.anim_group = QtCore.QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animateWidgetMove(self.player_left, 0, -300, 1000, QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.player_right, 0, -300, 1000, QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.ai_left, 0, 300, 1000, QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.ai_right, 0, 300, 1000, QEasingCurve.InOutExpo))
        self.anim_group.finished.connect(self.showTurnInit)
        self.anim_group.start()

    def showTurnInit(self):
        self.turnStatusShow(0)

    def showIngameFrame(self):
        self.home_frame.hide()
        self.ingame_frame.show()
        self.ingame_frame.raise_()

        self.moveWidgetTo(self.player_left, 0, 300)
        self.moveWidgetTo(self.player_right, 0, 300)
        self.moveWidgetTo(self.ai_left, 0, -300)
        self.moveWidgetTo(self.ai_right, 0, -300)

        self.showHandAnimation()
        # pass

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

    def playAgainClicked(self, event):
        pass

    def showAgainHomeAnimation(self):
        self.anim_group = QtCore.QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animateWidgetMove(self.start_button, 0, -300, 1000, QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.exit_button, 0, -100, 1000, QEasingCurve.InOutExpo))
        self.anim_group.addAnimation(self.animateWidgetMove(self.logo_label, 0, 400, 1300, QEasingCurve.InBounce))
        self.anim_group.start()
        pass

    def menuClicked(self, event):
        self.audio_lose.stop()
        self.audio_main_menu.play()
        print("MENU CLICKED")
        self.changeAiLeftHandTo(1)
        self.changeAiRightHandTo(1)
        self.changePlayerLeftHandTo(1)
        self.changePlayerRightHandTo(1)
        self.the_game.resetState()
        self.lose_frame.hide()
        self.ingame_frame.hide()
        self.home_frame.show()
        self.home_frame.raise_()
        self.clicked_player = ""
        self.showAgainHomeAnimation()
    pass

    def label_moveClicked(self, event):
        # print("EMIT CLICK MOVE")
        self.oldPos = event.globalPos()

    def label_moveMove(self, event):
        # print("EMIT MOVE")
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