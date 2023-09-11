# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(799, 553)
        Widget.setMaximumSize(QSize(167772, 16777215))
        Widget.setMouseTracking(False)
        Widget.setAcceptDrops(False)
        self.formLayout = QFormLayout(Widget)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 531, 371))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(Widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(349, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.verticalLayout_2.setStretch(0, 7)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.widget_3 = QWidget(Widget)
        self.widget_3.setObjectName(u"widget_3")
        self.textEdit = QTextEdit(self.widget_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 29, 361, 291))
        self.textEdit.setMaximumSize(QSize(167772, 16777215))
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 181, 31))

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(Widget)
        self.widget_4.setObjectName(u"widget_4")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 81, 31))
        self.textEdit_2 = QTextEdit(self.widget_4)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 30, 401, 261))

        self.verticalLayout.addWidget(self.widget_4)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.pushButton_5 = QPushButton(Widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(2, 1)

        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"MainFun", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u56fe\u7247", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u56fe\u7247detect\u8f93\u51fa", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"GPT\u63cf\u8ff0", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u751f\u6210\u7684\u97f3\u9891", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"\u70b9\u51fb\u64ad\u653e", None))
    # retranslateUi

