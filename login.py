from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from menu import Ui_pilih
import sqlite3 as sq
conn = sq.connect('laundry.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS login(User varchar(20), Password varchar(20))')

class Ui_login(QtWidgets.QMainWindow):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(592, 525)
        login.setStyleSheet("background-color: pink;")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.user1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user1.setFont(font)
        self.user1.setObjectName("user1")
        self.gridLayout.addWidget(self.user1, 0, 0, 1, 1)
        self.user = QtWidgets.QLineEdit(self.groupBox)
        self.user.setStyleSheet("background-color: white;")
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 0, 1, 1, 1)
        self.password1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password1.setFont(font)
        self.password1.setObjectName("password1")
        self.gridLayout.addWidget(self.password1, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setStyleSheet("background-color: white;")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.log = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.log.setFont(font)
        self.log.setStyleSheet("QPushButton {\n"
"background-color: rgb(32, 117, 255);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding: 10px;\n"
"color: white;\n"
"font: 11pt;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(42, 163, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(43, 170, 255);\n"
"}")
        self.log.setObjectName("log")
        self.horizontalLayout.addWidget(self.log)
        self.daftar = QtWidgets.QPushButton(self.groupBox)
        self.daftar.setStyleSheet("QPushButton {\n"
"background-color: rgb(32, 117, 255);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding: 10px;\n"
"color: white;\n"
"font: 11pt;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(42, 163, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(43, 170, 255);\n"
"}")
        self.daftar.setObjectName("daftar")
        self.horizontalLayout.addWidget(self.daftar)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log.clicked.connect(self.login)
        self.daftar.clicked.connect(self.register)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.groupBox.setTitle(_translate("login", "LOGIN"))
        self.user1.setText(_translate("login", "Username"))
        self.password1.setText(_translate("login", "Password"))
        self.log.setText(_translate("login", "LOGIN"))
        self.daftar.setText(_translate("login", "DAFTAR"))

    def login(self):
        user = self.user.text()
        password = self.password.text()
        conn = sq.connect('laundry.db')
        c = conn.cursor()
        c.execute("select User, Password from login where User = '%s' AND Password = '%s';" % (user, password))
        if (len(c.fetchall())>0):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_pilih()
            self.ui.setupUi(self.window)
            self.window.show()
            self.user.setText("")
            self.password.setText("")
        else:
            QtWidgets.QMessageBox.about(self,"Alert!!","Username dan Password Salah!")
            self.user.setText("")
            self.password.setText("")

    def register(self):
        user = self.user.text()
        password = self.password.text()
        conn = sq.connect('laundry.db')
        c = conn.cursor()
        if user == "" or password == "":
            QtWidgets.QMessageBox.about(self,"Alert!!","Silahkan Input Dahulu!")
        else:
            c.execute("INSERT INTO login(User, Password) VALUES ('%s', '%s');" % (user, password))
            conn.commit()
            QtWidgets.QMessageBox.about(self,"Congrat!!","Pendaftaran Berhasil!")
            self.user.setText("")
            self.password.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
