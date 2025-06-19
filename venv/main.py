import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap


class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('Qlabel Example')
        self.displayLabels()
        self.show()

    def displayLabels(self):
        text = QLabel(self)
        text.setText("Hello")
        text.move(105,15)
        image="../images/world3.png"
        try:
            with open(image):
                world_image=QLabel(self)
                pixmap=QPixmap(image)
                world_image.setPixmap(pixmap)
                world_image.move(-30,40)
        except FileNotFoundError:
            print("Image not found.")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=HelloWorld()
    sys.exit(app.exec())
