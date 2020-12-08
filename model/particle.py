from PyQt5 import QtGui
from PyQt5.QtGui import QPainterPath, QColor, QPen, QBrush
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import Qt, QRectF
from matplotlib.patches import Shadow


class Particle(QGraphicsItem):
    def __init__(self, x, y):
        super(Particle, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.rectF = QRectF(x, y, 10, 10)
        self.x = x
        self.y = y
        self._brush = QBrush(Qt.green)

    def setBrush(self, brush):
        self._brush = brush
        self.update()

    def boundingRect(self):
        return self.rectF

    def paint(self, painter=None, style=None, widget=None):
        painter.fillRect(self.rectF, self._brush)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setXa(self, x):
        self.rectF = QRectF(x, self.y, 10, 10)
        self.x = x
        self.update()

    def setYa(self, y):
        self.rectF = QRectF(self.x, y, 10, 10)
        self.y = y
        self.update