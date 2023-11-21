import io
import sys
import circles
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets


class MyPillow(QWidget, circles.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(5, 200)
        qp.drawEllipse(QPoint(350, 200), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyPillow()
    w.show()
    sys.exit(app.exec())
