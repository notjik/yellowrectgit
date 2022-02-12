import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw_bol)
        self.show()

    def draw_bol(self):
        self.flag = True
        if self.flag:
            self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        if self.flag:
            x, y, len_ = randint(0, self.width() - 1), randint(0, self.height() - 1), randint(0, self.width() // 2)
            qp.setBrush(QColor('yellow'))
            qp.drawEllipse(x, y, len_, len_)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
