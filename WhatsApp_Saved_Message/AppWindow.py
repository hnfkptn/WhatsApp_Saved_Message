# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WhatsAppAutoMessage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 842)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/1705653353012.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.main_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.delete_msg_button = QtWidgets.QPushButton(self.main_page)
        self.delete_msg_button.setMinimumSize(QtCore.QSize(60, 0))
        self.delete_msg_button.setMaximumSize(QtCore.QSize(60, 60))
        self.delete_msg_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_msg_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/1705774343299.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_msg_button.setIcon(icon1)
        self.delete_msg_button.setIconSize(QtCore.QSize(30, 30))
        self.delete_msg_button.setObjectName("delete_msg_button")
        self.gridLayout_2.addWidget(self.delete_msg_button, 0, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.main_page)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.saved_message_scroll_area = QtWidgets.QScrollArea(self.groupBox)
        self.saved_message_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.saved_message_scroll_area.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.saved_message_scroll_area.setWidgetResizable(True)
        self.saved_message_scroll_area.setObjectName("saved_message_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 680, 667))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.saved_message_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.saved_message_scroll_area)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.new_person_button = QtWidgets.QPushButton(self.groupBox)
        self.new_person_button.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.new_person_button.setFont(font)
        self.new_person_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/1705774343278.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_person_button.setIcon(icon2)
        self.new_person_button.setIconSize(QtCore.QSize(30, 30))
        self.new_person_button.setObjectName("new_person_button")
        self.horizontalLayout_3.addWidget(self.new_person_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.new_message_button = QtWidgets.QPushButton(self.groupBox)
        self.new_message_button.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.new_message_button.setFont(font)
        self.new_message_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/1705774343524.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_message_button.setIcon(icon3)
        self.new_message_button.setIconSize(QtCore.QSize(30, 30))
        self.new_message_button.setObjectName("new_message_button")
        self.horizontalLayout_3.addWidget(self.new_message_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.send_button = QtWidgets.QPushButton(self.groupBox)
        self.send_button.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/1705774343.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_button.setIcon(icon4)
        self.send_button.setIconSize(QtCore.QSize(30, 30))
        self.send_button.setObjectName("send_button")
        self.horizontalLayout_3.addWidget(self.send_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 4)
        self.settings_button = QtWidgets.QPushButton(self.main_page)
        self.settings_button.setMaximumSize(QtCore.QSize(60, 60))
        self.settings_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.settings_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/1705774343451.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon5)
        self.settings_button.setIconSize(QtCore.QSize(30, 30))
        self.settings_button.setObjectName("settings_button")
        self.gridLayout_2.addWidget(self.settings_button, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.main_page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.title.setFont(font)
        self.title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 1, 1, 5)
        self.auto_time_period_radio = QtWidgets.QRadioButton(self.page_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.auto_time_period_radio.setFont(font)
        self.auto_time_period_radio.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.auto_time_period_radio.setChecked(True)
        self.auto_time_period_radio.setObjectName("auto_time_period_radio")
        self.gridLayout.addWidget(self.auto_time_period_radio, 8, 0, 1, 7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 7)
        self.label = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 2, 1, 2)
        self.decrease_person_button = QtWidgets.QPushButton(self.page_2)
        self.decrease_person_button.setMaximumSize(QtCore.QSize(60, 16777215))
        self.decrease_person_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.decrease_person_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/1705653353528.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decrease_person_button.setIcon(icon6)
        self.decrease_person_button.setIconSize(QtCore.QSize(30, 30))
        self.decrease_person_button.setObjectName("decrease_person_button")
        self.gridLayout.addWidget(self.decrease_person_button, 13, 5, 1, 1)
        self.second = QtWidgets.QSpinBox(self.page_2)
        self.second.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.second.setFont(font)
        self.second.setToolTip("")
        self.second.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.second.setMinimum(0)
        self.second.setMaximum(1800)
        self.second.setProperty("value", 0)
        self.second.setObjectName("second")
        self.gridLayout.addWidget(self.second, 6, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 17, 0, 1, 7)
        self.piece = QtWidgets.QSpinBox(self.page_2)
        self.piece.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.piece.setFont(font)
        self.piece.setToolTip("")
        self.piece.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.piece.setMinimum(1)
        self.piece.setMaximum(1000)
        self.piece.setObjectName("piece")
        self.gridLayout.addWidget(self.piece, 11, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 7)
        self.message_scroll_area = QtWidgets.QScrollArea(self.page_2)
        self.message_scroll_area.setMinimumSize(QtCore.QSize(0, 90))
        self.message_scroll_area.setStyleSheet("color: rgb(0, 0, 0);")
        self.message_scroll_area.setWidgetResizable(True)
        self.message_scroll_area.setObjectName("message_scroll_area")
        self.messages_area = QtWidgets.QWidget()
        self.messages_area.setGeometry(QtCore.QRect(0, 0, 511, 88))
        self.messages_area.setObjectName("messages_area")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.messages_area)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.message = QtWidgets.QTextEdit(self.messages_area)
        self.message.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.message.setFont(font)
        self.message.setToolTip("")
        self.message.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.message.setObjectName("message")
        self.verticalLayout_5.addWidget(self.message)
        self.message_scroll_area.setWidget(self.messages_area)
        self.gridLayout.addWidget(self.message_scroll_area, 3, 1, 1, 5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 10, 0, 1, 7)
        self.previous_button = QtWidgets.QPushButton(self.page_2)
        self.previous_button.setMinimumSize(QtCore.QSize(0, 0))
        self.previous_button.setMaximumSize(QtCore.QSize(70, 35))
        self.previous_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.previous_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/1705774342520.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_button.setIcon(icon7)
        self.previous_button.setIconSize(QtCore.QSize(35, 30))
        self.previous_button.setObjectName("previous_button")
        self.gridLayout.addWidget(self.previous_button, 0, 0, 1, 1)
        self.time_period_radio = QtWidgets.QRadioButton(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_period_radio.setFont(font)
        self.time_period_radio.setStyleSheet("")
        self.time_period_radio.setObjectName("time_period_radio")
        self.gridLayout.addWidget(self.time_period_radio, 6, 0, 1, 1)
        self.increase_message_button = QtWidgets.QPushButton(self.page_2)
        self.increase_message_button.setMaximumSize(QtCore.QSize(60, 16777215))
        self.increase_message_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.increase_message_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/1705653353549.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.increase_message_button.setIcon(icon8)
        self.increase_message_button.setIconSize(QtCore.QSize(30, 30))
        self.increase_message_button.setObjectName("increase_message_button")
        self.gridLayout.addWidget(self.increase_message_button, 3, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 12, 0, 1, 7)
        self.label_5 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 13, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 4, 0, 1, 7)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 11, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 2, 1, 2)
        self.send_button_2 = QtWidgets.QPushButton(self.page_2)
        self.send_button_2.setMinimumSize(QtCore.QSize(0, 0))
        self.send_button_2.setMaximumSize(QtCore.QSize(165, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.send_button_2.setFont(font)
        self.send_button_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.send_button_2.setIcon(icon4)
        self.send_button_2.setIconSize(QtCore.QSize(30, 30))
        self.send_button_2.setObjectName("send_button_2")
        self.gridLayout.addWidget(self.send_button_2, 18, 2, 1, 1)
        self.increase_person_button = QtWidgets.QPushButton(self.page_2)
        self.increase_person_button.setMaximumSize(QtCore.QSize(60, 16777215))
        self.increase_person_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.increase_person_button.setText("")
        self.increase_person_button.setIcon(icon8)
        self.increase_person_button.setIconSize(QtCore.QSize(30, 30))
        self.increase_person_button.setObjectName("increase_person_button")
        self.gridLayout.addWidget(self.increase_person_button, 13, 6, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.page_2)
        self.save_button.setMaximumSize(QtCore.QSize(165, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/1705774343433.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon9)
        self.save_button.setIconSize(QtCore.QSize(30, 30))
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 18, 4, 1, 1)
        self.contacts = QtWidgets.QComboBox(self.page_2)
        self.contacts.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.contacts.setFont(font)
        self.contacts.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.contacts.setObjectName("contacts")
        self.gridLayout.addWidget(self.contacts, 13, 1, 1, 4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.previous_button_2 = QtWidgets.QPushButton(self.page_3)
        self.previous_button_2.setMaximumSize(QtCore.QSize(70, 35))
        self.previous_button_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.previous_button_2.setText("")
        self.previous_button_2.setIcon(icon7)
        self.previous_button_2.setIconSize(QtCore.QSize(30, 30))
        self.previous_button_2.setObjectName("previous_button_2")
        self.horizontalLayout_4.addWidget(self.previous_button_2)
        self.label_8 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem9)
        self.label_6 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dark_green_button = QtWidgets.QPushButton(self.page_3)
        self.dark_green_button.setMinimumSize(QtCore.QSize(100, 0))
        self.dark_green_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dark_green_button.setFont(font)
        self.dark_green_button.setStyleSheet("background-color: rgb(59, 101, 105);")
        self.dark_green_button.setText("")
        self.dark_green_button.setObjectName("dark_green_button")
        self.gridLayout_3.addWidget(self.dark_green_button, 0, 0, 1, 1)
        self.grey_button = QtWidgets.QPushButton(self.page_3)
        self.grey_button.setMinimumSize(QtCore.QSize(100, 0))
        self.grey_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.grey_button.setFont(font)
        self.grey_button.setStyleSheet("background-color:  rgb(200, 200, 200);")
        self.grey_button.setText("")
        self.grey_button.setObjectName("grey_button")
        self.gridLayout_3.addWidget(self.grey_button, 1, 4, 1, 1)
        self.light_green_button = QtWidgets.QPushButton(self.page_3)
        self.light_green_button.setMinimumSize(QtCore.QSize(100, 0))
        self.light_green_button.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.light_green_button.setFont(font)
        self.light_green_button.setStyleSheet("background-color: rgb(133, 158, 156);")
        self.light_green_button.setText("")
        self.light_green_button.setObjectName("light_green_button")
        self.gridLayout_3.addWidget(self.light_green_button, 1, 0, 1, 1)
        self.beige_button = QtWidgets.QPushButton(self.page_3)
        self.beige_button.setMinimumSize(QtCore.QSize(100, 0))
        self.beige_button.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.beige_button.setFont(font)
        self.beige_button.setStyleSheet("background-color: rgb(227, 213, 203);")
        self.beige_button.setText("")
        self.beige_button.setObjectName("beige_button")
        self.gridLayout_3.addWidget(self.beige_button, 1, 1, 1, 1)
        self.brown_button = QtWidgets.QPushButton(self.page_3)
        self.brown_button.setMinimumSize(QtCore.QSize(100, 0))
        self.brown_button.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.brown_button.setFont(font)
        self.brown_button.setStyleSheet("background-color: rgb(167, 149, 120);")
        self.brown_button.setText("")
        self.brown_button.setObjectName("brown_button")
        self.gridLayout_3.addWidget(self.brown_button, 0, 1, 1, 1)
        self.pink_button = QtWidgets.QPushButton(self.page_3)
        self.pink_button.setMinimumSize(QtCore.QSize(100, 0))
        self.pink_button.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pink_button.setFont(font)
        self.pink_button.setStyleSheet("background-color: rgb(199, 147, 149);")
        self.pink_button.setText("")
        self.pink_button.setObjectName("pink_button")
        self.gridLayout_3.addWidget(self.pink_button, 0, 4, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem10)
        self.label_7 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.english_button = QtWidgets.QPushButton(self.page_3)
        self.english_button.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.english_button.setFont(font)
        self.english_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.english_button.setObjectName("english_button")
        self.horizontalLayout_2.addWidget(self.english_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem11)
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.show_contact_button = QtWidgets.QPushButton(self.page_3)
        self.show_contact_button.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.show_contact_button.setFont(font)
        self.show_contact_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.show_contact_button.setObjectName("show_contact_button")
        self.horizontalLayout_5.addWidget(self.show_contact_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem12)
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.information_button = QtWidgets.QPushButton(self.page_3)
        self.information_button.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.information_button.setFont(font)
        self.information_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.information_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.information_button.setObjectName("information_button")
        self.horizontalLayout_6.addWidget(self.information_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App"))
        self.delete_msg_button.setToolTip(_translate("MainWindow", "delete"))
        self.groupBox.setTitle(_translate("MainWindow", "Saved message"))
        self.new_person_button.setToolTip(_translate("MainWindow", "new message"))
        self.new_person_button.setText(_translate("MainWindow", "new person"))
        self.new_message_button.setToolTip(_translate("MainWindow", "new message"))
        self.new_message_button.setText(_translate("MainWindow", "new message"))
        self.send_button.setToolTip(_translate("MainWindow", "send"))
        self.send_button.setText(_translate("MainWindow", "send message"))
        self.auto_time_period_radio.setText(_translate("MainWindow", "Automatic Timer: The time to send the message is automatically\n"
" adjusted according to the lenght of the message"))
        self.label.setText(_translate("MainWindow", "Message"))
        self.label_4.setText(_translate("MainWindow", "piece"))
        self.label_9.setText(_translate("MainWindow", "Footnote: This feature applied when the number of message is more than 1"))
        self.message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.previous_button.setToolTip(_translate("MainWindow", "back"))
        self.time_period_radio.setText(_translate("MainWindow", "Standby\n"
"Time"))
        self.increase_message_button.setToolTip(_translate("MainWindow", "add person"))
        self.label_5.setText(_translate("MainWindow", "Contacts"))
        self.label_3.setText(_translate("MainWindow", "Repetition of\n"
"message"))
        self.label_13.setText(_translate("MainWindow", "Title"))
        self.label_2.setText(_translate("MainWindow", "second"))
        self.send_button_2.setToolTip(_translate("MainWindow", "send"))
        self.send_button_2.setText(_translate("MainWindow", "send message"))
        self.increase_person_button.setToolTip(_translate("MainWindow", "add person"))
        self.save_button.setToolTip(_translate("MainWindow", "save"))
        self.save_button.setText(_translate("MainWindow", "save message"))
        self.label_8.setText(_translate("MainWindow", "                          SETTINGS"))
        self.label_6.setText(_translate("MainWindow", "COLORS"))
        self.label_7.setText(_translate("MainWindow", "LANGUAGES"))
        self.english_button.setText(_translate("MainWindow", "english"))
        self.label_11.setText(_translate("MainWindow", "CONTACT"))
        self.show_contact_button.setText(_translate("MainWindow", "show contact"))
        self.label_12.setText(_translate("MainWindow", "ABOUT APP"))
        self.information_button.setText(_translate("MainWindow", "information"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
