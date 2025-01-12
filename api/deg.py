import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtWidgets import QMessageBox



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
    
    
    def end(self):
        self.close()