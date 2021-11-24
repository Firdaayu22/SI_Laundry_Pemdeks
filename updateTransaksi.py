from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("laundry.db")
db.open()
query = QtSql.QSqlQuery()
query.exec_('CREATE TABLE IF NOT EXISTS trans(No INTEGER primary key AUTOINCREMENT,ID_User varchar(20), Nama varchar(20), Alamat varchar(20), No_Hp varchar(20),'
            'Jenis varchar(20), Berat varchar(20), Harga varchar(20), Total varchar(20), Tgl_Dtg date, Tgl_Amb date, Status varchar(20))')
tabel = QtSql.QSqlTableModel()

class Ui_inputUp(QtWidgets.QMainWindow):
    def setupUi(self, transaksi):
        transaksi.setObjectName("transaksi")
        transaksi.resize(592, 525)
        transaksi.setStyleSheet("background-color: pink;")
        self.centralwidget = QtWidgets.QWidget(transaksi)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(229, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 5, 1, 1)
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setStyleSheet("QPushButton {\n"
"background-color: rgb(32, 117, 255);\n"
"border: none;\n"
"border-radius: 12px;\n"
"padding: 5px;\n"
"color: white;\n"
"font: 10pt;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(42, 163, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(43, 170, 255);\n"
"}")
        self.logout.setObjectName("logout")
        self.gridLayout.addWidget(self.logout, 4, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 4, 1, 2, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 5, 4, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.id = QtWidgets.QLabel(self.groupBox)
        self.id.setObjectName("id")
        self.gridLayout_2.addWidget(self.id, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.update = QtWidgets.QPushButton(self.groupBox)
        self.update.setStyleSheet("QPushButton {\n"
"background-color: rgb(32, 117, 255);\n"
"border: none;\n"
"border-radius: 12px;\n"
"padding: 5px;\n"
"color: white;\n"
"font: 10pt;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(42, 163, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(43, 170, 255);\n"
"}")
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        self.cancel = QtWidgets.QPushButton(self.groupBox)
        self.cancel.setStyleSheet("QPushButton {\n"
"background-color: rgb(32, 117, 255);\n"
"border: none;\n"
"border-radius: 12px;\n"
"padding: 5px;\n"
"color: white;\n"
"font: 10pt;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(42, 163, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(43, 170, 255);\n"
"}")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.status = QtWidgets.QLabel(self.groupBox)
        self.status.setObjectName("status")
        self.gridLayout_2.addWidget(self.status, 3, 0, 1, 1)
        self.id1 = QtWidgets.QLineEdit(self.groupBox)
        self.id1.setStyleSheet("background-color: white;")
        self.id1.setObjectName("id1")
        self.gridLayout_2.addWidget(self.id1, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setStyleSheet("background-color: white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 3, 1, 1, 1)
        self.tgl = QtWidgets.QLabel(self.groupBox)
        self.tgl.setObjectName("tgl")
        self.gridLayout_2.addWidget(self.tgl, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 6, 0, 1, 2)
        self.tgl1 = QtWidgets.QDateEdit(self.groupBox)
        self.tgl1.setStyleSheet("background-color: white;")
        self.tgl1.setObjectName("tgl1")
        self.tgl1.setDate(QtCore.QDate.currentDate())
        self.gridLayout_2.addWidget(self.tgl1, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 4)
        transaksi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(transaksi)
        self.statusbar.setObjectName("statusbar")
        transaksi.setStatusBar(self.statusbar)

        self.update.clicked.connect(self.baru)
        self.cancel.clicked.connect(self.clear)
        self.logout.clicked.connect(self.tutup)
        self.logout.clicked.connect(transaksi.close)

        self.retranslateUi(transaksi)
        QtCore.QMetaObject.connectSlotsByName(transaksi)

    def retranslateUi(self, transaksi):
        _translate = QtCore.QCoreApplication.translate
        transaksi.setWindowTitle(_translate("transaksi", "Laundry"))
        self.label.setText(_translate("transaksi", ". . . L A U N D R Y . . ."))
        self.logout.setText(_translate("transaksi", "BACK"))
        self.label_2.setText(_translate("transaksi", "        ...Data Transaksi..."))
        self.groupBox.setTitle(_translate("transaksi", "Update"))
        self.id.setText(_translate("transaksi", "ID User"))
        self.update.setText(_translate("transaksi", "Update"))
        self.cancel.setText(_translate("transaksi", "Cancel"))
        self.status.setText(_translate("transaksi", "Status"))
        self.comboBox.setItemText(0, _translate("transaksi", "--Pilih Status--"))
        self.comboBox.setItemText(1, _translate("transaksi", "Belum Diambil"))
        self.comboBox.setItemText(2, _translate("transaksi", "Sudah Diambil"))
        self.tgl.setText(_translate("transaksi", "Tgl Ambil"))

    def refresh(self):
        query = QtSql.QSqlQuery()
        query.exec_("select * from trans")
        tabel.setQuery(query)

    def baru(self):
        user = self.id1.text()
        tgl = self.tgl1.date().toPyDate()
        status = self.comboBox.currentText()
        query = QtSql.QSqlQuery()
        if user == "" or tgl == QtCore.QDate.currentDate():
            QtWidgets.QMessageBox.about(self,"Alert!!","Silahkan Input Dahulu!")
        else:
            query.exec_("UPDATE trans SET Tgl_Amb = '%s', Status = '%s' WHERE ID_User = '%s';" % (tgl, status, user))
            self.refresh()
            self.clear()

    def clear(self):
        user = self.id1.setText("")
        amb = self.tgl1.setDate(QtCore.QDate.currentDate())
        status = self.comboBox.setCurrentIndex(0)

    def tutup(self):
        from dataTransaksi import Ui_transaksi
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_inputUp()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    transaksi = QtWidgets.QMainWindow()
    ui = Ui_inputUp()
    ui.setupUi(transaksi)
    transaksi.show()
    sys.exit(app.exec_())
