import sys, random
import glob

#print(glob.glob("sample/*.png"))
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
#from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer, pyqtSignal

from PyQt5 import uic

form_class = uic.loadUiType("MainWindow.ui")[0]

class SampleParser():
    def __init__(self):
        self.img_list = glob.glob("sample/*.png")

    def get_category(self,filename):
        category = filename.split('\\')[-1]
        category = filename.split('_')[0]
        return category

    def get_file_list(self,filename):
        if filename == None:
            return self.img_list
        else:
            category = self.get_category(filename)
            return [img for img in self.img_list if category == self.get_category(img) ]

class ClickLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)
'''
class SelectedLabel(QLabel):
    
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e):
        self.setText(e.mimeData().text())
        self.parent().label.setPixmap(QPixmap(m.urls()[0].toLocalFile())) '''

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.initialize()

        self.sample_parser = SampleParser()
        self.insert_num = 0
        self.extract_fileName = None

        self.refresh.clicked.connect(self.refresh_btn_clicked)
        self.insert.clicked.connect(self.insert_btn_clicked)
        self.extract.clicked.connect(self.extract_btn_clicked)
        self.un_extract.clicked.connect(self.un_extract_btn_clicked)
    
    def initialize(self):
        self.parameter()
    
    def parameter(self):
        img_resource = ['SOFF.png','NB.png','BB.png']
        label_name = 'self.label_{0}'
        for i, resource in enumerate(img_resource):
            label = eval(label_name.format(i+1))
            label.setPixmap(QPixmap(resource))
            label.setScaledContents(True)

    def generate_img(self):
        #imageName = "sample/dummy_{0}"
        fileName = self.sample_parser.get_file_list(self.extract_fileName)
        random.shuffle(fileName)

        frameName = "self.g_img_{0}"
        for i in range(1,10):
            image_map = QPixmap(fileName[i-1])

            frame_label = eval(frameName.format(i))
            # down casting
            frame_label.__class__ = ClickLabel 
            
            # set size 
            frame_label.setPixmap(image_map)
            frame_label.setScaledContents(True)
            frame_label.clicked.connect(self.on_product_clicked)
            frame_label.fileName = fileName[i-1]
    
    def on_product_clicked(self):
        frame_label = self.sender()
        
        self.selected_frame.setPixmap(frame_label.pixmap())
        self.selected_frame.setScaledContents(True)
        self.selected_frame.fileName = frame_label.fileName

    def insert_btn_clicked(self):
        self.insert_num += 1
        frameName = "self.storage_{0}"
        frame_label = eval(frameName.format(self.insert_num))

        frame_label.setPixmap(self.selected_frame.pixmap())
        frame_label.setScaledContents(True)

    def refresh_btn_clicked(self):
        self.generate_img()
    
    def extract_btn_clicked(self):
        self.extract_fileName = self.selected_frame.fileName

    def un_extract_btn_clicked(self):
        self.extract_fileName = None

        
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

