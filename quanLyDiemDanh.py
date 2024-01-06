# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quanLyDiemDanh.ui'
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 1621, 771))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_frameBarCode = QtWidgets.QLabel(self.groupBox_3)
        self.label_frameBarCode.setGeometry(QtCore.QRect(10, 30, 461, 311))
        self.label_frameBarCode.setFrameShape(QtWidgets.QFrame.Box)
        self.label_frameBarCode.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_frameBarCode.setLineWidth(5)
        self.label_frameBarCode.setScaledContents(True)
        self.label_frameBarCode.setObjectName("label_frameBarCode")
        self.btn_openCam = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_openCam.setGeometry(QtCore.QRect(510, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_openCam.setFont(font)
        self.btn_openCam.setObjectName("btn_openCam")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 380, 391, 151))
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
        self.input_hoTenGV = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.input_hoTenGV.setMaximumSize(QtCore.QSize(260, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_hoTenGV.setFont(font)
        self.input_hoTenGV.setObjectName("input_hoTenGV")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_hoTenGV)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.input_ma_mon = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.input_ma_mon.setMaximumSize(QtCore.QSize(260, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_ma_mon.setFont(font)
        self.input_ma_mon.setObjectName("input_ma_mon")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_ma_mon)
        self.emailLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
        self.input_nhom = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.input_nhom.setMaximumSize(QtCore.QSize(260, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_nhom.setFont(font)
        self.input_nhom.setObjectName("input_nhom")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_nhom)
        self.ngYLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ngYLabel.setFont(font)
        self.ngYLabel.setObjectName("ngYLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ngYLabel)
        self.input_ngay = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.input_ngay.setMinimumSize(QtCore.QSize(0, 27))
        self.input_ngay.setMaximumSize(QtCore.QSize(260, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_ngay.setFont(font)
        self.input_ngay.setObjectName("input_ngay")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_ngay)
        self.btn_closeCam = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_closeCam.setGeometry(QtCore.QRect(510, 100, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_closeCam.setFont(font)
        self.btn_closeCam.setObjectName("btn_closeCam")
        self.btn_export_file = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_export_file.setGeometry(QtCore.QRect(510, 380, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_export_file.setFont(font)
        self.btn_export_file.setObjectName("btn_export_file")
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.bang_danh_sach = QtWidgets.QTableWidget(self.groupBox_2)
        self.bang_danh_sach.setGeometry(QtCore.QRect(270, 20, 301, 621))
        self.bang_danh_sach.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bang_danh_sach.setLineWidth(3)
        self.bang_danh_sach.setObjectName("bang_danh_sach")
        self.bang_danh_sach.setColumnCount(2)
        self.bang_danh_sach.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bang_danh_sach.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bang_danh_sach.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Điều hướng"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Quản lý điểm danh"))
        self.label_frameBarCode.setText(_translate("MainWindow", "khung hiển thị"))
        self.btn_openCam.setText(_translate("MainWindow", "Mở Camera "))
        self.hTNLabel.setText(_translate("MainWindow", "Giảng viên"))
        self.label_2.setText(_translate("MainWindow", "Mã học phần"))
        self.emailLabel.setText(_translate("MainWindow", "Nhóm"))
        self.ngYLabel.setText(_translate("MainWindow", "Ngày"))
        self.btn_closeCam.setText(_translate("MainWindow", "Tắt Camera "))
        self.btn_export_file.setText(_translate("MainWindow", "Xuất file excel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Danh sách"))
        item = self.bang_danh_sach.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mssv"))
        item = self.bang_danh_sach.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Điểm danh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())