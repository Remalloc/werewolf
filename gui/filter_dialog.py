# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FliterDialog(object):
    def setupUi(self, FliterDialog):
        FliterDialog.setObjectName("FliterDialog")
        FliterDialog.resize(380, 236)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FliterDialog.sizePolicy().hasHeightForWidth())
        FliterDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo-black"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FliterDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(FliterDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.determineButton = QtWidgets.QPushButton(FliterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.determineButton.sizePolicy().hasHeightForWidth())
        self.determineButton.setSizePolicy(sizePolicy)
        self.determineButton.setObjectName("determineButton")
        self.verticalLayout.addWidget(self.determineButton)
        self.selectAllButton = QtWidgets.QPushButton(FliterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectAllButton.sizePolicy().hasHeightForWidth())
        self.selectAllButton.setSizePolicy(sizePolicy)
        self.selectAllButton.setObjectName("selectAllButton")
        self.verticalLayout.addWidget(self.selectAllButton)
        self.antiElectionButton = QtWidgets.QPushButton(FliterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.antiElectionButton.sizePolicy().hasHeightForWidth())
        self.antiElectionButton.setSizePolicy(sizePolicy)
        self.antiElectionButton.setObjectName("antiElectionButton")
        self.verticalLayout.addWidget(self.antiElectionButton)
        self.cancelButton = QtWidgets.QPushButton(FliterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setObjectName("cancelButton")
        self.verticalLayout.addWidget(self.cancelButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.playerList = QtWidgets.QGroupBox(FliterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerList.sizePolicy().hasHeightForWidth())
        self.playerList.setSizePolicy(sizePolicy)
        self.playerList.setObjectName("playerList")
        self.gridLayout.addWidget(self.playerList, 0, 0, 1, 1)

        self.retranslateUi(FliterDialog)
        QtCore.QMetaObject.connectSlotsByName(FliterDialog)

    def retranslateUi(self, FliterDialog):
        _translate = QtCore.QCoreApplication.translate
        FliterDialog.setWindowTitle(_translate("FliterDialog", "筛选"))
        self.determineButton.setText(_translate("FliterDialog", "确定"))
        self.selectAllButton.setText(_translate("FliterDialog", "全选"))
        self.antiElectionButton.setText(_translate("FliterDialog", "反选"))
        self.cancelButton.setText(_translate("FliterDialog", "取消"))
        self.playerList.setTitle(_translate("FliterDialog", "显示玩家"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FliterDialog = QtWidgets.QDialog()
    ui = Ui_FliterDialog()
    ui.setupUi(FliterDialog)
    FliterDialog.show()
    sys.exit(app.exec_())

