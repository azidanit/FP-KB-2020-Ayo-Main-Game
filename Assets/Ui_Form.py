# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(QObject):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(384, 670)
        self.home_frame = QFrame(Form)
        self.home_frame.setObjectName(u"home_frame")
        self.home_frame.setGeometry(QRect(54, 253, 271, 171))
        self.home_frame.setFrameShape(QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.home_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.start_button = QPushButton(self.home_frame)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 55))

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.start_button)

        self.verticalSpacer = QSpacerItem(20, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.verticalSpacer)

        self.exit_button = QPushButton(self.home_frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(0, 55))

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.exit_button)

        self.ingame_frame = QFrame(Form)
        self.ingame_frame.setObjectName(u"ingame_frame")
        self.ingame_frame.setGeometry(QRect(10, 0, 361, 671))
        self.ingame_frame.setFrameShape(QFrame.StyledPanel)
        self.ingame_frame.setFrameShadow(QFrame.Raised)
        self.ai_left = QLabel(self.ingame_frame)
        self.ai_left.setObjectName(u"ai_left")
        self.ai_left.setGeometry(QRect(8, 1, 161, 271))
        font = QFont()
        font.setPointSize(48)
        self.ai_left.setFont(font)
        self.ai_left.setAlignment(Qt.AlignCenter)
        self.player_left = QLabel(self.ingame_frame)
        self.player_left.setObjectName(u"player_left")
        self.player_left.setGeometry(QRect(8, 399, 161, 271))
        self.player_left.setFont(font)
        self.player_left.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.ingame_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 300, 341, 91))
        font1 = QFont()
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.ai_right = QLabel(self.ingame_frame)
        self.ai_right.setObjectName(u"ai_right")
        self.ai_right.setGeometry(QRect(190, 1, 161, 271))
        self.ai_right.setFont(font)
        self.ai_right.setAlignment(Qt.AlignCenter)
        self.player_right = QLabel(self.ingame_frame)
        self.player_right.setObjectName(u"player_right")
        self.player_right.setGeometry(QRect(190, 399, 161, 271))
        self.player_right.setFont(font)
        self.player_right.setAlignment(Qt.AlignCenter)
        self.ingame_frame.raise_()
        self.home_frame.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.start_button.setText(QCoreApplication.translate("Form", u"START", None))
        self.exit_button.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.ai_left.setText(QCoreApplication.translate("Form", u"1", None))
        self.player_left.setText(QCoreApplication.translate("Form", u"1", None))
        self.label.setText(QCoreApplication.translate("Form", u"PILIH TANGAN LAWAN", None))
        self.ai_right.setText(QCoreApplication.translate("Form", u"1", None))
        self.player_right.setText(QCoreApplication.translate("Form", u"1", None))
    # retranslateUi

