# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterAttribute.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formAttribute(object):
    def setupUi(self, formAttribute):
        formAttribute.setObjectName("formAttribute")
        formAttribute.resize(872, 460)
        self.gridLayout_2 = QtWidgets.QGridLayout(formAttribute)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtWidgets.QLabel(formAttribute)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 4, 1, 1)
        self.pwCH = QtWidgets.QSpinBox(formAttribute)
        self.pwCH.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pwCH.setWrapping(False)
        self.pwCH.setFrame(True)
        self.pwCH.setAlignment(QtCore.Qt.AlignCenter)
        self.pwCH.setReadOnly(True)
        self.pwCH.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pwCH.setProperty("showGroupSeparator", False)
        self.pwCH.setObjectName("pwCH")
        self.gridLayout.addWidget(self.pwCH, 8, 4, 1, 1)
        self.pwMU = QtWidgets.QSpinBox(formAttribute)
        self.pwMU.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pwMU.setWrapping(False)
        self.pwMU.setFrame(True)
        self.pwMU.setAlignment(QtCore.Qt.AlignCenter)
        self.pwMU.setReadOnly(True)
        self.pwMU.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pwMU.setProperty("showGroupSeparator", False)
        self.pwMU.setObjectName("pwMU")
        self.gridLayout.addWidget(self.pwMU, 3, 4, 1, 1)
        self.pwKK = QtWidgets.QSpinBox(formAttribute)
        self.pwKK.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pwKK.setWrapping(False)
        self.pwKK.setFrame(True)
        self.pwKK.setAlignment(QtCore.Qt.AlignCenter)
        self.pwKK.setReadOnly(True)
        self.pwKK.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pwKK.setProperty("showGroupSeparator", False)
        self.pwKK.setObjectName("pwKK")
        self.gridLayout.addWidget(self.pwKK, 5, 4, 1, 1)
        self.abSB = QtWidgets.QSpinBox(formAttribute)
        self.abSB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.abSB.setWrapping(False)
        self.abSB.setFrame(True)
        self.abSB.setAlignment(QtCore.Qt.AlignCenter)
        self.abSB.setReadOnly(True)
        self.abSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.abSB.setProperty("showGroupSeparator", False)
        self.abSB.setObjectName("abSB")
        self.gridLayout.addWidget(self.abSB, 5, 8, 1, 1)
        self.pwIN = QtWidgets.QSpinBox(formAttribute)
        self.pwIN.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pwIN.setWrapping(False)
        self.pwIN.setFrame(True)
        self.pwIN.setAlignment(QtCore.Qt.AlignCenter)
        self.pwIN.setReadOnly(True)
        self.pwIN.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pwIN.setProperty("showGroupSeparator", False)
        self.pwIN.setObjectName("pwIN")
        self.gridLayout.addWidget(self.pwIN, 6, 4, 1, 1)
        self.label = QtWidgets.QLabel(formAttribute)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.pwKO = QtWidgets.QSpinBox(formAttribute)
        self.pwKO.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pwKO.setWrapping(False)
        self.pwKO.setFrame(True)
        self.pwKO.setAlignment(QtCore.Qt.AlignCenter)
        self.pwKO.setReadOnly(True)
        self.pwKO.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pwKO.setProperty("showGroupSeparator", False)
        self.pwKO.setObjectName("pwKO")
        self.gridLayout.addWidget(self.pwKO, 2, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(formAttribute)
        self.label_24.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 8, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(formAttribute)
        self.label_22.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 6, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(formAttribute)
        self.label_20.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 4, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(formAttribute)
        self.label_23.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 7, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(formAttribute)
        self.label_25.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 9, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(formAttribute)
        self.label_19.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(formAttribute)
        self.label_21.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(formAttribute)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.pwGE = QtWidgets.QSpinBox(formAttribute)
        self.pwGE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pwGE.setWrapping(False)
        self.pwGE.setFrame(True)
        self.pwGE.setAlignment(QtCore.Qt.AlignCenter)
        self.pwGE.setReadOnly(True)
        self.pwGE.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pwGE.setProperty("showGroupSeparator", False)
        self.pwGE.setObjectName("pwGE")
        self.gridLayout.addWidget(self.pwGE, 4, 4, 1, 1)
        self.abWS = QtWidgets.QSpinBox(formAttribute)
        self.abWS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.abWS.setWrapping(False)
        self.abWS.setFrame(True)
        self.abWS.setAlignment(QtCore.Qt.AlignCenter)
        self.abWS.setReadOnly(True)
        self.abWS.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.abWS.setProperty("showGroupSeparator", False)
        self.abWS.setObjectName("abWS")
        self.gridLayout.addWidget(self.abWS, 2, 8, 1, 1)
        self.spinFF = QtWidgets.QSpinBox(formAttribute)
        self.spinFF.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFF.setReadOnly(False)
        self.spinFF.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinFF.setObjectName("spinFF")
        self.gridLayout.addWidget(self.spinFF, 9, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(formAttribute)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)
        self.spinKL = QtWidgets.QSpinBox(formAttribute)
        self.spinKL.setAlignment(QtCore.Qt.AlignCenter)
        self.spinKL.setReadOnly(False)
        self.spinKL.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinKL.setObjectName("spinKL")
        self.gridLayout.addWidget(self.spinKL, 7, 3, 1, 1)
        self.spinIN = QtWidgets.QSpinBox(formAttribute)
        self.spinIN.setAlignment(QtCore.Qt.AlignCenter)
        self.spinIN.setReadOnly(False)
        self.spinIN.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinIN.setObjectName("spinIN")
        self.gridLayout.addWidget(self.spinIN, 6, 3, 1, 1)
        self.abMR = QtWidgets.QSpinBox(formAttribute)
        self.abMR.setFocusPolicy(QtCore.Qt.NoFocus)
        self.abMR.setWrapping(False)
        self.abMR.setFrame(True)
        self.abMR.setAlignment(QtCore.Qt.AlignCenter)
        self.abMR.setReadOnly(True)
        self.abMR.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.abMR.setProperty("showGroupSeparator", False)
        self.abMR.setObjectName("abMR")
        self.gridLayout.addWidget(self.abMR, 3, 8, 1, 1)
        self.abGS = QtWidgets.QSpinBox(formAttribute)
        self.abGS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.abGS.setWrapping(False)
        self.abGS.setFrame(True)
        self.abGS.setAlignment(QtCore.Qt.AlignCenter)
        self.abGS.setReadOnly(True)
        self.abGS.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.abGS.setProperty("showGroupSeparator", False)
        self.abGS.setObjectName("abGS")
        self.gridLayout.addWidget(self.abGS, 4, 8, 1, 1)
        self.spinGE = QtWidgets.QSpinBox(formAttribute)
        self.spinGE.setAlignment(QtCore.Qt.AlignCenter)
        self.spinGE.setReadOnly(False)
        self.spinGE.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinGE.setObjectName("spinGE")
        self.gridLayout.addWidget(self.spinGE, 4, 3, 1, 1)
        self.spinKO = QtWidgets.QSpinBox(formAttribute)
        self.spinKO.setAlignment(QtCore.Qt.AlignCenter)
        self.spinKO.setReadOnly(False)
        self.spinKO.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinKO.setObjectName("spinKO")
        self.gridLayout.addWidget(self.spinKO, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(formAttribute)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 9, 1, 1)
        self.label_13 = QtWidgets.QLabel(formAttribute)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 6, 1, 1)
        self.pwKL = QtWidgets.QSpinBox(formAttribute)
        self.pwKL.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pwKL.setWrapping(False)
        self.pwKL.setFrame(True)
        self.pwKL.setAlignment(QtCore.Qt.AlignCenter)
        self.pwKL.setReadOnly(True)
        self.pwKL.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pwKL.setProperty("showGroupSeparator", False)
        self.pwKL.setObjectName("pwKL")
        self.gridLayout.addWidget(self.pwKL, 7, 4, 1, 1)
        self.spinMU = QtWidgets.QSpinBox(formAttribute)
        self.spinMU.setAlignment(QtCore.Qt.AlignCenter)
        self.spinMU.setReadOnly(False)
        self.spinMU.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinMU.setObjectName("spinMU")
        self.gridLayout.addWidget(self.spinMU, 3, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(formAttribute)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 6, 1, 1)
        self.label_16 = QtWidgets.QLabel(formAttribute)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(formAttribute)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        self.spinKK = QtWidgets.QSpinBox(formAttribute)
        self.spinKK.setAlignment(QtCore.Qt.AlignCenter)
        self.spinKK.setReadOnly(False)
        self.spinKK.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinKK.setObjectName("spinKK")
        self.gridLayout.addWidget(self.spinKK, 5, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(formAttribute)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.abIN = QtWidgets.QSpinBox(formAttribute)
        self.abIN.setFocusPolicy(QtCore.Qt.NoFocus)
        self.abIN.setWrapping(False)
        self.abIN.setFrame(True)
        self.abIN.setAlignment(QtCore.Qt.AlignCenter)
        self.abIN.setReadOnly(True)
        self.abIN.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.abIN.setProperty("showGroupSeparator", False)
        self.abIN.setObjectName("abIN")
        self.gridLayout.addWidget(self.abIN, 6, 8, 1, 1)
        self.spinCH = QtWidgets.QSpinBox(formAttribute)
        self.spinCH.setAlignment(QtCore.Qt.AlignCenter)
        self.spinCH.setReadOnly(False)
        self.spinCH.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinCH.setObjectName("spinCH")
        self.gridLayout.addWidget(self.spinCH, 8, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(formAttribute)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(formAttribute)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 6, 1, 1)
        self.pwFF = QtWidgets.QSpinBox(formAttribute)
        self.pwFF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pwFF.setWrapping(False)
        self.pwFF.setFrame(True)
        self.pwFF.setAlignment(QtCore.Qt.AlignCenter)
        self.pwFF.setReadOnly(True)
        self.pwFF.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pwFF.setProperty("showGroupSeparator", False)
        self.pwFF.setObjectName("pwFF")
        self.gridLayout.addWidget(self.pwFF, 9, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 10, 6, 1, 1)
        self.label_8 = QtWidgets.QLabel(formAttribute)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 5, 1, 1)
        self.lblKapZugekauft = QtWidgets.QLabel(formAttribute)
        self.lblKapZugekauft.setMinimumSize(QtCore.QSize(100, 0))
        self.lblKapZugekauft.setObjectName("lblKapZugekauft")
        self.gridLayout.addWidget(self.lblKapZugekauft, 9, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(formAttribute)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 6, 1, 1)
        self.label_18 = QtWidgets.QLabel(formAttribute)
        self.label_18.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(formAttribute)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 6, 1, 1)
        self.label_14 = QtWidgets.QLabel(formAttribute)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 8, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(formAttribute)
        self.label_26.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 2, 7, 1, 1)
        self.label_100 = QtWidgets.QLabel(formAttribute)
        self.label_100.setMinimumSize(QtCore.QSize(25, 0))
        self.label_100.setObjectName("label_100")
        self.gridLayout.addWidget(self.label_100, 2, 9, 1, 1)
        self.label_101 = QtWidgets.QLabel(formAttribute)
        self.label_101.setMinimumSize(QtCore.QSize(25, 0))
        self.label_101.setObjectName("label_101")
        self.gridLayout.addWidget(self.label_101, 3, 9, 1, 1)
        self.label_102 = QtWidgets.QLabel(formAttribute)
        self.label_102.setMinimumSize(QtCore.QSize(25, 0))
        self.label_102.setObjectName("label_102")
        self.gridLayout.addWidget(self.label_102, 4, 9, 1, 1)
        self.label_103 = QtWidgets.QLabel(formAttribute)
        self.label_103.setMinimumSize(QtCore.QSize(25, 0))
        self.label_103.setObjectName("label_103")
        self.gridLayout.addWidget(self.label_103, 5, 9, 1, 1)
        self.label_104 = QtWidgets.QLabel(formAttribute)
        self.label_104.setMinimumSize(QtCore.QSize(25, 0))
        self.label_104.setObjectName("label_104")
        self.gridLayout.addWidget(self.label_104, 6, 9, 1, 1)
        self.label_27 = QtWidgets.QLabel(formAttribute)
        self.label_27.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 3, 7, 1, 1)
        self.label_28 = QtWidgets.QLabel(formAttribute)
        self.label_28.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 4, 7, 1, 1)
        self.label_29 = QtWidgets.QLabel(formAttribute)
        self.label_29.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 5, 7, 1, 1)
        self.label_30 = QtWidgets.QLabel(formAttribute)
        self.label_30.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 6, 7, 1, 1)
        self.label_31 = QtWidgets.QLabel(formAttribute)
        self.label_31.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 8, 7, 1, 1)
        self.lblKap = QtWidgets.QLabel(formAttribute)
        self.lblKap.setMinimumSize(QtCore.QSize(26, 0))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lblKap.setFont(font)
        self.lblKap.setAlignment(QtCore.Qt.AlignCenter)
        self.lblKap.setObjectName("lblKap")
        self.gridLayout.addWidget(self.lblKap, 9, 7, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_33 = QtWidgets.QLabel(formAttribute)
        self.label_33.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout.addWidget(self.label_33)
        self.spinAsP = QtWidgets.QSpinBox(formAttribute)
        self.spinAsP.setMaximumSize(QtCore.QSize(37, 16777215))
        self.spinAsP.setAlignment(QtCore.Qt.AlignCenter)
        self.spinAsP.setReadOnly(False)
        self.spinAsP.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinAsP.setPrefix("")
        self.spinAsP.setObjectName("spinAsP")
        self.horizontalLayout.addWidget(self.spinAsP)
        self.label_15 = QtWidgets.QLabel(formAttribute)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 9, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_34 = QtWidgets.QLabel(formAttribute)
        self.label_34.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_2.addWidget(self.label_34)
        self.spinKaP = QtWidgets.QSpinBox(formAttribute)
        self.spinKaP.setMaximumSize(QtCore.QSize(37, 16777215))
        self.spinKaP.setAlignment(QtCore.Qt.AlignCenter)
        self.spinKaP.setReadOnly(False)
        self.spinKaP.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinKaP.setObjectName("spinKaP")
        self.horizontalLayout_2.addWidget(self.spinKaP)
        self.label_32 = QtWidgets.QLabel(formAttribute)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_2.addWidget(self.label_32)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 9, 1, 1)
        self.abAsP = QtWidgets.QSpinBox(formAttribute)
        self.abAsP.setFocusPolicy(QtCore.Qt.NoFocus)
        self.abAsP.setAlignment(QtCore.Qt.AlignCenter)
        self.abAsP.setReadOnly(True)
        self.abAsP.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.abAsP.setMaximum(999)
        self.abAsP.setObjectName("abAsP")
        self.gridLayout.addWidget(self.abAsP, 8, 8, 1, 1)
        self.abKaP = QtWidgets.QSpinBox(formAttribute)
        self.abKaP.setFocusPolicy(QtCore.Qt.NoFocus)
        self.abKaP.setAlignment(QtCore.Qt.AlignCenter)
        self.abKaP.setReadOnly(True)
        self.abKaP.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.abKaP.setMaximum(999)
        self.abKaP.setObjectName("abKaP")
        self.gridLayout.addWidget(self.abKaP, 9, 8, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(formAttribute)
        QtCore.QMetaObject.connectSlotsByName(formAttribute)
        formAttribute.setTabOrder(self.spinKO, self.spinMU)
        formAttribute.setTabOrder(self.spinMU, self.spinGE)
        formAttribute.setTabOrder(self.spinGE, self.spinKK)
        formAttribute.setTabOrder(self.spinKK, self.spinIN)
        formAttribute.setTabOrder(self.spinIN, self.spinKL)
        formAttribute.setTabOrder(self.spinKL, self.spinCH)
        formAttribute.setTabOrder(self.spinCH, self.spinFF)
        formAttribute.setTabOrder(self.spinFF, self.pwKO)
        formAttribute.setTabOrder(self.pwKO, self.pwMU)
        formAttribute.setTabOrder(self.pwMU, self.pwGE)
        formAttribute.setTabOrder(self.pwGE, self.pwKK)
        formAttribute.setTabOrder(self.pwKK, self.pwIN)
        formAttribute.setTabOrder(self.pwIN, self.pwKL)
        formAttribute.setTabOrder(self.pwKL, self.pwCH)
        formAttribute.setTabOrder(self.pwCH, self.pwFF)
        formAttribute.setTabOrder(self.pwFF, self.abWS)
        formAttribute.setTabOrder(self.abWS, self.abMR)
        formAttribute.setTabOrder(self.abMR, self.abGS)
        formAttribute.setTabOrder(self.abGS, self.abSB)
        formAttribute.setTabOrder(self.abSB, self.abIN)

    def retranslateUi(self, formAttribute):
        _translate = QtCore.QCoreApplication.translate
        formAttribute.setWindowTitle(_translate("formAttribute", "Attribute"))
        self.label_17.setText(_translate("formAttribute", "PW"))
        self.label.setText(_translate("formAttribute", "Konstitution"))
        self.label_24.setText(_translate("formAttribute", "CH"))
        self.label_22.setText(_translate("formAttribute", "IN"))
        self.label_20.setText(_translate("formAttribute", "GE"))
        self.label_23.setText(_translate("formAttribute", "KL"))
        self.label_25.setText(_translate("formAttribute", "FF"))
        self.label_19.setText(_translate("formAttribute", "MU"))
        self.label_21.setText(_translate("formAttribute", "KK"))
        self.label_3.setText(_translate("formAttribute", "Gewandheit"))
        self.label_6.setText(_translate("formAttribute", "Klugheit"))
        self.label_4.setText(_translate("formAttribute", "Körperkraft"))
        self.label_13.setText(_translate("formAttribute", "Initiative"))
        self.label_12.setText(_translate("formAttribute", "Schadensbonus"))
        self.label_16.setText(_translate("formAttribute", "Wert"))
        self.label_5.setText(_translate("formAttribute", "Intuition"))
        self.label_2.setText(_translate("formAttribute", "Mut"))
        self.label_7.setText(_translate("formAttribute", "Charisma"))
        self.label_9.setText(_translate("formAttribute", "Wundschwelle"))
        self.label_8.setText(_translate("formAttribute", "Fingerfertigkeit"))
        self.lblKapZugekauft.setText(_translate("formAttribute", "Karmaenergie"))
        self.label_10.setText(_translate("formAttribute", "Magieresistenz"))
        self.label_18.setText(_translate("formAttribute", "KO"))
        self.label_11.setText(_translate("formAttribute", "Geschwindigkeit"))
        self.label_14.setText(_translate("formAttribute", "Astralenergie"))
        self.label_26.setText(_translate("formAttribute", "WS"))
        self.label_100.setText(_translate("formAttribute", "(4 + 1 je 4 KO)"))
        self.label_101.setText(_translate("formAttribute", "(4 + 1 je 4 MU)"))
        self.label_102.setText(_translate("formAttribute", "(4 + 1 je 4 GE)"))
        self.label_103.setText(_translate("formAttribute", "(1 je 4 KK)"))
        self.label_104.setText(_translate("formAttribute", "(IN)"))
        self.label_27.setText(_translate("formAttribute", "MR"))
        self.label_28.setText(_translate("formAttribute", "GS"))
        self.label_29.setText(_translate("formAttribute", "SB"))
        self.label_30.setText(_translate("formAttribute", "INI"))
        self.label_31.setText(_translate("formAttribute", "AsP"))
        self.lblKap.setText(_translate("formAttribute", "KaP"))
        self.label_33.setText(_translate("formAttribute", "+"))
        self.label_15.setText(_translate("formAttribute", "Zugekauft"))
        self.label_34.setText(_translate("formAttribute", "+"))
        self.label_32.setText(_translate("formAttribute", "Zugekauft"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formAttribute = QtWidgets.QWidget()
    ui = Ui_formAttribute()
    ui.setupUi(formAttribute)
    formAttribute.show()
    sys.exit(app.exec_())
