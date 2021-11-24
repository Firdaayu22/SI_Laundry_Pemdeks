from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("laundry.db")
db.open()
query = QtSql.QSqlQuery()
query.exec_('CREATE TABLE IF NOT EXISTS trans(No INTEGER primary key AUTOINCREMENT,ID_User varchar(20), Nama varchar(20), Alamat varchar(20), No_Hp varchar(20),'
            'Jenis varchar(20), Berat varchar(20), Harga varchar(20), Total varchar(20), Tgl_Dtg date, Tgl_Amb date, Status varchar(20))')
tabel = QtSql.QSqlTableModel()

class Ui_pelanggan(QtWidgets.QMainWindow):
    def setupUi(self, pelanggan):
        pelanggan.setObjectName("pelanggan")
        pelanggan.resize(592, 525)
        pelanggan.setStyleSheet("background-color: pink;")
        self.centralwidget = QtWidgets.QWidget(pelanggan)
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
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 5, 4, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.data = QtWidgets.QLabel(self.groupBox_2)
        self.data.setObjectName("data")
        self.horizontalLayout.addWidget(self.data)
        self.data1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.data1.setStyleSheet("background-color: white;")
        self.data1.setObjectName("data1")
        self.horizontalLayout.addWidget(self.data1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search = QtWidgets.QPushButton(self.groupBox_2)
        self.search.setStyleSheet("QPushButton {\n"
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
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.delete = QtWidgets.QPushButton(self.groupBox_2)
        self.delete.setStyleSheet("QPushButton {\n"
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
        self.delete.setObjectName("del")
        self.horizontalLayout_2.addWidget(self.delete)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setStyleSheet("background-color: white;")
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 1, 0, 1, 1)
        self.fresh = QtWidgets.QPushButton(self.groupBox_2)
        self.fresh.setStyleSheet("QPushButton {\n"
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
        self.fresh.setObjectName("fresh")
        self.gridLayout_3.addWidget(self.fresh, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 1, 1, 4)
        pelanggan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(pelanggan)
        self.statusbar.setObjectName("statusbar")
        pelanggan.setStatusBar(self.statusbar)

        self.search.clicked.connect(self.cari)
        self.delete.clicked.connect(self.hapus)
        self.logout.clicked.connect(self.tutup)
        self.logout.clicked.connect(pelanggan.close)
        self.fresh.clicked.connect(self.refresh)

        self.retranslateUi(pelanggan)
        QtCore.QMetaObject.connectSlotsByName(pelanggan)

    def retranslateUi(self, pelanggan):
        _translate = QtCore.QCoreApplication.translate
        pelanggan.setWindowTitle(_translate("pelanggan", "Laundry"))
        self.label.setText(_translate("pelanggan", ". . . L A U N D R Y . . ."))
        self.logout.setText(_translate("pelanggan", "BACK"))
        self.label_2.setText(_translate("pelanggan", "        ...Data Pelanggan..."))
        self.groupBox_2.setTitle(_translate("pelanggan", "Data"))
        self.data.setText(_translate("pelanggan", "Nama"))
        self.search.setText(_translate("pelanggan", "Search"))
        self.delete.setText(_translate("pelanggan", "Delete"))
        self.fresh.setText(_translate("pelanggan", "Refresh"))

    def refresh(self):
        query = QtSql.QSqlQuery()
        query.exec_("select ID_User, Nama, Alamat, No_Hp, Jenis, Berat, Total from trans")
        tabel.setQuery(query)
        self.tableView.setModel(tabel)

    def cari(self):
        Id = self.data1.text()
        query = QtSql.QSqlQuery()
        if Id == "":
            QtWidgets.QMessageBox.about(self,"Alert!!","Silahkan Input Dahulu!")
        else:
            query.exec_("select ID_User, Nama, Alamat, No_Hp, Jenis, Berat, Total from trans where ID_User like '%"+Id+"%'")
            tabel.setQuery(query)
            self.tableView.setModel(tabel)
            self.data1.setText("")
            
    def hapus(self):
        Id = self.data1.text()
        query = QtSql.QSqlQuery()
        query.exec_("DELETE from trans where ID_User like '%"+Id+"%'")
        self.refresh()
        self.data1.setText("")

    def tutup(self):
        from menu import Ui_pilih
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_pelanggan()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pelanggan = QtWidgets.QMainWindow()
    ui = Ui_pelanggan()
    ui.setupUi(pelanggan)
    pelanggan.show()
    sys.exit(app.exec_())
