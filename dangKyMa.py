# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dangKy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1682, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 1611, 741))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(120, 27, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 27, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_imgUser = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_imgUser.setGeometry(QtCore.QRect(390, 160, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_imgUser.setFont(font)
        self.btn_imgUser.setObjectName("btn_imgUser")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(880, 20, 471, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.hTNLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hTNLabel.setFont(font)
        self.hTNLabel.setObjectName("hTNLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hTNLabel)
        self.input_hoTen = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_hoTen.setFont(font)
        self.input_hoTen.setObjectName("input_hoTen")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_hoTen)
        self.mSLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mSLabel.setFont(font)
        self.mSLabel.setObjectName("mSLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mSLabel)
        self.input_maSo = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_maSo.setFont(font)
        self.input_maSo.setObjectName("input_maSo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_maSo)
        self.sINThoILabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sINThoILabel.setFont(font)
        self.sINThoILabel.setObjectName("sINThoILabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sINThoILabel)
        self.input_phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_phone.setFont(font)
        self.input_phone.setObjectName("input_phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_phone)
        self.emailLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
        self.input_email = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_email.setFont(font)
        self.input_email.setObjectName("input_email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_email)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.input_gioiTinh = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_gioiTinh.setFont(font)
        self.input_gioiTinh.setObjectName("input_gioiTinh")
        self.input_gioiTinh.addItem("")
        self.input_gioiTinh.addItem("")
        self.input_gioiTinh.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.input_gioiTinh)
        self.label_maMon = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_maMon.setFont(font)
        self.label_maMon.setObjectName("label_maMon")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_maMon)
        self.input_maMon = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_maMon.setFont(font)
        self.input_maMon.setObjectName("input_maMon")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.input_maMon)
        self.label_nhom = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nhom.setFont(font)
        self.label_nhom.setObjectName("label_nhom")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_nhom)
        self.input_nhom = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_nhom.setFont(font)
        self.input_nhom.setObjectName("input_nhom")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.input_nhom)
        self.label_user = QtWidgets.QLabel(self.groupBox_2)
        self.label_user.setGeometry(QtCore.QRect(100, 40, 241, 271))
        self.label_user.setFrameShape(QtWidgets.QFrame.Box)
        self.label_user.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_user.setLineWidth(5)
        self.label_user.setText("")
        self.label_user.setPixmap(QtGui.QPixmap("img/pic_user.png"))
        self.label_user.setScaledContents(True)
        self.label_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user.setObjectName("label_user")
        self.btn_luuThongTin = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_luuThongTin.setGeometry(QtCore.QRect(1190, 330, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_luuThongTin.setFont(font)
        self.btn_luuThongTin.setObjectName("btn_luuThongTin")
        self.btn_clear_input = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_clear_input.setGeometry(QtCore.QRect(1190, 400, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_clear_input.setFont(font)
        self.btn_clear_input.setObjectName("btn_clear_input")
        self.label_barCode = QtWidgets.QLabel(self.groupBox_2)
        self.label_barCode.setGeometry(QtCore.QRect(100, 350, 331, 221))
        self.label_barCode.setFrameShape(QtWidgets.QFrame.Box)
        self.label_barCode.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_barCode.setLineWidth(3)
        self.label_barCode.setObjectName("label_barCode")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1682, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Điều hướng"))
        self.pushButton.setText(_translate("MainWindow", "Đăng Ký mã vạch"))
        self.pushButton_2.setText(_translate("MainWindow", "Quản Lý Điểm Danh"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Đăng ký thông tin"))
        self.btn_imgUser.setText(_translate("MainWindow", "Đăng ảnh"))
        self.hTNLabel.setText(_translate("MainWindow", "Họ tên"))
        self.mSLabel.setText(_translate("MainWindow", "Mã số "))
        self.sINThoILabel.setText(_translate("MainWindow", "Số điện thoại"))
        self.input_phone.setInputMask(_translate("MainWindow", "0000-000-000"))
        self.emailLabel.setText(_translate("MainWindow", "Email"))
        self.label.setText(_translate("MainWindow", "Giới tính"))
        self.input_gioiTinh.setItemText(0, _translate("MainWindow", "Nam"))
        self.input_gioiTinh.setItemText(1, _translate("MainWindow", "Nữ"))
        self.input_gioiTinh.setItemText(2, _translate("MainWindow", "Khác"))
        self.label_maMon.setText(_translate("MainWindow", "Mã môn"))
        self.label_nhom.setText(_translate("MainWindow", "Nhóm"))
        self.btn_luuThongTin.setText(_translate("MainWindow", "Lưu thông tin"))
        self.btn_clear_input.setText(_translate("MainWindow", "Làm mới"))
        self.label_barCode.setText(_translate("MainWindow", "Mã vạch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())