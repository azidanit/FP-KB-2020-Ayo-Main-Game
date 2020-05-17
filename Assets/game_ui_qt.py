# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_ui_qt.ui'
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


class Ui_Form(QMainWindow):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(380, 670)
        self.home_frame = QFrame(Form)
        self.home_frame.setObjectName(u"home_frame")
        self.home_frame.setGeometry(QRect(20, -7, 351, 681))
        self.home_frame.setFrameShape(QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.home_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer = QSpacerItem(20, 22, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 144, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.logo_label = QLabel(self.home_frame)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMinimumSize(QSize(0, 80))

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.logo_label)

        self.exit_button = QLabel(self.home_frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(0, 65))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.exit_button)

        self.verticalSpacer_3 = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.start_button = QLabel(self.home_frame)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 65))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.start_button)

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
        self.status_game_label = QLabel(self.ingame_frame)
        self.status_game_label.setObjectName(u"status_game_label")
        self.status_game_label.setGeometry(QRect(10, 301, 341, 91))
        font1 = QFont()
        font1.setPointSize(22)
        self.status_game_label.setFont(font1)
        self.status_game_label.setAlignment(Qt.AlignCenter)
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
        self.exit_button_ingame = QLabel(self.ingame_frame)
        self.exit_button_ingame.setObjectName(u"exit_button_ingame")
        self.exit_button_ingame.setGeometry(QRect(0, 330, 91, 31))
        self.bg_label = QLabel(Form)
        self.bg_label.setObjectName(u"bg_label")
        self.bg_label.setGeometry(QRect(0, 0, 384, 680))
        self.move_label = QLabel(Form)
        self.move_label.setObjectName(u"move_label")
        self.move_label.setGeometry(QRect(0, 0, 401, 20))
        self.lose_frame = QFrame(Form)
        self.lose_frame.setObjectName(u"lose_frame")
        self.lose_frame.setGeometry(QRect(0, 0, 381, 681))
        self.lose_frame.setFrameShape(QFrame.StyledPanel)
        self.lose_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.lose_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lose_label = QLabel(self.lose_frame)
        self.lose_label.setObjectName(u"lose_label")
        self.lose_label.setMinimumSize(QSize(0, 120))

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.lose_label)

        self.play_again_label = QLabel(self.lose_frame)
        self.play_again_label.setObjectName(u"play_again_label")
        self.play_again_label.setMinimumSize(QSize(0, 66))

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.play_again_label)

        self.menu_label = QLabel(self.lose_frame)
        self.menu_label.setObjectName(u"menu_label")
        self.menu_label.setMinimumSize(QSize(0, 65))

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.menu_label)

        self.verticalSpacer_4 = QSpacerItem(20, 170, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.verticalSpacer_5 = QSpacerItem(20, 170, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.bg_label.raise_()
        self.ingame_frame.raise_()
        self.home_frame.raise_()
        self.move_label.raise_()
        self.lose_frame.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo_label.setText(QCoreApplication.translate("Form", u"LOGO", None))
        self.exit_button.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.start_button.setText(QCoreApplication.translate("Form", u"START", None))
        self.ai_left.setText(QCoreApplication.translate("Form", u"1", None))
        self.player_left.setText(QCoreApplication.translate("Form", u"1", None))
        self.status_game_label.setText(QCoreApplication.translate("Form", u"PILIH TANGAN LAWAN", None))
        self.ai_right.setText(QCoreApplication.translate("Form", u"1", None))
        self.player_right.setText(QCoreApplication.translate("Form", u"1", None))
        self.exit_button_ingame.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.bg_label.setText("")
        self.move_label.setText("")
        self.lose_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.play_again_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.menu_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

