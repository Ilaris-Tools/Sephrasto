# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterMain.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_formMain(object):
    def setupUi(self, formMain):
        formMain.setObjectName("formMain")
        formMain.resize(713, 491)
        self.gridLayout = QtWidgets.QGridLayout(formMain)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabs = QtWidgets.QTabWidget(formMain)
        self.tabs.setObjectName("tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabs.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabs)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(formMain)
        self.label.setMinimumSize(QtCore.QSize(115, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.editEP = QtWidgets.QLineEdit(formMain)
        self.editEP.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editEP.sizePolicy().hasHeightForWidth())
        self.editEP.setSizePolicy(sizePolicy)
        self.editEP.setMinimumSize(QtCore.QSize(50, 0))
        self.editEP.setMaximumSize(QtCore.QSize(50, 16777215))
        self.editEP.setText("")
        self.editEP.setObjectName("editEP")
        self.horizontalLayout_2.addWidget(self.editEP)
        self.label_2 = QtWidgets.QLabel(formMain)
        self.label_2.setMinimumSize(QtCore.QSize(115, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.editRemaining = QtWidgets.QLineEdit(formMain)
        self.editRemaining.setMinimumSize(QtCore.QSize(50, 0))
        self.editRemaining.setMaximumSize(QtCore.QSize(50, 16777215))
        self.editRemaining.setObjectName("editRemaining")
        self.horizontalLayout_2.addWidget(self.editRemaining)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonSave = QtWidgets.QPushButton(formMain)
        self.buttonSave.setMinimumSize(QtCore.QSize(75, 0))
        self.buttonSave.setObjectName("buttonSave")
        self.horizontalLayout_2.addWidget(self.buttonSave)
        self.buttonSavePDF = QtWidgets.QPushButton(formMain)
        self.buttonSavePDF.setMinimumSize(QtCore.QSize(100, 0))
        self.buttonSavePDF.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.buttonSavePDF.setObjectName("buttonSavePDF")
        self.horizontalLayout_2.addWidget(self.buttonSavePDF)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(formMain)
        QtCore.QMetaObject.connectSlotsByName(formMain)

    def retranslateUi(self, formMain):
        _translate = QtCore.QCoreApplication.translate
        formMain.setWindowTitle(_translate("formMain", "Sephrasto - Charakter erstellen"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("formMain", "Tab 1"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("formMain", "Tab 2"))
        self.label.setText(_translate("formMain", "Erfahrungspunke:"))
        self.label_2.setText(_translate("formMain", "Verfügbar:"))
        self.buttonSave.setText(_translate("formMain", "Speichern"))
        self.buttonSavePDF.setText(_translate("formMain", "PDF erstellen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formMain = QtWidgets.QWidget()
    ui = Ui_formMain()
    ui.setupUi(formMain)
    formMain.show()
    sys.exit(app.exec_())

