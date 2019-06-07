from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QApplication
from PyQt5.QtGui import QPixmap
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Pokemon'
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        text = QLabel('请输入需查询神奇宝贝图片的名称')
        self.textEdit = QLineEdit(self)
        self.button = QPushButton('识别', self)
        author = QLabel('Author')
        publishdate = QLabel('PublishDate')
        usedtimes = QLabel('UsedTimes')
        self.authorEdit = QLineEdit()
        self.publishdateEdit = QLineEdit()
        self.usedtimesEdit = QLineEdit()
        mainlayout = QHBoxLayout()
        vlayout1 = QVBoxLayout()
        vlayout2 = QVBoxLayout()
        self.label = QLabel(self)
        vlayout1.addWidget(text)
        vlayout1.addWidget(self.textEdit)
        vlayout1.addWidget(self.button)
        vlayout1.addWidget(self.label)
        vlayout2.addWidget(author)
        vlayout2.addWidget(self.authorEdit)
        vlayout2.addWidget(publishdate)
        vlayout2.addWidget(self.publishdateEdit)
        vlayout2.addWidget(usedtimes)
        vlayout2.addWidget(self.usedtimesEdit)
        v1 = QWidget(); v2 = QWidget()
        v1.setLayout(vlayout1)
        v2.setLayout(vlayout2)
        mainlayout.addWidget(v1)
        mainlayout.addWidget(v2)
        self.setLayout(mainlayout)
        self.button.clicked.connect(self.getTitle)
        self.show()
    def getTitle(self):
        name = self.textEdit.text()
        img = QPixmap(name).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(img)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exit(app.exec_())
