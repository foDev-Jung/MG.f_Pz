import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QMainWindow, QGridLayout, QDesktopWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout,QGridLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QAction, qApp, QToolTip, QCheckBox, QComboBox, QProgressBar
from PyQt5.QtWidgets import QFrame, QSplitter

from PyQt5.QtGui import QIcon, QFont, QPixmap

from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer

# Windows widgets 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = FormWidget(self)
        self.setCentralWidget(self.main_widget)
        self.init_UI()
    
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar.showMessage(sender.text() + ' was clicked')

    def init_UI(self):
        # icon image
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        # action shortcut
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # menuBar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        # statusBar
        self.statusBar()
        #self.statusBar().showMessage('Ready')
        #self.statusBar().currentMessage()

        # Retrieve Center points of Desktop 
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle = self.frameGeometry()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.setWindowTitle('Puzzle Map Generator_v1')
        self.setWindowIcon(QIcon('web.png'))
        #self.setGeometry(300, 300, 560, 560)
        self.show()

#  widgets about forms
class FormWidget(QWidget):

    def __init__(self,parent):
        super(FormWidget, self).__init__(parent)
        self.step = 0
        self._width = 640
        self._height = 480
        self.setStyleSheet("""
               background-color: black;
               color: white;
               font: bold;
               padding: 6px;
               border-width: 2px;
               border-style: solid;
               border-radius: 16px;
               border-color: white;
           """)

        self.setMinimumSize(self._width, self._height)
        self.initUI()
    
    def changeTitle(self,state):
            if state == Qt.Checked:
                self.setWindowTitle('QCheckBox')
            else:
                self.setWindowTitle(' ')
    
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

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

    def initUI(self):
        
        '''
        # urllib를 이용하여 웹에서 사진데이터를 가져온 후 저장하는 코드
        import urllib.request
        urlString = https://avatars1.githubusercontent.com/u/44885477?s=460&v=4
        imageFromWeb = urllib.request.urlopen(urlString).read()

        # 사진데이터를 이용해 객체에 이미지를 load하는 코드
        qPixmapVar = QPixmap()
        qPixmapVar.loadFromDate(imageFromWeb)

        #qPixmapVar.save(파일명)
        '''

        # 상대경로
        #qPixmapVar.load('dummy_1.jpg')
        #img_lbl = QLabel()
        #img_lbl.setPixmap(qPixmapVar)
        '''pixmap = QPixmap()
        pixmap.load('dummy_1.jpg')
        pixmap = pixmap.scaledToWidth(25)
        pixmap = pixmap.scaledToHeight(25)
        '''

        # tool tip
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
    
        # Splitter
        sample_img_frame_list = []
        for _ in range(0,9):
            
            sample_img = QFrame()
            #sample_img.resize(30,30)
            #sample_img.setPixmap(pixmap)

            sample_img.setStyleSheet("background-color: rgb(200, 255, 255)")
            #sample_img.setFrameShape(QFrame.Box)
            #sample_img.setFrameShadow(QFrame.Plain)

            #sample_img.setFrameShape(QFrame.StyledPanel)
            #sample_img.setFrameShape(QFrame.Panel)
            #sample_img.setFrameShape(QFrame.WinPanel)
            sample_img_frame_list.append(sample_img)
        # QFrame 이 parent class of QLabel
        selected_img = QFrame()
        parameter = QFrame()

        save_img=QFrame()

        # Refresh button
        # Fill button
        # Insert button
        # Load button
        # Save Button
        
        refresh_btn = QPushButton('Refresh', self)
        fill_btn = QPushButton('Fill', self)
        select_btn = QPushButton('Select', self)
        load_btn = QPushButton('Load', self)
        save_btn = QPushButton('Save', self)

        midleft = QFrame()
        #midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)
        
        bottom = QFrame()
        #bottom.setFrameShape(QFrame.WinPanel)
        #bottom.setFrameShadow(QFrame.Sunken)

        #splitter = QSplitter(Qt.Vertical)
        #splitter = QSplitter(Qt.Horizontal)
        top_splitter = QSplitter(Qt.Horizontal)
        for sample_img in sample_img_frame_list:
            top_splitter.addWidget(sample_img)
        top_splitter.addWidget(refresh_btn)
        top_splitter.resize(self._width,20)
        
        img_button_splitter = QSplitter(Qt.Vertical)
        img_button_splitter.addWidget(fill_btn)
        img_button_splitter.addWidget(select_btn)
        img_button_splitter.resize(50,30)

        io_button_splitter = QSplitter(Qt.Vertical)
        io_button_splitter.addWidget(load_btn)
        io_button_splitter.addWidget(save_btn)
        io_button_splitter.resize(50,30)

        mid_splitter = QSplitter(Qt.Horizontal)
        mid_splitter.addWidget(midleft)
        mid_splitter.addWidget(midright)
        mid_splitter.addWidget(img_button_splitter)
        mid_splitter.resize(self._width,50)

        bottom_splitter = QSplitter(Qt.Horizontal)
        bottom_splitter.addWidget(bottom)
        bottom_splitter.addWidget(io_button_splitter)
        bottom_splitter.resize(self._width,50)      

        layout_splitter = QSplitter(Qt.Vertical)
        layout_splitter.addWidget(top_splitter)
        layout_splitter.addWidget(mid_splitter)
        layout_splitter.addWidget(bottom_splitter)
        
        plot_grid = QGridLayout()
        self.setLayout(plot_grid)
        plot_grid.addWidget(layout_splitter)

        '''
        # combobox - selected menu
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)
        
        # progressBar
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(80, 80, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(290, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        
        # push button
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        
        # check box 
        cb = QCheckBox('Show title', self)
        cb.move(80, 80)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        grid = QGridLayout()
        self.setLayout(grid)
        
        # Using Grid layout 
        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)
        '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())