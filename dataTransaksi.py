from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from updateTransaksi import Ui_inputUp
from inputTransaksi import Ui_inputAdd

db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("laundry.db")
db.open()
query = QtSql.QSqlQuery()
query.exec_('CREATE TABLE IF NOT EXISTS trans(No INTEGER primary key AUTOINCREMENT,ID_User varchar(20), Nama varchar(20), Alamat varchar(20), No_Hp varchar(20),'
            'Jenis varchar(20), Berat varchar(20), Harga varchar(20), Total varchar(20), Tgl_Dtg date, Tgl_Amb date, Status varchar(20))')
tabel = QtSql.QSqlTableModel()

class Ui_transaksi(QtWidgets.QMainWindow):
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.search_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.search_2.setStyleSheet("QPushButton {\n"
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
        self.search_2.setObjectName("search_2")
        self.horizontalLayout_5.addWidget(self.search_2)
        self.del_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.del_2.setStyleSheet("QPushButton {\n"
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
        self.del_2.setObjectName("del_2")
        self.horizontalLayout_5.addWidget(self.del_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 2)
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setStyleSheet("background-color: white;")
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 2, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.update_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.update_2.setStyleSheet("QPushButton {\n"
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
        self.update_2.setObjectName("update_2")
        self.horizontalLayout_6.addWidget(self.update_2)
        self.oke_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.oke_2.setStyleSheet("QPushButton {\n"
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
        self.oke_2.setObjectName("oke_2")
        self.horizontalLayout_6.addWidget(self.oke_2)
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
        self.horizontalLayout_6.addWidget(self.fresh)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 3, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.data_2 = QtWidgets.QLabel(self.groupBox_2)
        self.data_2.setObjectName("data_2")
        self.horizontalLayout_2.addWidget(self.data_2)
        self.data1_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.data1_2.setStyleSheet("background-color: white;")
        self.data1_2.setObjectName("data1_2")
        self.horizontalLayout_2.addWidget(self.data1_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_2, 3, 1, 1, 4)
        transaksi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(transaksi)
        self.statusbar.setObjectName("statusbar")
        transaksi.setStatusBar(self.statusbar)

        self.search_2.clicked.connect(self.cari)
        self.del_2.clicked.connect(self.hapus)
        self.update_2.clicked.connect(self.inputUp)
        self.oke_2.clicked.connect(self.inputAdd)
        self.logout.clicked.connect(self.tutup)
        self.logout.clicked.connect(transaksi.close)
        self.fresh.clicked.connect(self.refresh)

        self.retranslateUi(transaksi)
        QtCore.QMetaObject.connectSlotsByName(transaksi)

    def retranslateUi(self, transaksi):
        _translate = QtCore.QCoreApplication.translate
        transaksi.setWindowTitle(_translate("transaksi", "Laundry"))
        self.label.setText(_translate("transaksi", ". . . L A U N D R Y . . ."))
        self.logout.setText(_translate("transaksi", "BACK"))
        self.label_2.setText(_translate("transaksi", "        ...Data Transaksi..."))
        self.groupBox_2.setTitle(_translate("transaksi", "Transaksi"))
        self.search_2.setText(_translate("transaksi", "Search"))
        self.del_2.setText(_translate("transaksi", "Delete"))
        self.update_2.setText(_translate("transaksi", "Update"))
        self.oke_2.setText(_translate("transaksi", "Tambah"))
        self.fresh.setText(_translate("transaksi", "Refresh"))
        self.data_2.setText(_translate("transaksi", "ID User"))

    def refresh(self):
        query = QtSql.QSqlQuery()
        query.exec_("select * from trans")
        tabel.setQuery(query)
        self.tableView.setModel(tabel)

    def cari(self):
        Id = self.data1_2.text()
        query = QtSql.QSqlQuery()
        if Id == "":
            QtWidgets.QMessageBox.about(self,"Alert!!","Silahkan Input Dahulu!")
        else:
            query.exec_("select * from trans where ID_User like '%"+Id+"%'")
            tabel.setQuery(query)
            self.tableView.setModel(tabel)
            self.data1_2.setText("")
            
    def hapus(self):
        Id = self.data1_2.text()
        query = QtSql.QSqlQuery()
        query.exec_("DELETE from trans where ID_User like '%"+Id+"%'")
        self.refresh()
        self.data1_2.setText("")

    def inputUp(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_inputUp()
        self.ui.setupUi(self.window)
        self.window.show()

    def inputAdd(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_inputAdd()
        self.ui.setupUi(self.window)
        self.window.show()

    def tutup(self):
        from menu import Ui_pilih
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_transaksi()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    transaksi = QtWidgets.QMainWindow()
    ui = Ui_transaksi()
    ui.setupUi(transaksi)
    transaksi.show()
    sys.exit(app.exec_())
