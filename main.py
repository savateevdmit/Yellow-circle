import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from pyqt5_plugins.examplebuttonplugin import QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.setMouseTracking(True)
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.do_paint = True
        self.figure = 'circle'
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        if self.do_paint and self.figure == 'circle':
            qp = QPainter()
            qp.begin(self)
            size = random.randint(10, self.width() // 4)
            qp.setBrush(QColor(255, 230, 0))
            qp.drawEllipse(440 - size // 2, 300 - size // 2, size, size)
            qp.end()
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
