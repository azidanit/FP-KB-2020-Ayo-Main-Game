# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Form.ui',
# licensing of 'Ui_Form.ui' applies.
#
# Created: Mon May 11 05:22:58 2020
#      by: pyside2-uic  running on PySide2 5.12.6
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 689)
        self.home_frame = QtWidgets.QFrame(Form)
        self.home_frame.setGeometry(QtCore.QRect(60, 240, 271, 171))
        self.home_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_frame.setObjectName("home_frame")
        self.formLayout = QtWidgets.QFormLayout(self.home_frame)
        self.formLayout.setObjectName("formLayout")
        self.start_button = QtWidgets.QPushButton(self.home_frame)
        self.start_button.setMinimumSize(QtCore.QSize(0, 55))
        self.start_button.setObjectName("start_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.start_button)
        self.exit_button = QtWidgets.QPushButton(self.home_frame)
        self.exit_button.setMinimumSize(QtCore.QSize(0, 55))
        self.exit_button.setObjectName("exit_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.exit_button)
        spacerItem = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.ingame_frame = QtWidgets.QFrame(Form)
        self.ingame_frame.setGeometry(QtCore.QRect(10, 10, 381, 671))
        self.ingame_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ingame_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ingame_frame.setObjectName("ingame_frame")
        self.ai_left = QtWidgets.QLabel(self.ingame_frame)
        self.ai_left.setGeometry(QtCore.QRect(20, 0, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.ai_left.setFont(font)
        self.ai_left.setAlignment(QtCore.Qt.AlignCenter)
        self.ai_left.setObjectName("ai_left")
        self.player_left = QtWidgets.QLabel(self.ingame_frame)
        self.player_left.setGeometry(QtCore.QRect(40, 530, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.player_left.setFont(font)
        self.player_left.setAlignment(QtCore.Qt.AlignCenter)
        self.player_left.setObjectName("player_left")
        self.label = QtWidgets.QLabel(self.ingame_frame)
        self.label.setGeometry(QtCore.QRect(0, 410, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ai_right = QtWidgets.QLabel(self.ingame_frame)
        self.ai_right.setGeometry(QtCore.QRect(190, 3, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.ai_right.setFont(font)
        self.ai_right.setAlignment(QtCore.Qt.AlignCenter)
        self.ai_right.setObjectName("ai_right")
        self.player_right = QtWidgets.QLabel(self.ingame_frame)
        self.player_right.setGeometry(QtCore.QRect(200, 528, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.player_right.setFont(font)
        self.player_right.setAlignment(QtCore.Qt.AlignCenter)
        self.player_right.setObjectName("player_right")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.start_button.setText(QtWidgets.QApplication.translate("Form", "START", None, -1))
        self.exit_button.setText(QtWidgets.QApplication.translate("Form", "EXIT", None, -1))
        self.ai_left.setText(QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.player_left.setText(QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "PILIH TANGAN LAWAN", None, -1))
        self.ai_right.setText(QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.player_right.setText(QtWidgets.QApplication.translate("Form", "1", None, -1))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

