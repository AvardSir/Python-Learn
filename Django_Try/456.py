import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QColor, QPalette

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Change Color")
        self.setGeometry(100, 100, 300, 200)

        self.button1 = QPushButton("Левый", self)
        self.button1.setGeometry(50, 50, 100, 50)
        self.button1.clicked.connect(self.change_color1)

        self.button2 = QPushButton("Правый", self)
        self.button2.setGeometry(150, 50, 100, 50)
        self.button2.clicked.connect(self.change_color2)
        #self.button2.clicked.connect(self.change_color3)


        self.default_palette = self.palette()

    def change_color1(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("red"))
        self.setPalette(palette)

    def change_color3(self):
        palette.setColor(QPalette.Window, QColor("purple"))

        palette = self.palette()
        self.setPalette(palette)
    def change_color2(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())