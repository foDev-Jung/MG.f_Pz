import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer, pyqtSignal

from PyQt5 import uic

form_class = uic.loadUiType("MainWindow.ui")[0]

class ClickLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.refresh.clicked.connect(self.refresh_btn_clicked)
        self.insert.clicked.connect(self.insert_btn_clicked)
    
    def generate_img(self):
        imageName = "dummy_{0}"
        frameName = "self.g_img_{0}"
        for i in range(1,4):
            frame_label = eval(frameName.format(i))
            image_map = QPixmap(imageName.format(i))
            
            # set size 
            frame_label.setPixmap(image_map)
            frame_label.setScaledContents(True)
            frame_label.clicked.connect(self.on_product_clicked)
    
    def on_product_clicked(self):
        frame_label = self.sender()

    def insert_btn_clicked(self):
        #frame_label = self.sender()
        pass
        

    def refresh_btn_clicked(self):
        self.generate_img()
        
    '''
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
    '''
 
if __name__ == "__main__":
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   app.exec_()

