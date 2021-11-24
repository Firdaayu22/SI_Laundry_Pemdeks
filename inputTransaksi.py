from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("laundry.db")
db.open()
query = QtSql.QSqlQuery()
query.exec_('CREATE TABLE IF NOT EXISTS trans(No INTEGER primary key AUTOINCREMENT,ID_User varchar(20), Nama varchar(20), Alamat varchar(20), No_Hp varchar(20),'
            'Jenis varchar(20), Berat varchar(20), Harga varchar(20), Total varchar(20), Tgl_Dtg date, Tgl_Amb date, Status varchar(20))')
tabel = QtSql.QSqlTableModel()

class Ui_inputAdd(QtWidgets.QMainWindow):
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
        self.tgl1 = QtWidgets.QDateEdit(self.groupBox)
        self.tgl1.setStyleSheet("background-color: white;")
        self.tgl1.setObjectName("tgl1")
        self.tgl1.setDate(QtCore.QDate.currentDate())
        self.gridLayout_2.addWidget(self.tgl1, 10, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.oke = QtWidgets.QPushButton(self.groupBox)
        self.oke.setStyleSheet("QPushButton {\n"
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
        self.oke.setObjectName("oke")
        self.horizontalLayout.addWidget(self.oke)
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
        self.gridLayout_2.addLayout(self.horizontalLayout, 13, 0, 1, 2)
        self.tgl = QtWidgets.QLabel(self.groupBox)
        self.tgl.setObjectName("tgl")
        self.gridLayout_2.addWidget(self.tgl, 10, 0, 1, 1)
        self.status = QtWidgets.QLabel(self.groupBox)
        self.status.setObjectName("status")
        self.gridLayout_2.addWidget(self.status, 11, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 14, 0, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setStyleSheet("background-color: white;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 4, 1, 1, 1)
        self.nama = QtWidgets.QLabel(self.groupBox)
        self.nama.setObjectName("nama")
        self.gridLayout_2.addWidget(self.nama, 1, 0, 1, 1)
        self.alamat = QtWidgets.QLabel(self.groupBox)
        self.alamat.setObjectName("alamat")
        self.gridLayout_2.addWidget(self.alamat, 2, 0, 1, 1)
        self.total1 = QtWidgets.QLineEdit(self.groupBox)
        self.total1.setStyleSheet("background-color: white;")
        self.total1.setObjectName("total1")
        self.gridLayout_2.addWidget(self.total1, 8, 1, 1, 1)
        self.tglDtg = QtWidgets.QLabel(self.groupBox)
        self.tglDtg.setObjectName("tglDtg")
        self.gridLayout_2.addWidget(self.tglDtg, 9, 0, 1, 1)
        self.id1 = QtWidgets.QLineEdit(self.groupBox)
        self.id1.setStyleSheet("background-color: white;")
        self.id1.setObjectName("id1")
        self.gridLayout_2.addWidget(self.id1, 0, 1, 1, 1)
        self.nama1 = QtWidgets.QLineEdit(self.groupBox)
        self.nama1.setStyleSheet("background-color: white;")
        self.nama1.setObjectName("nama1")
        self.gridLayout_2.addWidget(self.nama1, 1, 1, 1, 1)
        self.alamat1 = QtWidgets.QLineEdit(self.groupBox)
        self.alamat1.setStyleSheet("background-color: white;")
        self.alamat1.setObjectName("alamat1")
        self.gridLayout_2.addWidget(self.alamat1, 2, 1, 1, 1)
        self.berat = QtWidgets.QLabel(self.groupBox)
        self.berat.setObjectName("berat")
        self.gridLayout_2.addWidget(self.berat, 6, 0, 1, 1)
        self.harga = QtWidgets.QLabel(self.groupBox)
        self.harga.setObjectName("harga")
        self.gridLayout_2.addWidget(self.harga, 7, 0, 1, 1)
        self.berat1 = QtWidgets.QLineEdit(self.groupBox)
        self.berat1.setStyleSheet("background-color: white;")
        self.berat1.setObjectName("berat1")
        self.gridLayout_2.addWidget(self.berat1, 6, 1, 1, 1)
        self.hp1 = QtWidgets.QLineEdit(self.groupBox)
        self.hp1.setStyleSheet("background-color: white;")
        self.hp1.setObjectName("hp1")
        self.gridLayout_2.addWidget(self.hp1, 3, 1, 1, 1)
        self.hp = QtWidgets.QLabel(self.groupBox)
        self.hp.setObjectName("hp")
        self.gridLayout_2.addWidget(self.hp, 3, 0, 1, 1)
        self.id = QtWidgets.QLabel(self.groupBox)
        self.id.setObjectName("id")
        self.gridLayout_2.addWidget(self.id, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setStyleSheet("background-color: white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 11, 1, 1, 1)
        self.tglDtg1 = QtWidgets.QDateEdit(self.groupBox)
        self.tglDtg1.setStyleSheet("background-color: white;")
        self.tglDtg1.setObjectName("tglDtg1")
        self.tglDtg1.setDate(QtCore.QDate.currentDate())
        self.gridLayout_2.addWidget(self.tglDtg1, 9, 1, 1, 1)
        self.total = QtWidgets.QLabel(self.groupBox)
        self.total.setObjectName("total")
        self.gridLayout_2.addWidget(self.total, 8, 0, 1, 1)
        self.harga1 = QtWidgets.QLineEdit(self.groupBox)
        self.harga1.setStyleSheet("background-color: white;")
        self.harga1.setObjectName("harga1")
        self.gridLayout_2.addWidget(self.harga1, 7, 1, 1, 1)
        self.jenis = QtWidgets.QLabel(self.groupBox)
        self.jenis.setObjectName("jenis")
        self.gridLayout_2.addWidget(self.jenis, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 4)
        transaksi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(transaksi)
        self.statusbar.setObjectName("statusbar")
        transaksi.setStatusBar(self.statusbar)

        self.oke.clicked.connect(self.tambah)
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
        self.groupBox.setTitle(_translate("transaksi", "Input"))
        self.oke.setText(_translate("transaksi", "Tambah"))
        self.cancel.setText(_translate("transaksi", "Cancel"))
        self.tgl.setText(_translate("transaksi", "Tgl Ambil"))
        self.status.setText(_translate("transaksi", "Status"))
        self.comboBox_2.setItemText(0, _translate("transaksi", "--Pilih Jenis--"))
        self.comboBox_2.setItemText(1, _translate("transaksi", "Cuci Basah"))
        self.comboBox_2.setItemText(2, _translate("transaksi", "Cuci Kering"))
        self.comboBox_2.setItemText(3, _translate("transaksi", "Cuci Komplit"))
        self.nama.setText(_translate("transaksi", "Nama"))
        self.alamat.setText(_translate("transaksi", "Alamat"))
        self.tglDtg.setText(_translate("transaksi", "Tgl Datang"))
        self.berat.setText(_translate("transaksi", "Berat"))
        self.harga.setText(_translate("transaksi", "Harga"))
        self.hp.setText(_translate("transaksi", "NO. Hp"))
        self.id.setText(_translate("transaksi", "ID User"))
        self.comboBox.setItemText(0, _translate("transaksi", "--Pilih Status--"))
        self.comboBox.setItemText(1, _translate("transaksi", "Belum Diambil"))
        self.comboBox.setItemText(2, _translate("transaksi", "Sudah Diambil"))
        self.total.setText(_translate("transaksi", "Total Bayar"))
        self.jenis.setText(_translate("transaksi", "Jenis"))

    def refresh(self):
        query = QtSql.QSqlQuery()
        query.exec_("select * from trans")
        tabel.setQuery(query)

    def tambah(self):
        user = self.id1.text()
        nama = self.nama1.text()
        alamat = self.alamat1.text()
        hp = self.hp1.text()
        jenis = self.comboBox_2.currentText()
        berat = self.berat1.text()
        harga = self.harga1.text()
        total = self.total1.text()
        dtg = self.tglDtg1.date().toPyDate()
        amb = self.tgl1.date().toPyDate()
        status = self.comboBox.currentText()
        query = QtSql.QSqlQuery()
        if user=="" or nama=="" or alamat=="" or hp=="" or berat=="" or harga=="" or total=="" or amb==QtCore.QDate.currentDate():
            QtWidgets.QMessageBox.about(self,"Alert!!","Silahkan Input Dahulu!")
        else:
            query.exec_("INSERT INTO trans(No, ID_User, Nama, Alamat, No_Hp, Jenis, Berat, Harga, Total, Tgl_Dtg, Tgl_Amb, Status)"
                        " VALUES (NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (user, nama, alamat, hp, jenis, berat, harga, total, dtg, amb, status))
            self.refresh()
            self.clear()

    def clear(self):
        user = self.id1.setText("")
        nama = self.nama1.setText("")
        alamat = self.alamat1.setText("")
        hp = self.hp1.setText("")
        jenis = self.comboBox_2.setCurrentIndex(0)
        berat = self.berat1.setText("")
        harga = self.harga1.setText("")
        total = self.total1.setText("")
        dtg = self.tglDtg1.setDate(QtCore.QDate.currentDate())
        amb = self.tgl1.setDate(QtCore.QDate.currentDate())
        status = self.comboBox.setCurrentIndex(0)

    def tutup(self):
        from dataTransaksi import Ui_transaksi
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_inputAdd()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    transaksi = QtWidgets.QMainWindow()
    ui = Ui_inputAdd()
    ui.setupUi(transaksi)
    transaksi.show()
    sys.exit(app.exec_())
