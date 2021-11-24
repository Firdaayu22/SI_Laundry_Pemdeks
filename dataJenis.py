from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from inputJenis import Ui_inputAdd
from updateJenis import Ui_inputUp

db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("laundry.db")
db.open()
query = QtSql.QSqlQuery()
query.exec_('CREATE TABLE IF NOT EXISTS dataJenis(No INTEGER primary key AUTOINCREMENT,'
          'Jenis varchar(20), Harga varchar(20))')
tabel = QtSql.QSqlTableModel()

class Ui_jenis(QtWidgets.QMainWindow):
    def setupUi(self, jenis):
        jenis.setObjectName("jenis")
        jenis.resize(592, 525)
        jenis.setStyleSheet("background-color: pink;")
        self.centralwidget = QtWidgets.QWidget(jenis)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 4, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 4, 1, 2, 1)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setStyleSheet("QPushButton {\n"
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
        self.back.setObjectName("back")
        self.gridLayout_5.addWidget(self.back, 4, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 5, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 3, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 4, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(229, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 1, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 2, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 3, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nama = QtWidgets.QLabel(self.groupBox_2)
        self.nama.setObjectName("nama")
        self.horizontalLayout_2.addWidget(self.nama)
        self.nama1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.nama1.setStyleSheet("background-color: white;")
        self.nama1.setObjectName("nama1")
        self.horizontalLayout_2.addWidget(self.nama1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
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
        self.horizontalLayout_4.addWidget(self.search)
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
        self.horizontalLayout_4.addWidget(self.delete)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setBaseSize(QtCore.QSize(0, 0))
        self.tableView.setStyleSheet("background-color: white;")
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.update = QtWidgets.QPushButton(self.groupBox_2)
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
        self.oke = QtWidgets.QPushButton(self.groupBox_2)
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
        self.horizontalLayout.addWidget(self.fresh)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 3, 1, 1, 4)
        jenis.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(jenis)
        self.statusbar.setObjectName("statusbar")
        jenis.setStatusBar(self.statusbar)

        self.search.clicked.connect(self.cari)
        self.delete.clicked.connect(self.hapus)
        self.update.clicked.connect(self.inputUp)
        self.oke.clicked.connect(self.inputAdd)
        self.back.clicked.connect(self.tutup)
        self.back.clicked.connect(jenis.close)
        self.fresh.clicked.connect(self.data)

        self.retranslateUi(jenis)
        QtCore.QMetaObject.connectSlotsByName(jenis)

    def retranslateUi(self, jenis):
        _translate = QtCore.QCoreApplication.translate
        jenis.setWindowTitle(_translate("jenis", "Laundry"))
        self.back.setText(_translate("jenis", "BACK"))
        self.label.setText(_translate("jenis", ". . . L A U N D R Y . . ."))
        self.label_2.setText(_translate("jenis", "     ...Data Jenis Laundry..."))
        self.groupBox_2.setTitle(_translate("jenis", "Jenis Laundry"))
        self.nama.setText(_translate("jenis", "Jenis"))
        self.search.setText(_translate("jenis", "Search"))
        self.delete.setText(_translate("jenis", "Delete"))
        self.update.setText(_translate("jenis", "Update"))
        self.oke.setText(_translate("jenis", "Tambah"))
        self.fresh.setText(_translate("jenis", "Refresh"))

    def data(self):
        db.open()
        query = QtSql.QSqlQuery()
        query.exec_("select * from dataJenis")
        tabel.setQuery(query)
        self.tableView.setModel(tabel)
        
    def cari(self):
        jenis = self.nama1.text()
        query = QtSql.QSqlQuery()
        if jenis == "":
            QtWidgets.QMessageBox.about(self,"Alert!!","Silahkan Input Dahulu!")
        else:
            query.exec_("select * from dataJenis where Jenis like '%"+jenis+"%'")
            tabel.setQuery(query)
            self.tableView.setModel(tabel)
            self.nama1.setText("")

    def hapus(self):
        jenis = self.nama1.text()
        query = QtSql.QSqlQuery()
        query.exec_("DELETE from dataJenis where Jenis like '%"+jenis+"%'")
        self.data()
        self.nama1.setText("")
        
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
        self.ui = Ui_jenis()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jenis = QtWidgets.QMainWindow()
    ui = Ui_jenis()
    ui.setupUi(jenis)
    jenis.show()
    sys.exit(app.exec_())
