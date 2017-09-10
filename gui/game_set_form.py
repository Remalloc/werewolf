# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_set_form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GameSetForm(object):
    def setupUi(self, GameSetForm):
        GameSetForm.setObjectName("GameSetForm")
        GameSetForm.resize(473, 421)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo-black"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GameSetForm.setWindowIcon(icon)
        self.mainLayout = QtWidgets.QGridLayout(GameSetForm)
        self.mainLayout.setObjectName("mainLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.totalSetLayout = QtWidgets.QHBoxLayout()
        self.totalSetLayout.setObjectName("totalSetLayout")
        self.totalLabel = QtWidgets.QLabel(GameSetForm)
        self.totalLabel.setObjectName("totalLabel")
        self.totalSetLayout.addWidget(self.totalLabel)
        self.totalSetSpinBox = QtWidgets.QSpinBox(GameSetForm)
        self.totalSetSpinBox.setMinimum(1)
        self.totalSetSpinBox.setMaximum(12)
        self.totalSetSpinBox.setObjectName("totalSetSpinBox")
        self.totalSetLayout.addWidget(self.totalSetSpinBox)
        self.totalSetSlider = QtWidgets.QSlider(GameSetForm)
        self.totalSetSlider.setMinimum(1)
        self.totalSetSlider.setMaximum(12)
        self.totalSetSlider.setOrientation(QtCore.Qt.Horizontal)
        self.totalSetSlider.setObjectName("totalSetSlider")
        self.totalSetLayout.addWidget(self.totalSetSlider)
        self.verticalLayout.addLayout(self.totalSetLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listLabel = QtWidgets.QLabel(GameSetForm)
        self.listLabel.setObjectName("listLabel")
        self.horizontalLayout_2.addWidget(self.listLabel)
        self.listLabel_2 = QtWidgets.QLabel(GameSetForm)
        self.listLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.listLabel_2.setObjectName("listLabel_2")
        self.horizontalLayout_2.addWidget(self.listLabel_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.playerSetLayout = QtWidgets.QHBoxLayout()
        self.playerSetLayout.setObjectName("playerSetLayout")
        self.allRoleList = QtWidgets.QListWidget(GameSetForm)
        self.allRoleList.setObjectName("allRoleList")
        self.playerSetLayout.addWidget(self.allRoleList)
        self.controlLayout = QtWidgets.QVBoxLayout()
        self.controlLayout.setObjectName("controlLayout")
        self.rightButton = QtWidgets.QPushButton(GameSetForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightButton.sizePolicy().hasHeightForWidth())
        self.rightButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.rightButton.setFont(font)
        self.rightButton.setObjectName("rightButton")
        self.controlLayout.addWidget(self.rightButton)
        self.leftButton = QtWidgets.QPushButton(GameSetForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftButton.sizePolicy().hasHeightForWidth())
        self.leftButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.leftButton.setFont(font)
        self.leftButton.setObjectName("leftButton")
        self.controlLayout.addWidget(self.leftButton)
        self.addButton = QtWidgets.QPushButton(GameSetForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.controlLayout.addWidget(self.addButton)
        self.delButton = QtWidgets.QPushButton(GameSetForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delButton.sizePolicy().hasHeightForWidth())
        self.delButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.delButton.setFont(font)
        self.delButton.setObjectName("delButton")
        self.controlLayout.addWidget(self.delButton)
        self.playerSetLayout.addLayout(self.controlLayout)
        self.selectRoleList = QtWidgets.QListWidget(GameSetForm)
        self.selectRoleList.setObjectName("selectRoleList")
        self.playerSetLayout.addWidget(self.selectRoleList)
        self.verticalLayout.addLayout(self.playerSetLayout)
        self.resultLayout = QtWidgets.QHBoxLayout()
        self.resultLayout.setObjectName("resultLayout")
        self.defaultButton = QtWidgets.QPushButton(GameSetForm)
        self.defaultButton.setObjectName("defaultButton")
        self.resultLayout.addWidget(self.defaultButton)
        self.determineButton = QtWidgets.QPushButton(GameSetForm)
        self.determineButton.setObjectName("determineButton")
        self.resultLayout.addWidget(self.determineButton)
        self.verticalLayout.addLayout(self.resultLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.mainLayout.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(GameSetForm)
        self.totalSetSlider.valueChanged['int'].connect(self.totalSetSpinBox.setValue)
        self.totalSetSpinBox.valueChanged['int'].connect(self.totalSetSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(GameSetForm)

    def retranslateUi(self, GameSetForm):
        _translate = QtCore.QCoreApplication.translate
        GameSetForm.setWindowTitle(_translate("GameSetForm", "新建对局"))
        self.totalLabel.setText(_translate("GameSetForm", "玩家总数"))
        self.listLabel.setText(_translate("GameSetForm", "所有角色类型"))
        self.listLabel_2.setText(_translate("GameSetForm", "选择角色类型"))
        self.rightButton.setText(_translate("GameSetForm", ">>"))
        self.leftButton.setText(_translate("GameSetForm", "<<"))
        self.addButton.setText(_translate("GameSetForm", "+"))
        self.delButton.setText(_translate("GameSetForm", "-"))
        self.defaultButton.setText(_translate("GameSetForm", "默认设置"))
        self.determineButton.setText(_translate("GameSetForm", "确定"))

import gui.img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameSetForm = QtWidgets.QWidget()
    ui = Ui_GameSetForm()
    ui.setupUi(GameSetForm)
    GameSetForm.show()
    sys.exit(app.exec_())

