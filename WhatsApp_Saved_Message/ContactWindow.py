# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contact.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 324)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/1705653353012.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(90, 0))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.contact_list = QtWidgets.QTableWidget(self.widget)
        self.contact_list.setMinimumSize(QtCore.QSize(0, 0))
        self.contact_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.contact_list.setObjectName("contact_list")
        self.contact_list.setColumnCount(2)
        self.contact_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.contact_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.contact_list.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.contact_list, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.widget)
        self.delete_button.setMaximumSize(QtCore.QSize(60, 16777215))
        self.delete_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/1705653353528.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setIconSize(QtCore.QSize(30, 30))
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 1, 1, 1, 1)
        self.insert_button = QtWidgets.QPushButton(self.widget)
        self.insert_button.setMaximumSize(QtCore.QSize(60, 16777215))
        self.insert_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.insert_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/1705653353549.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insert_button.setIcon(icon2)
        self.insert_button.setIconSize(QtCore.QSize(30, 30))
        self.insert_button.setObjectName("insert_button")
        self.gridLayout.addWidget(self.insert_button, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Contact"))
        item = self.contact_list.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Tel number"))
        item = self.contact_list.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Person"))
        self.insert_button.setToolTip(_translate("Form", "add person"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
