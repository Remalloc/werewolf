# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 590)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo-black"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.playerLayout = QtWidgets.QGridLayout()
        self.playerLayout.setObjectName("playerLayout")
        self.playerLayout_1 = QtWidgets.QVBoxLayout()
        self.playerLayout_1.setObjectName("playerLayout_1")
        self.playerButton_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_1.sizePolicy().hasHeightForWidth())
        self.playerButton_1.setSizePolicy(sizePolicy)
        self.playerButton_1.setText("")
        self.playerButton_1.setObjectName("playerButton_1")
        self.playerLayout_1.addWidget(self.playerButton_1)
        self.playerLabel_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_1.sizePolicy().hasHeightForWidth())
        self.playerLabel_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_1.setFont(font)
        self.playerLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_1.setObjectName("playerLabel_1")
        self.playerLayout_1.addWidget(self.playerLabel_1)
        self.playerLayout.addLayout(self.playerLayout_1, 1, 0, 1, 1)
        self.playerLayout_7 = QtWidgets.QVBoxLayout()
        self.playerLayout_7.setObjectName("playerLayout_7")
        self.playerButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_7.sizePolicy().hasHeightForWidth())
        self.playerButton_7.setSizePolicy(sizePolicy)
        self.playerButton_7.setText("")
        self.playerButton_7.setObjectName("playerButton_7")
        self.playerLayout_7.addWidget(self.playerButton_7)
        self.playerLabel_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_7.sizePolicy().hasHeightForWidth())
        self.playerLabel_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_7.setFont(font)
        self.playerLabel_7.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_7.setObjectName("playerLabel_7")
        self.playerLayout_7.addWidget(self.playerLabel_7)
        self.playerLayout.addLayout(self.playerLayout_7, 2, 2, 1, 1)
        self.playerLayout_8 = QtWidgets.QVBoxLayout()
        self.playerLayout_8.setObjectName("playerLayout_8")
        self.playerButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_8.sizePolicy().hasHeightForWidth())
        self.playerButton_8.setSizePolicy(sizePolicy)
        self.playerButton_8.setText("")
        self.playerButton_8.setObjectName("playerButton_8")
        self.playerLayout_8.addWidget(self.playerButton_8)
        self.playerLabel_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_8.sizePolicy().hasHeightForWidth())
        self.playerLabel_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_8.setFont(font)
        self.playerLabel_8.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_8.setObjectName("playerLabel_8")
        self.playerLayout_8.addWidget(self.playerLabel_8)
        self.playerLayout.addLayout(self.playerLayout_8, 2, 3, 1, 1)
        self.playerLayout_3 = QtWidgets.QVBoxLayout()
        self.playerLayout_3.setObjectName("playerLayout_3")
        self.playerButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_3.sizePolicy().hasHeightForWidth())
        self.playerButton_3.setSizePolicy(sizePolicy)
        self.playerButton_3.setText("")
        self.playerButton_3.setObjectName("playerButton_3")
        self.playerLayout_3.addWidget(self.playerButton_3)
        self.playerLabel_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_3.sizePolicy().hasHeightForWidth())
        self.playerLabel_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_3.setFont(font)
        self.playerLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_3.setObjectName("playerLabel_3")
        self.playerLayout_3.addWidget(self.playerLabel_3)
        self.playerLayout.addLayout(self.playerLayout_3, 1, 2, 1, 1)
        self.playerLayout_5 = QtWidgets.QVBoxLayout()
        self.playerLayout_5.setObjectName("playerLayout_5")
        self.playerButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_5.sizePolicy().hasHeightForWidth())
        self.playerButton_5.setSizePolicy(sizePolicy)
        self.playerButton_5.setText("")
        self.playerButton_5.setObjectName("playerButton_5")
        self.playerLayout_5.addWidget(self.playerButton_5)
        self.playerLabel_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_5.sizePolicy().hasHeightForWidth())
        self.playerLabel_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_5.setFont(font)
        self.playerLabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_5.setObjectName("playerLabel_5")
        self.playerLayout_5.addWidget(self.playerLabel_5)
        self.playerLayout.addLayout(self.playerLayout_5, 2, 0, 1, 1)
        self.playerLayout_6 = QtWidgets.QVBoxLayout()
        self.playerLayout_6.setObjectName("playerLayout_6")
        self.playerButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_6.sizePolicy().hasHeightForWidth())
        self.playerButton_6.setSizePolicy(sizePolicy)
        self.playerButton_6.setText("")
        self.playerButton_6.setObjectName("playerButton_6")
        self.playerLayout_6.addWidget(self.playerButton_6)
        self.playerLabel_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_6.sizePolicy().hasHeightForWidth())
        self.playerLabel_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_6.setFont(font)
        self.playerLabel_6.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_6.setObjectName("playerLabel_6")
        self.playerLayout_6.addWidget(self.playerLabel_6)
        self.playerLayout.addLayout(self.playerLayout_6, 2, 1, 1, 1)
        self.playerLayout_4 = QtWidgets.QVBoxLayout()
        self.playerLayout_4.setObjectName("playerLayout_4")
        self.playerButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_4.sizePolicy().hasHeightForWidth())
        self.playerButton_4.setSizePolicy(sizePolicy)
        self.playerButton_4.setText("")
        self.playerButton_4.setObjectName("playerButton_4")
        self.playerLayout_4.addWidget(self.playerButton_4)
        self.playerLabel_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_4.sizePolicy().hasHeightForWidth())
        self.playerLabel_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_4.setFont(font)
        self.playerLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_4.setObjectName("playerLabel_4")
        self.playerLayout_4.addWidget(self.playerLabel_4)
        self.playerLayout.addLayout(self.playerLayout_4, 1, 3, 1, 1)
        self.playerLayout_2 = QtWidgets.QVBoxLayout()
        self.playerLayout_2.setObjectName("playerLayout_2")
        self.playerButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_2.sizePolicy().hasHeightForWidth())
        self.playerButton_2.setSizePolicy(sizePolicy)
        self.playerButton_2.setText("")
        self.playerButton_2.setObjectName("playerButton_2")
        self.playerLayout_2.addWidget(self.playerButton_2)
        self.playerLabel_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_2.sizePolicy().hasHeightForWidth())
        self.playerLabel_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_2.setFont(font)
        self.playerLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_2.setObjectName("playerLabel_2")
        self.playerLayout_2.addWidget(self.playerLabel_2)
        self.playerLayout.addLayout(self.playerLayout_2, 1, 1, 1, 1)
        self.playerLayout_9 = QtWidgets.QVBoxLayout()
        self.playerLayout_9.setObjectName("playerLayout_9")
        self.playerButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_9.sizePolicy().hasHeightForWidth())
        self.playerButton_9.setSizePolicy(sizePolicy)
        self.playerButton_9.setText("")
        self.playerButton_9.setObjectName("playerButton_9")
        self.playerLayout_9.addWidget(self.playerButton_9)
        self.playerLabel_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_9.sizePolicy().hasHeightForWidth())
        self.playerLabel_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_9.setFont(font)
        self.playerLabel_9.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_9.setObjectName("playerLabel_9")
        self.playerLayout_9.addWidget(self.playerLabel_9)
        self.playerLayout.addLayout(self.playerLayout_9, 3, 0, 1, 1)
        self.playerLayout_10 = QtWidgets.QVBoxLayout()
        self.playerLayout_10.setObjectName("playerLayout_10")
        self.playerButton_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_10.sizePolicy().hasHeightForWidth())
        self.playerButton_10.setSizePolicy(sizePolicy)
        self.playerButton_10.setText("")
        self.playerButton_10.setObjectName("playerButton_10")
        self.playerLayout_10.addWidget(self.playerButton_10)
        self.playerLabel_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_10.sizePolicy().hasHeightForWidth())
        self.playerLabel_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_10.setFont(font)
        self.playerLabel_10.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_10.setObjectName("playerLabel_10")
        self.playerLayout_10.addWidget(self.playerLabel_10)
        self.playerLayout.addLayout(self.playerLayout_10, 3, 1, 1, 1)
        self.playerLayout_11 = QtWidgets.QVBoxLayout()
        self.playerLayout_11.setObjectName("playerLayout_11")
        self.playerButton_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_11.sizePolicy().hasHeightForWidth())
        self.playerButton_11.setSizePolicy(sizePolicy)
        self.playerButton_11.setText("")
        self.playerButton_11.setObjectName("playerButton_11")
        self.playerLayout_11.addWidget(self.playerButton_11)
        self.playerLabel_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_11.sizePolicy().hasHeightForWidth())
        self.playerLabel_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_11.setFont(font)
        self.playerLabel_11.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_11.setObjectName("playerLabel_11")
        self.playerLayout_11.addWidget(self.playerLabel_11)
        self.playerLayout.addLayout(self.playerLayout_11, 3, 2, 1, 1)
        self.playerLayout_12 = QtWidgets.QVBoxLayout()
        self.playerLayout_12.setObjectName("playerLayout_12")
        self.playerButton_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerButton_12.sizePolicy().hasHeightForWidth())
        self.playerButton_12.setSizePolicy(sizePolicy)
        self.playerButton_12.setText("")
        self.playerButton_12.setObjectName("playerButton_12")
        self.playerLayout_12.addWidget(self.playerButton_12)
        self.playerLabel_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLabel_12.sizePolicy().hasHeightForWidth())
        self.playerLabel_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.playerLabel_12.setFont(font)
        self.playerLabel_12.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel_12.setObjectName("playerLabel_12")
        self.playerLayout_12.addWidget(self.playerLabel_12)
        self.playerLayout.addLayout(self.playerLayout_12, 3, 3, 1, 1)
        self.gridLayout_2.addLayout(self.playerLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout_2.addWidget(self.infoLabel)
        self.infoList = QtWidgets.QListWidget(self.centralwidget)
        self.infoList.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoList.sizePolicy().hasHeightForWidth())
        self.infoList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.infoList.setFont(font)
        self.infoList.setObjectName("infoList")
        self.verticalLayout_2.addWidget(self.infoList)
        self.recordLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordLabel.sizePolicy().hasHeightForWidth())
        self.recordLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordLabel.setFont(font)
        self.recordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.recordLabel.setObjectName("recordLabel")
        self.verticalLayout_2.addWidget(self.recordLabel)
        self.recordList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordList.sizePolicy().hasHeightForWidth())
        self.recordList.setSizePolicy(sizePolicy)
        self.recordList.setObjectName("recordList")
        self.verticalLayout_2.addWidget(self.recordList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filterButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterButton.sizePolicy().hasHeightForWidth())
        self.filterButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.filterButton.setFont(font)
        self.filterButton.setObjectName("filterButton")
        self.horizontalLayout.addWidget(self.filterButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.newGame = QtWidgets.QAction(MainWindow)
        self.newGame.setObjectName("newGame")
        self.teamAnalysis = QtWidgets.QAction(MainWindow)
        self.teamAnalysis.setObjectName("teamAnalysis")
        self.viewVote = QtWidgets.QAction(MainWindow)
        self.viewVote.setObjectName("viewVote")
        self.setDefault = QtWidgets.QAction(MainWindow)
        self.setDefault.setChecked(False)
        self.setDefault.setObjectName("setDefault")
        self.cleanMode = QtWidgets.QAction(MainWindow)
        self.cleanMode.setCheckable(True)
        self.cleanMode.setChecked(False)
        self.cleanMode.setObjectName("cleanMode")
        self.contactAuthor = QtWidgets.QAction(MainWindow)
        self.contactAuthor.setObjectName("contactAuthor")
        self.softwareInfo = QtWidgets.QAction(MainWindow)
        self.softwareInfo.setObjectName("softwareInfo")
        self.menuGame.addAction(self.newGame)
        self.menuGame.addAction(self.teamAnalysis)
        self.menuGame.addAction(self.viewVote)
        self.menu.addAction(self.setDefault)
        self.menu.addAction(self.cleanMode)
        self.menu_2.addAction(self.contactAuthor)
        self.menu_2.addAction(self.softwareInfo)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "狼人杀记牌器"))
        self.playerLabel_1.setText(_translate("MainWindow", "1号"))
        self.playerLabel_7.setText(_translate("MainWindow", "7号"))
        self.playerLabel_8.setText(_translate("MainWindow", "8号"))
        self.playerLabel_3.setText(_translate("MainWindow", "3号"))
        self.playerLabel_5.setText(_translate("MainWindow", "5号"))
        self.playerLabel_6.setText(_translate("MainWindow", "6号"))
        self.playerLabel_4.setText(_translate("MainWindow", "4号"))
        self.playerLabel_2.setText(_translate("MainWindow", "2号"))
        self.playerLabel_9.setText(_translate("MainWindow", "9号"))
        self.playerLabel_10.setText(_translate("MainWindow", "10号"))
        self.playerLabel_11.setText(_translate("MainWindow", "11号"))
        self.playerLabel_12.setText(_translate("MainWindow", "12号"))
        self.infoLabel.setText(_translate("MainWindow", "玩家信息"))
        self.recordLabel.setText(_translate("MainWindow", "行为记录"))
        self.filterButton.setText(_translate("MainWindow", "筛选"))
        self.menuGame.setTitle(_translate("MainWindow", "对局"))
        self.menu.setTitle(_translate("MainWindow", "高级"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpenFile.setText(_translate("MainWindow", "Open"))
        self.newGame.setText(_translate("MainWindow", "新建对局"))
        self.teamAnalysis.setText(_translate("MainWindow", "团队分析"))
        self.viewVote.setText(_translate("MainWindow", "查看投票"))
        self.setDefault.setText(_translate("MainWindow", "默认值设置"))
        self.cleanMode.setText(_translate("MainWindow", "纯净模式"))
        self.contactAuthor.setText(_translate("MainWindow", "联系作者"))
        self.softwareInfo.setText(_translate("MainWindow", "软件信息"))

import gui.img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

