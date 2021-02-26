# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authentication.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import behavior

class Ui_authentication(QtWidgets.QDialog):
    def setupUi(self, authentication):
        super().__init__()
        authentication.setObjectName("authentication")
        authentication.resize(400, 600)
        authentication.setMinimumSize(QtCore.QSize(400, 600))
        authentication.setMaximumSize(QtCore.QSize(400, 600))
        self.authentication_Label = QtWidgets.QLabel(authentication)
        self.authentication_Label.setGeometry(QtCore.QRect(90, 80, 220, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.authentication_Label.setFont(font)
        self.authentication_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.authentication_Label.setObjectName("authentication_Label")
        self.authentication_reminder_Label = QtWidgets.QLabel(authentication)
        self.authentication_reminder_Label.setGeometry(QtCore.QRect(80, 170, 251, 171))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.authentication_reminder_Label.setFont(font)
        self.authentication_reminder_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.authentication_reminder_Label.setWordWrap(True)
        self.authentication_reminder_Label.setObjectName("authentication_reminder_Label")
        self.start_pushButton = QtWidgets.QPushButton(authentication)
        self.start_pushButton.setGeometry(QtCore.QRect(160, 460, 60, 60))
        self.start_pushButton.setObjectName("start_pushButton")
        self.back_pushButton = QtWidgets.QPushButton(authentication)
        self.back_pushButton.setGeometry(QtCore.QRect(20, 20, 60, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.back_pushButton.setFont(font)
        self.back_pushButton.setObjectName("back_pushButton")
        self.layoutWidget = QtWidgets.QWidget(authentication)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 340, 321, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.num1_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(36)
        self.num1_label.setFont(font)
        self.num1_label.setObjectName("num1_label")
        self.horizontalLayout.addWidget(self.num1_label)
        self.num2_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(36)
        self.num2_label.setFont(font)
        self.num2_label.setObjectName("num2_label")
        self.horizontalLayout.addWidget(self.num2_label)
        self.num3_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(36)
        self.num3_label.setFont(font)
        self.num3_label.setObjectName("num3_label")
        self.horizontalLayout.addWidget(self.num3_label)
        self.num4_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(36)
        self.num4_label.setFont(font)
        self.num4_label.setObjectName("num4_label")
        self.horizontalLayout.addWidget(self.num4_label)

        self.retranslateUi(authentication)
        QtCore.QMetaObject.connectSlotsByName(authentication)

        # success and fail
        self.success_ui = Ui_success()
        self.success_ui.setupUi(self.success_ui)
        self.fail_ui = Ui_fail()
        self.fail_ui.setupUi(self.fail_ui)

    def retranslateUi(self, authentication):
        _translate = QtCore.QCoreApplication.translate
        authentication.setWindowTitle(_translate("authentication", "Voiceprint Recognition"))
        self.authentication_Label.setText(_translate("authentication", "用户验证"))
        self.authentication_reminder_Label.setText(_translate("authentication", "请对准摄像头\n"
                                                                                "说出以下数字"))
        self.start_pushButton.setText(_translate("authentication", "开始"))
        self.back_pushButton.setText(_translate("authentication", "返回"))
        self.num1_label.setText(_translate("authentication", "2"))
        self.num2_label.setText(_translate("authentication", "2"))
        self.num3_label.setText(_translate("authentication", "2"))
        self.num4_label.setText(_translate("authentication", "2"))

    # authentication
    def authenticate(self):
        self.num_generate()

        self.authenticate_record()
        result = self.compare()

        if result:
            self.success_ui.show()  # 不用exec_ 因为这样只能通过右上角关闭键关闭
            self.success_ui.back_pushButton.clicked.connect(self.success_ui.close)
            behavior.open_door()
        else:
            self.fail_ui.show()
            self.fail_ui.back_pushButton.clicked.connect(self.fail_ui.close)

    def num_generate(self):
        import random
        random_num = []
        for i in range(4):
            num = random.randint(0, 9)
            if num == 1:
                continue
            else:
                random_num.append(num)
                i += 1
        return random_num

    def authenticate_record(self):
        pass

    def compare(self):
        return True
        pass


class Ui_success(QtWidgets.QDialog):
    def setupUi(self, success):
        super().__init__()
        success.setObjectName("success")
        success.resize(400, 600)
        success.setMinimumSize(QtCore.QSize(400, 600))
        success.setMaximumSize(QtCore.QSize(400, 600))
        self.result_Label = QtWidgets.QLabel(success)
        self.result_Label.setGeometry(QtCore.QRect(90, 80, 220, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.result_Label.setFont(font)
        self.result_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.result_Label.setObjectName("result_Label")
        self.success_Label = QtWidgets.QLabel(success)
        self.success_Label.setGeometry(QtCore.QRect(60, 190, 271, 171))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.success_Label.setFont(font)
        self.success_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.success_Label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.success_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.success_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.success_Label.setWordWrap(True)
        self.success_Label.setObjectName("success_Label")
        self.back_pushButton = QtWidgets.QPushButton(success)
        self.back_pushButton.setGeometry(QtCore.QRect(160, 440, 60, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.back_pushButton.setFont(font)
        self.back_pushButton.setObjectName("back_pushButton")
        self.success_Label_2 = QtWidgets.QLabel(success)
        self.success_Label_2.setGeometry(QtCore.QRect(60, 370, 271, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.success_Label_2.setFont(font)
        self.success_Label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.success_Label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.success_Label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.success_Label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.success_Label_2.setWordWrap(True)
        self.success_Label_2.setObjectName("success_Label_2")

        self.retranslateUi(success)
        QtCore.QMetaObject.connectSlotsByName(success)

    def retranslateUi(self, success):
        _translate = QtCore.QCoreApplication.translate
        success.setWindowTitle(_translate("success", "Voiceprint Recognition"))
        self.result_Label.setText(_translate("success", "识别结果"))
        self.success_Label.setText(_translate("success", "识别成功\n"
                                                         "\n"
                                                         "门已自动打开"))
        self.back_pushButton.setText(_translate("success", "返回"))


class Ui_fail(QtWidgets.QDialog):
    def setupUi(self, fail):
        super().__init__()
        fail.setObjectName("fail")
        fail.resize(400, 600)
        fail.setMinimumSize(QtCore.QSize(400, 600))
        fail.setMaximumSize(QtCore.QSize(400, 600))
        self.result_Label = QtWidgets.QLabel(fail)
        self.result_Label.setGeometry(QtCore.QRect(90, 80, 220, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.result_Label.setFont(font)
        self.result_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.result_Label.setObjectName("result_Label")
        self.fail_Label = QtWidgets.QLabel(fail)
        self.fail_Label.setGeometry(QtCore.QRect(70, 200, 251, 171))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.fail_Label.setFont(font)
        self.fail_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fail_Label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fail_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fail_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.fail_Label.setWordWrap(True)
        self.fail_Label.setObjectName("fail_Label")
        self.back_pushButton = QtWidgets.QPushButton(fail)
        self.back_pushButton.setGeometry(QtCore.QRect(160, 440, 60, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.back_pushButton.setFont(font)
        self.back_pushButton.setObjectName("back_pushButton")

        self.retranslateUi(fail)
        QtCore.QMetaObject.connectSlotsByName(fail)

    def retranslateUi(self, fail):
        _translate = QtCore.QCoreApplication.translate
        fail.setWindowTitle(_translate("fail", "Voiceprint Recognition"))
        self.result_Label.setText(_translate("fail", "识别结果"))
        self.fail_Label.setText(_translate("fail", "对不起\n"
                                                   "\n"
                                                   "非注册用户"))
        self.back_pushButton.setText(_translate("fail", "返回"))