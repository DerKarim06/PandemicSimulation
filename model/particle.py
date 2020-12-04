from PyQt5 import QtGui
from PyQt5.QtGui import QPainterPath
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import Qt, QRectF


class Particle(QGraphicsItem):

    def __init__(self, x, y, parent=None):
        super().__init__(parent)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.xCord = x
        self.yCord = y

    def boundingRect(self):
        penWidth = 1.0
        return QRectF(self.xCord, self.xCord, 20 + penWidth, 20 + penWidth)

    def paint(self, painter, option, widget):
        painter.drawRect(self.xCord, self.yCord, 20, 20)

    def shape(self):
        path = QPainterPath()
        path.addRect(self.boundingRect())
        return path