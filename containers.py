# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\containers.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(924, 750)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 441, 221))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.Ship_number = QtWidgets.QLineEdit(self.groupBox)
        self.Ship_number.setGeometry(QtCore.QRect(200, 60, 191, 20))
        self.Ship_number.setObjectName("Ship_number")
        self.Ship_ip = QtWidgets.QLineEdit(self.groupBox)
        self.Ship_ip.setGeometry(QtCore.QRect(200, 110, 191, 20))
        self.Ship_ip.setObjectName("Ship_ip")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 350, 441, 241))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(30, 120, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.TM_rate = QtWidgets.QLineEdit(self.groupBox_2)
        self.TM_rate.setGeometry(QtCore.QRect(200, 60, 191, 20))
        self.TM_rate.setObjectName("TM_rate")
        self.Video_rate = QtWidgets.QLineEdit(self.groupBox_2)
        self.Video_rate.setGeometry(QtCore.QRect(200, 120, 191, 20))
        self.Video_rate.setObjectName("Video_rate")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(470, 110, 450, 221))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Source_port = QtWidgets.QLineEdit(self.groupBox_3)
        self.Source_port.setGeometry(QtCore.QRect(190, 50, 191, 20))
        self.Source_port.setObjectName("Source_port")
        self.Des_port = QtWidgets.QLineEdit(self.groupBox_3)
        self.Des_port.setGeometry(QtCore.QRect(190, 110, 191, 20))
        self.Des_port.setObjectName("Des_port")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(470, 350, 450, 241))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.Start_data = QtWidgets.QDateTimeEdit(self.groupBox_4)
        self.Start_data.setGeometry(QtCore.QRect(220, 50, 194, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Start_data.setFont(font)
        self.Start_data.setObjectName("Start_data")
        self.End_date = QtWidgets.QDateTimeEdit(self.groupBox_4)
        self.End_date.setGeometry(QtCore.QRect(220, 110, 194, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.End_date.setFont(font)
        self.End_date.setObjectName("End_date")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 60, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 630, 171, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Ship Information"))
        self.label_6.setText(_translate("Form", "Ship Hull Number"))
        self.label_7.setText(_translate("Form", "Ship IP"))
        self.groupBox_2.setTitle(_translate("Form", "Rates"))
        self.label_8.setText(_translate("Form", "TM Bit Rate"))
        self.label_9.setText(_translate("Form", "Video Bit Rate"))
        self.groupBox_3.setTitle(_translate("Form", "Ports"))
        self.label_4.setText(_translate("Form", "Source Port"))
        self.label_5.setText(_translate("Form", "Desintation Port"))
        self.groupBox_4.setTitle(_translate("Form", "Dates"))
        self.label_2.setText(_translate("Form", "Start Date/Time"))
        self.label_3.setText(_translate("Form", "End Date/Time"))
        self.label.setText(_translate("Form", "User Interface"))
        self.pushButton.setText(_translate("Form", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())