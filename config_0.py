# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setings_0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_0(object):
    def setupUi(self, Dialog_0):
        Dialog_0.setObjectName("Dialog_0")
        Dialog_0.resize(301, 100)
        Dialog_0.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label = QtWidgets.QLabel(Dialog_0)
        self.label.setGeometry(QtCore.QRect(10, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(3)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_0)

    def retranslateUi(self, Dialog_0):
        _translate = QtCore.QCoreApplication.translate
        Dialog_0.setWindowTitle(_translate("Dialog_0", "Таблиця збережина"))
        self.label.setText(_translate("Dialog_0", "         Таблиця збережина"))


