# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dw_containers_no_tabs.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from pyqtgraph.Qt import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(497, 566)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_45 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_45.setObjectName(_fromUtf8("gridLayout_45"))
        self.label_126 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_126.setFont(font)
        self.label_126.setObjectName(_fromUtf8("label_126"))
        self.gridLayout_45.addWidget(self.label_126, 0, 3, 2, 1)
        self.label_124 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_124.setFont(font)
        self.label_124.setObjectName(_fromUtf8("label_124"))
        self.gridLayout_45.addWidget(self.label_124, 0, 2, 2, 1)
        self.label_133 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_133.setFont(font)
        self.label_133.setObjectName(_fromUtf8("label_133"))
        self.gridLayout_45.addWidget(self.label_133, 8, 0, 1, 2)
        self.groupBoxDis_2 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBoxDis_2.setEnabled(False)
        self.groupBoxDis_2.setObjectName(_fromUtf8("groupBoxDis_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBoxDis_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_7 = QtGui.QLabel(self.groupBoxDis_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.gridLayout_45.addWidget(self.groupBoxDis_2, 2, 3, 1, 1)
        self.stackedWidget_2 = QtGui.QStackedWidget(self.dockWidgetContents)
        self.stackedWidget_2.setObjectName(_fromUtf8("stackedWidget_2"))
        self.page1_2 = QtGui.QWidget()
        self.page1_2.setObjectName(_fromUtf8("page1_2"))
        self.gridLayout_35 = QtGui.QGridLayout(self.page1_2)
        self.gridLayout_35.setObjectName(_fromUtf8("gridLayout_35"))
        self.label_57 = QtGui.QLabel(self.page1_2)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.gridLayout_35.addWidget(self.label_57, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page1_2)
        self.page2_2 = QtGui.QWidget()
        self.page2_2.setObjectName(_fromUtf8("page2_2"))
        self.gridLayout_36 = QtGui.QGridLayout(self.page2_2)
        self.gridLayout_36.setObjectName(_fromUtf8("gridLayout_36"))
        self.label_58 = QtGui.QLabel(self.page2_2)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.gridLayout_36.addWidget(self.label_58, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page2_2)
        self.gridLayout_45.addWidget(self.stackedWidget_2, 5, 2, 1, 1)
        self.stackedWidgetDis_2 = QtGui.QStackedWidget(self.dockWidgetContents)
        self.stackedWidgetDis_2.setEnabled(False)
        self.stackedWidgetDis_2.setObjectName(_fromUtf8("stackedWidgetDis_2"))
        self.page1Dis_2 = QtGui.QWidget()
        self.page1Dis_2.setObjectName(_fromUtf8("page1Dis_2"))
        self.gridLayout_37 = QtGui.QGridLayout(self.page1Dis_2)
        self.gridLayout_37.setObjectName(_fromUtf8("gridLayout_37"))
        self.label_113 = QtGui.QLabel(self.page1Dis_2)
        self.label_113.setObjectName(_fromUtf8("label_113"))
        self.gridLayout_37.addWidget(self.label_113, 0, 0, 1, 1)
        self.stackedWidgetDis_2.addWidget(self.page1Dis_2)
        self.page2Dis_2 = QtGui.QWidget()
        self.page2Dis_2.setObjectName(_fromUtf8("page2Dis_2"))
        self.gridLayout_38 = QtGui.QGridLayout(self.page2Dis_2)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.label_114 = QtGui.QLabel(self.page2Dis_2)
        self.label_114.setObjectName(_fromUtf8("label_114"))
        self.gridLayout_38.addWidget(self.label_114, 0, 0, 1, 1)
        self.stackedWidgetDis_2.addWidget(self.page2Dis_2)
        self.gridLayout_45.addWidget(self.stackedWidgetDis_2, 5, 3, 1, 1)
        self.label_131 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_131.setFont(font)
        self.label_131.setObjectName(_fromUtf8("label_131"))
        self.gridLayout_45.addWidget(self.label_131, 6, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.dockWidgetContents)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_43 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_43.setObjectName(_fromUtf8("gridLayout_43"))
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_43.addWidget(self.label_9, 0, 0, 1, 1)
        self.gridLayout_45.addWidget(self.frame_2, 6, 2, 1, 1)
        self.frameDis_2 = QtGui.QFrame(self.dockWidgetContents)
        self.frameDis_2.setEnabled(False)
        self.frameDis_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameDis_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frameDis_2.setObjectName(_fromUtf8("frameDis_2"))
        self.gridLayout_40 = QtGui.QGridLayout(self.frameDis_2)
        self.gridLayout_40.setObjectName(_fromUtf8("gridLayout_40"))
        self.label_8 = QtGui.QLabel(self.frameDis_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_40.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_45.addWidget(self.frameDis_2, 6, 3, 1, 1)
        self.label_132 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_132.setFont(font)
        self.label_132.setObjectName(_fromUtf8("label_132"))
        self.gridLayout_45.addWidget(self.label_132, 7, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)
        self.gridLayout_45.addWidget(self.groupBox_2, 2, 2, 1, 1)
        self.mdiAreaDis_2 = QtGui.QMdiArea(self.dockWidgetContents)
        self.mdiAreaDis_2.setEnabled(False)
        self.mdiAreaDis_2.setObjectName(_fromUtf8("mdiAreaDis_2"))
        self.subwindow1Dis_2 = QtGui.QWidget()
        self.subwindow1Dis_2.setObjectName(_fromUtf8("subwindow1Dis_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.subwindow1Dis_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_111 = QtGui.QLabel(self.subwindow1Dis_2)
        self.label_111.setObjectName(_fromUtf8("label_111"))
        self.verticalLayout_9.addWidget(self.label_111)
        self.subwindow2Dis_2 = QtGui.QWidget()
        self.subwindow2Dis_2.setObjectName(_fromUtf8("subwindow2Dis_2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.subwindow2Dis_2)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_112 = QtGui.QLabel(self.subwindow2Dis_2)
        self.label_112.setObjectName(_fromUtf8("label_112"))
        self.verticalLayout_10.addWidget(self.label_112)
        self.gridLayout_45.addWidget(self.mdiAreaDis_2, 8, 3, 1, 1)
        self.label_127 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_127.setFont(font)
        self.label_127.setObjectName(_fromUtf8("label_127"))
        self.gridLayout_45.addWidget(self.label_127, 2, 0, 1, 2)
        self.widget_2 = QtGui.QWidget(self.dockWidgetContents)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_39 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_39.setObjectName(_fromUtf8("gridLayout_39"))
        self.label_59 = QtGui.QLabel(self.widget_2)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout_39.addWidget(self.label_59, 0, 0, 1, 1)
        self.gridLayout_45.addWidget(self.widget_2, 7, 2, 1, 1)
        self.widgetDis_2 = QtGui.QWidget(self.dockWidgetContents)
        self.widgetDis_2.setEnabled(False)
        self.widgetDis_2.setObjectName(_fromUtf8("widgetDis_2"))
        self.gridLayout_44 = QtGui.QGridLayout(self.widgetDis_2)
        self.gridLayout_44.setObjectName(_fromUtf8("gridLayout_44"))
        self.label_125 = QtGui.QLabel(self.widgetDis_2)
        self.label_125.setObjectName(_fromUtf8("label_125"))
        self.gridLayout_44.addWidget(self.label_125, 0, 0, 1, 1)
        self.gridLayout_45.addWidget(self.widgetDis_2, 7, 3, 1, 1)
        self.mdiArea_2 = QtGui.QMdiArea(self.dockWidgetContents)
        self.mdiArea_2.setObjectName(_fromUtf8("mdiArea_2"))
        self.subwindow1_2 = QtGui.QWidget()
        self.subwindow1_2.setObjectName(_fromUtf8("subwindow1_2"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.subwindow1_2)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_29 = QtGui.QLabel(self.subwindow1_2)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.verticalLayout_11.addWidget(self.label_29)
        self.subwindow2_2 = QtGui.QWidget()
        self.subwindow2_2.setObjectName(_fromUtf8("subwindow2_2"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.subwindow2_2)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_56 = QtGui.QLabel(self.subwindow2_2)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.verticalLayout_12.addWidget(self.label_56)
        self.gridLayout_45.addWidget(self.mdiArea_2, 8, 2, 1, 1)
        self.label_128 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_128.setFont(font)
        self.label_128.setObjectName(_fromUtf8("label_128"))
        self.gridLayout_45.addWidget(self.label_128, 3, 0, 1, 2)
        self.scrollArea_2 = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 181, 246))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_70 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.verticalLayout_14.addWidget(self.label_70)
        self.label_71 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.verticalLayout_14.addWidget(self.label_71)
        self.label_75 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.verticalLayout_14.addWidget(self.label_75)
        self.label_76 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.verticalLayout_14.addWidget(self.label_76)
        self.label_77 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.verticalLayout_14.addWidget(self.label_77)
        self.label_78 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.verticalLayout_14.addWidget(self.label_78)
        self.label_79 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.verticalLayout_14.addWidget(self.label_79)
        self.label_80 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.verticalLayout_14.addWidget(self.label_80)
        self.label_81 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_81.setObjectName(_fromUtf8("label_81"))
        self.verticalLayout_14.addWidget(self.label_81)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_45.addWidget(self.scrollArea_2, 3, 2, 1, 1)
        self.scrollAreaDis_2 = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollAreaDis_2.setEnabled(False)
        self.scrollAreaDis_2.setWidgetResizable(True)
        self.scrollAreaDis_2.setObjectName(_fromUtf8("scrollAreaDis_2"))
        self.scrollAreaWidgetContentsDis_2 = QtGui.QWidget()
        self.scrollAreaWidgetContentsDis_2.setGeometry(QtCore.QRect(0, 0, 181, 246))
        self.scrollAreaWidgetContentsDis_2.setObjectName(_fromUtf8("scrollAreaWidgetContentsDis_2"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.scrollAreaWidgetContentsDis_2)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_115 = QtGui.QLabel(self.scrollAreaWidgetContentsDis_2)
        self.label_115.setObjectName(_fromUtf8("label_115"))
        self.verticalLayout_13.addWidget(self.label_115)
        self.label_116 = QtGui.QLabel(self.scrollAreaWidgetContentsDis_2)
        self.label_116.setObjectName(_fromUtf8("label_116"))
        self.verticalLayout_13.addWidget(self.label_116)
        self.label_117 = QtGui.QLabel(self.scrollAreaWidgetContentsDis_2)
        self.label_117.setObjectName(_fromUtf8("label_117"))
        self.verticalLayout_13.addWidget(self.label_117)
        self.label_118 = QtGui.QLabel(self.scrollAreaWidgetContentsDis_2)
        self.label_118.setObjectName(_fromUtf8("label_118"))
        self.verticalLayout_13.addWidget(self.label_118)
        self.label_119 = QtGui.QLabel(self.scrollAreaWidgetContentsDis_2)
        self.label_119.setObjectName(_fromUtf8("label_119"))
        self.verticalLayout_13.addWidget(self.label_119)
        self.label_120 = QtGui.QLabel(self.scrollAreaWidgetContentsDis_2)
        self.label_120.setObjectName(_fromUtf8("label_120"))
        self.verticalLayout_13.addWidget(self.label_120)
        self.label_121 = QtGui.QLabel(self.scrollAreaWidgetContentsDis_2)
        self.label_121.setObjectName(_fromUtf8("label_121"))
        self.verticalLayout_13.addWidget(self.label_121)
        self.label_122 = QtGui.QLabel(self.scrollAreaWidgetContentsDis_2)
        self.label_122.setObjectName(_fromUtf8("label_122"))
        self.verticalLayout_13.addWidget(self.label_122)
        self.label_123 = QtGui.QLabel(self.scrollAreaWidgetContentsDis_2)
        self.label_123.setObjectName(_fromUtf8("label_123"))
        self.verticalLayout_13.addWidget(self.label_123)
        self.scrollAreaDis_2.setWidget(self.scrollAreaWidgetContentsDis_2)
        self.gridLayout_45.addWidget(self.scrollAreaDis_2, 3, 3, 1, 1)
        self.label_129 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_129.setFont(font)
        self.label_129.setObjectName(_fromUtf8("label_129"))
        self.gridLayout_45.addWidget(self.label_129, 4, 0, 1, 2)
        self.toolBox_2 = QtGui.QToolBox(self.dockWidgetContents)
        self.toolBox_2.setObjectName(_fromUtf8("toolBox_2"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 196, 73))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.gridLayout_41 = QtGui.QGridLayout(self.page_3)
        self.gridLayout_41.setObjectName(_fromUtf8("gridLayout_41"))
        self.label_60 = QtGui.QLabel(self.page_3)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.gridLayout_41.addWidget(self.label_60, 2, 0, 1, 1)
        self.toolBox_2.addItem(self.page_3, _fromUtf8(""))
        self.page_8 = QtGui.QWidget()
        self.page_8.setGeometry(QtCore.QRect(0, 0, 163, 38))
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.gridLayout_42 = QtGui.QGridLayout(self.page_8)
        self.gridLayout_42.setObjectName(_fromUtf8("gridLayout_42"))
        self.label_61 = QtGui.QLabel(self.page_8)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout_42.addWidget(self.label_61, 0, 0, 1, 1)
        self.toolBox_2.addItem(self.page_8, _fromUtf8(""))
        self.gridLayout_45.addWidget(self.toolBox_2, 4, 2, 1, 1)
        self.toolBoxDis_2 = QtGui.QToolBox(self.dockWidgetContents)
        self.toolBoxDis_2.setEnabled(False)
        self.toolBoxDis_2.setObjectName(_fromUtf8("toolBoxDis_2"))
        self.page_6 = QtGui.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 196, 73))
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.gridLayout_29 = QtGui.QGridLayout(self.page_6)
        self.gridLayout_29.setObjectName(_fromUtf8("gridLayout_29"))
        self.label_109 = QtGui.QLabel(self.page_6)
        self.label_109.setObjectName(_fromUtf8("label_109"))
        self.gridLayout_29.addWidget(self.label_109, 2, 0, 1, 1)
        self.toolBoxDis_2.addItem(self.page_6, _fromUtf8(""))
        self.page_7 = QtGui.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 163, 38))
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.gridLayout_34 = QtGui.QGridLayout(self.page_7)
        self.gridLayout_34.setObjectName(_fromUtf8("gridLayout_34"))
        self.label_110 = QtGui.QLabel(self.page_7)
        self.label_110.setObjectName(_fromUtf8("label_110"))
        self.gridLayout_34.addWidget(self.label_110, 0, 0, 1, 1)
        self.toolBoxDis_2.addItem(self.page_7, _fromUtf8(""))
        self.gridLayout_45.addWidget(self.toolBoxDis_2, 4, 3, 1, 1)
        self.label_130 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_130.setFont(font)
        self.label_130.setObjectName(_fromUtf8("label_130"))
        self.gridLayout_45.addWidget(self.label_130, 5, 0, 1, 2)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidgetDis_2.setCurrentIndex(1)
        self.toolBox_2.setCurrentIndex(0)
        self.toolBoxDis_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "Containers - No Tabs", None))
        self.label_126.setText(_translate("DockWidget", "Disabled", None))
        self.label_124.setText(_translate("DockWidget", "Enabled", None))
        self.label_133.setText(_translate("DockWidget", "MDI Area", None))
        self.groupBoxDis_2.setTitle(_translate("DockWidget", "GroupBox", None))
        self.label_7.setText(_translate("DockWidget", "Inside GroupBox", None))
        self.stackedWidget_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.stackedWidget_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.stackedWidget_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_57.setText(_translate("DockWidget", "Inside Stacked Page 1", None))
        self.label_58.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_58.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_58.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_58.setText(_translate("DockWidget", "Inside Stacked Page 2", None))
        self.stackedWidgetDis_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.stackedWidgetDis_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.stackedWidgetDis_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_113.setText(_translate("DockWidget", "Inside Stacked Page 1", None))
        self.label_114.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_114.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_114.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_114.setText(_translate("DockWidget", "Inside Stacked Page 2", None))
        self.label_131.setText(_translate("DockWidget", "Frame", None))
        self.frame_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.frame_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.frame_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_9.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_9.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_9.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_9.setText(_translate("DockWidget", "Inside Frame", None))
        self.frameDis_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.frameDis_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.frameDis_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_8.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_8.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_8.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_8.setText(_translate("DockWidget", "Inside Frame", None))
        self.label_132.setText(_translate("DockWidget", "Widget", None))
        self.groupBox_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.groupBox_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.groupBox_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.groupBox_2.setTitle(_translate("DockWidget", "GroupBox", None))
        self.label_10.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_10.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_10.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_10.setText(_translate("DockWidget", "Inside GroupBox", None))
        self.subwindow1Dis_2.setWindowTitle(_translate("DockWidget", "Subwindow", None))
        self.label_111.setText(_translate("DockWidget", "Inside MDI Area 1", None))
        self.subwindow2Dis_2.setWindowTitle(_translate("DockWidget", "Subwindow", None))
        self.label_112.setText(_translate("DockWidget", "Inside MDI Area 2 ", None))
        self.label_127.setText(_translate("DockWidget", "GroupBox", None))
        self.widget_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.widget_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.widget_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_59.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_59.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_59.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_59.setText(_translate("DockWidget", "Inside Widget", None))
        self.widgetDis_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.widgetDis_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.widgetDis_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_125.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_125.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_125.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_125.setText(_translate("DockWidget", "Inside Widget", None))
        self.subwindow1_2.setWindowTitle(_translate("DockWidget", "Subwindow", None))
        self.label_29.setText(_translate("DockWidget", "Inside MDI Area 1", None))
        self.subwindow2_2.setWindowTitle(_translate("DockWidget", "Subwindow", None))
        self.label_56.setText(_translate("DockWidget", "Inside MDI Area 2 ", None))
        self.label_128.setText(_translate("DockWidget", "ScroolArea", None))
        self.scrollArea_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.scrollArea_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.scrollArea_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_70.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_70.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_70.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_70.setText(_translate("DockWidget", "Inside ScroolArea", None))
        self.label_71.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_71.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_71.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_71.setText(_translate("DockWidget", "ScroolArea ", None))
        self.label_75.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_75.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_75.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_75.setText(_translate("DockWidget", "Inside ScroolArea ", None))
        self.label_76.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_76.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_76.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_76.setText(_translate("DockWidget", "ScroolArea", None))
        self.label_77.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_77.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_77.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_77.setText(_translate("DockWidget", "Inside ScroolArea", None))
        self.label_78.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_78.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_78.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_78.setText(_translate("DockWidget", "ScroolArea", None))
        self.label_79.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_79.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_79.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_79.setText(_translate("DockWidget", "Inside ScroolArea", None))
        self.label_80.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_80.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_80.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_80.setText(_translate("DockWidget", "ScroolArea", None))
        self.label_81.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_81.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_81.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_81.setText(_translate("DockWidget", "Inside ScroolArea", None))
        self.scrollAreaDis_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.scrollAreaDis_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.scrollAreaDis_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_115.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_115.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_115.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_115.setText(_translate("DockWidget", "Inside ScroolArea", None))
        self.label_116.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_116.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_116.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_116.setText(_translate("DockWidget", "ScroolArea ", None))
        self.label_117.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_117.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_117.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_117.setText(_translate("DockWidget", "Inside ScroolArea ", None))
        self.label_118.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_118.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_118.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_118.setText(_translate("DockWidget", "ScroolArea", None))
        self.label_119.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_119.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_119.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_119.setText(_translate("DockWidget", "Inside ScroolArea", None))
        self.label_120.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_120.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_120.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_120.setText(_translate("DockWidget", "ScroolArea", None))
        self.label_121.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_121.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_121.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_121.setText(_translate("DockWidget", "Inside ScroolArea", None))
        self.label_122.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_122.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_122.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_122.setText(_translate("DockWidget", "ScroolArea", None))
        self.label_123.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_123.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_123.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_123.setText(_translate("DockWidget", "Inside ScroolArea", None))
        self.label_129.setText(_translate("DockWidget", "ToolBox", None))
        self.toolBox_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.toolBox_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.toolBox_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_60.setText(_translate("DockWidget", "Inside ToolBox Page 1", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), _translate("DockWidget", "Page 1", None))
        self.label_61.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_61.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_61.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_61.setText(_translate("DockWidget", "Inside ToolBox Page 2", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_8), _translate("DockWidget", "Page 2", None))
        self.toolBoxDis_2.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.toolBoxDis_2.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.toolBoxDis_2.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_109.setText(_translate("DockWidget", "Inside ToolBox Page 1", None))
        self.toolBoxDis_2.setItemText(self.toolBoxDis_2.indexOf(self.page_6), _translate("DockWidget", "Page 1", None))
        self.label_110.setToolTip(_translate("DockWidget", "This is a tool tip", None))
        self.label_110.setStatusTip(_translate("DockWidget", "This is a status tip", None))
        self.label_110.setWhatsThis(_translate("DockWidget", "This is \"what is this\"", None))
        self.label_110.setText(_translate("DockWidget", "Inside ToolBox Page 2", None))
        self.toolBoxDis_2.setItemText(self.toolBoxDis_2.indexOf(self.page_7), _translate("DockWidget", "Page 2", None))
        self.label_130.setText(_translate("DockWidget", "Stacked", None))

