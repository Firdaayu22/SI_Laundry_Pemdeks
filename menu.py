from PyQt5 import QtCore, QtGui, QtWidgets
from dataJenis import Ui_jenis
from dataPelanggan import Ui_pelanggan
from dataTransaksi import Ui_transaksi

class Ui_pilih(QtWidgets.QMainWindow):
    def setupUi(self, pilih):
        pilih.setObjectName("pilih")
        pilih.resize(592, 525)
        pilih.setStyleSheet("background-color: pink;")
        self.centralwidget = QtWidgets.QWidget(pilih)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.jenis = QtWidgets.QPushButton(self.centralwidget)
        self.jenis.setStyleSheet("QPushButton {\n"
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
        self.jenis.setObjectName("jenis")
        self.verticalLayout.addWidget(self.jenis)
        self.data = QtWidgets.QPushButton(self.centralwidget)
        self.data.setStyleSheet("QPushButton {\n"
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
        self.data.setObjectName("data")
        self.verticalLayout.addWidget(self.data)
        self.transaksi = QtWidgets.QPushButton(self.centralwidget)
        self.transaksi.setStyleSheet("QPushButton {\n"
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
        self.transaksi.setObjectName("transaksi")
        self.verticalLayout.addWidget(self.transaksi)
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
        self.verticalLayout.addWidget(self.logout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 89, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        pilih.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(pilih)
        self.statusbar.setObjectName("statusbar")
        pilih.setStatusBar(self.statusbar)

        self.jenis.clicked.connect(self.dataJenis)
        self.data.clicked.connect(self.pelanggan)
        self.transaksi.clicked.connect(self.dataTransaksi)
        self.logout.clicked.connect(self.tutup)
        self.logout.clicked.connect(pilih.close)

        self.retranslateUi(pilih)
        QtCore.QMetaObject.connectSlotsByName(pilih)

    def retranslateUi(self, pilih):
        _translate = QtCore.QCoreApplication.translate
        pilih.setWindowTitle(_translate("pilih", "Laundry"))
        self.label.setText(_translate("pilih", ". . . L A U N D R Y . . ."))
        self.jenis.setText(_translate("pilih", "Jenis Laundry"))
        self.data.setText(_translate("pilih", "Data Pelanggan"))
        self.transaksi.setText(_translate("pilih", "Transaksi"))
        self.logout.setText(_translate("pilih", "LOGOUT"))

    def dataJenis(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_jenis()
        self.ui.setupUi(self.window)
        self.window.show()

    def pelanggan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_pelanggan()
        self.ui.setupUi(self.window)
        self.window.show()

    def dataTransaksi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_transaksi()
        self.ui.setupUi(self.window)
        self.window.show()

    def tutup(self):
        from login import Ui_login
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_pilih()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pilih = QtWidgets.QMainWindow()
    ui = Ui_pilih()
    ui.setupUi(pilih)
    pilih.show()
    sys.exit(app.exec_())
