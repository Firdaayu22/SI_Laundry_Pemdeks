from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("laundry.db")
db.open()
query = QtSql.QSqlQuery()
query.exec_('CREATE TABLE IF NOT EXISTS dataJenis(No INTEGER primary key AUTOINCREMENT,'
          'Jenis varchar(20), Harga varchar(20))')
tabel = QtSql.QSqlTableModel()

class Ui_inputUp(QtWidgets.QMainWindow):
    def setupUi(self, jenis):
        jenis.setObjectName("jenis")
        jenis.resize(581, 525)
        jenis.setStyleSheet("background-color: pink;")
        self.centralwidget = QtWidgets.QWidget(jenis)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 5, 6, 1, 1)
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
        self.gridLayout_5.addWidget(self.back, 5, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 3, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 5, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(229, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 1, 4, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.id = QtWidgets.QLabel(self.groupBox)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 0, 0, 1, 1)
        self.id1 = QtWidgets.QLineEdit(self.groupBox)
        self.id1.setStyleSheet("background-color: white;")
        self.id1.setObjectName("id1")
        self.gridLayout.addWidget(self.id1, 0, 1, 1, 1)
        self.harga = QtWidgets.QLabel(self.groupBox)
        self.harga.setObjectName("harga")
        self.gridLayout.addWidget(self.harga, 1, 0, 1, 1)
        self.harga1 = QtWidgets.QLineEdit(self.groupBox)
        self.harga1.setStyleSheet("background-color: white;")
        self.harga1.setObjectName("harga1")
        self.gridLayout.addWidget(self.harga1, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
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
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 3, 1, 2, 4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 2, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 6, 4, 1, 1)
        jenis.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(jenis)
        self.statusbar.setObjectName("statusbar")
        jenis.setStatusBar(self.statusbar)

        self.update.clicked.connect(self.baru)
        self.cancel.clicked.connect(self.clear)
        self.back.clicked.connect(self.tutup)
        self.back.clicked.connect(jenis.close)

        self.retranslateUi(jenis)
        QtCore.QMetaObject.connectSlotsByName(jenis)

    def retranslateUi(self, jenis):
        _translate = QtCore.QCoreApplication.translate
        jenis.setWindowTitle(_translate("jenis", "Laundry"))
        self.back.setText(_translate("jenis", "BACK"))
        self.label.setText(_translate("jenis", ". . . L A U N D R Y . . ."))
        self.groupBox.setTitle(_translate("jenis", "Update"))
        self.id.setText(_translate("jenis", "Jenis"))
        self.harga.setText(_translate("jenis", "Harga"))
        self.update.setText(_translate("jenis", "Update"))
        self.cancel.setText(_translate("jenis", "Cancel"))
        self.label_2.setText(_translate("jenis", "     ...Data Jenis Laundry..."))

    def data(self):
        db.open()
        query = QtSql.QSqlQuery()
        query.exec_("select * from dataJenis")
        tabel.setQuery(query)
        
    def baru(self):
        jenis = self.id1.text()
        harga = self.harga1.text()
        query = QtSql.QSqlQuery()
        if jenis == "" or harga == "":
            QtWidgets.QMessageBox.about(self,"Alert!!","Silahkan Input Dahulu!")
        else:
            query.exec_("UPDATE dataJenis SET Harga = '%s' WHERE Jenis = '%s';" % (harga, jenis))
            self.data()
            self.clear()

    def clear(self):
        self.id1.setText("")
        self.harga1.setText("")

    def tutup(self):
        from dataJenis import Ui_jenis
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_inputUp()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jenis = QtWidgets.QMainWindow()
    ui = Ui_inputUp()
    ui.setupUi(jenis)
    jenis.show()
    sys.exit(app.exec_())
