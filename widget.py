# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
#from PyQt5 import QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui.ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.openFolder)



    @Slot()
    def openFolder(self):
        folder_path = r'C:\Users\ww\Desktop\untitled\ai-eye-client'
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", folder_path, "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)
#        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "floder")
#        if folder_path:
#            file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", folder_path, "Image Files (*.png *.jpg *.bmp)")
#            if file_path:
#                pixmap = QPixmap(file_path)
#                self.ui.label.setPixmap(pixmap)
#                self.ui.label.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
