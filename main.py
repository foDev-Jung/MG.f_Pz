import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QMainWindow, QGridLayout, QDesktopWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout,QGridLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QAction, qApp, QToolTip, QCheckBox, QComboBox, QProgressBar
from PyQt5.QtWidgets import QFrame, QSplitter

from PyQt5.QtGui import QIcon, QFont

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
      self.setFixedSize(640, 480)
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
   
        # tool tip
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
    
        # Splitter
        top = QFrame()
        top.setFrameShape(QFrame.Box)

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        
        plot_grid = QGridLayout()
        self.setLayout(plot_grid)
        plot_grid.addWidget(splitter2)
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