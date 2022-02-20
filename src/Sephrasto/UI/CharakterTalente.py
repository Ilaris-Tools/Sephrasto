# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterTalente.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(928, 522)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listTalente = QtWidgets.QListView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listTalente.sizePolicy().hasHeightForWidth())
        self.listTalente.setSizePolicy(sizePolicy)
        self.listTalente.setObjectName("listTalente")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet("padding: 1px")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 467, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinKosten = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinKosten.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinKosten.setReadOnly(True)
        self.spinKosten.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinKosten.setMinimum(0)
        self.spinKosten.setMaximum(8000)
        self.spinKosten.setSingleStep(20)
        self.spinKosten.setObjectName("spinKosten")
        self.gridLayout_2.addWidget(self.spinKosten, 1, 1, 1, 1)
        self.labelKommentar = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelKommentar.setObjectName("labelKommentar")
        self.gridLayout_2.addWidget(self.labelKommentar, 3, 0, 1, 1)
        self.textKommentar = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.textKommentar.setObjectName("textKommentar")
        self.gridLayout_2.addWidget(self.textKommentar, 3, 1, 1, 1)
        self.plainText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plainText.setReadOnly(True)
        self.plainText.setObjectName("plainText")
        self.gridLayout_2.addWidget(self.plainText, 4, 0, 1, 2)
        self.labelName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelName.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.gridLayout_2.addWidget(self.labelName, 0, 0, 1, 2)
        self.labelInfo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelInfo.setMinimumSize(QtCore.QSize(0, 18))
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelInfo.setFont(font)
        self.labelInfo.setObjectName("labelInfo")
        self.gridLayout_2.addWidget(self.labelInfo, 2, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.listTalente, self.spinKosten)
        Dialog.setTabOrder(self.spinKosten, self.textKommentar)
        Dialog.setTabOrder(self.textKommentar, self.plainText)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sephrasto - Talente wählen..."))
        self.label_2.setText(_translate("Dialog", "Kosten:"))
        self.spinKosten.setSuffix(_translate("Dialog", " EP"))
        self.labelKommentar.setText(_translate("Dialog", "Kommentar:"))
        self.labelName.setText(_translate("Dialog", "Talentname"))
        self.labelInfo.setText(_translate("Dialog", "Spezialtalent"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
