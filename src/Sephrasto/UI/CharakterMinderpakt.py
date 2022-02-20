# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterMinderpakt.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(922, 558)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget.setTabKeyNavigation(True)
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(80)
        self.treeWidget.header().setStretchLastSection(False)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 465, 497))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTyp = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelTyp.setMinimumSize(QtCore.QSize(0, 18))
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelTyp.setFont(font)
        self.labelTyp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelTyp.setObjectName("labelTyp")
        self.gridLayout.addWidget(self.labelTyp, 1, 0, 1, 1)
        self.labelNachkauf = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelNachkauf.setMinimumSize(QtCore.QSize(0, 18))
        self.labelNachkauf.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNachkauf.setObjectName("labelNachkauf")
        self.gridLayout.addWidget(self.labelNachkauf, 3, 1, 1, 1)
        self.labelVorteil = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelVorteil.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelVorteil.setFont(font)
        self.labelVorteil.setObjectName("labelVorteil")
        self.gridLayout.addWidget(self.labelVorteil, 0, 0, 1, 2)
        self.plainText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plainText.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plainText.setLineWidth(1)
        self.plainText.setReadOnly(True)
        self.plainText.setBackgroundVisible(False)
        self.plainText.setObjectName("plainText")
        self.gridLayout.addWidget(self.plainText, 4, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.labelKosten = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelKosten.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelKosten.setObjectName("labelKosten")
        self.gridLayout.addWidget(self.labelKosten, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.treeWidget, self.scrollArea)
        Dialog.setTabOrder(self.scrollArea, self.plainText)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sephrasto - Minderpakt-Vorteil wählen"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "Vorteil"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "Kosten"))
        self.labelTyp.setText(_translate("Dialog", "Profan"))
        self.labelNachkauf.setText(_translate("Dialog", "Häufig"))
        self.labelVorteil.setText(_translate("Dialog", "Vorteil"))
        self.label_2.setText(_translate("Dialog", "Kosten:"))
        self.labelKosten.setText(_translate("Dialog", "20 EP"))
        self.label.setText(_translate("Dialog", "Nachkauf:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
