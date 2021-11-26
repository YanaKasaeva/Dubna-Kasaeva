import sys
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Ex(QMainWindow):
    def __init__(self):
        super(Ex, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Задача 2')
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 190, 0))
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        qp = QPainter()
        qp.begin(self)

    def draw_circle(self, qp):
        r = randint(5, 100)
        coords = randint(100, 500), randint(100, 500)
        qp.drawEllipse(coords[0] - r, coords[1] - r, 2 * r, 2 * r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
