import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QImage, QPixmap


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "くそみたいなGUI"
        self.width = 1280
        self.height = 720
        self.counter = 0
        self.initUI()

    def initUI(self):
        self.main_layout = QGridLayout()

        self.create_how_to_image()
        self.create_sliders()
        self.create_flipper_image()

        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        self.setLayout(self.main_layout)
        self._run()

    def create_flipper_image(self):
        image_layout = QHBoxLayout()
        image = QImage("flipper.png")
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap.fromImage(image))
        imageLabel.scaleFactor = 1.0
        image_layout.addWidget(imageLabel)
        self.main_layout.addLayout(image_layout, 0, 0)

    def create_how_to_image(self):
        image_layout = QHBoxLayout()
        image = QImage("how_to_contorol_.png")
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap.fromImage(image))
        imageLabel.scaleFactor = 1.0
        image_layout.addWidget(imageLabel)
        self.main_layout.addLayout(image_layout, 0, 1)

    def create_sliders(self):
        self.sliders_layout = QHBoxLayout()
        self.slider_FL = QSlider(Qt.Vertical, self)
        self.slider_FL.setMinimum(-180)
        self.slider_FL.setMaximum(180)
        self.sliders_layout.addWidget(self.slider_FL)
        self.slider_FR = QSlider(Qt.Vertical, self)
        self.slider_FR.setMinimum(-180)
        self.slider_FR.setMaximum(180)
        self.sliders_layout.addWidget(self.slider_FR)
        self.slider_BL = QSlider(Qt.Vertical, self)
        self.slider_BL.setMinimum(-180)
        self.slider_BL.setMaximum(180)
        self.sliders_layout.addWidget(self.slider_BL)
        self.slider_BR = QSlider(Qt.Vertical, self)
        self.slider_BR.setMinimum(-180)
        self.slider_BR.setMaximum(180)
        self.sliders_layout.addWidget(self.slider_BR)

        self.main_layout.addLayout(self.sliders_layout, 1, 0)

    def _run(self):
        if self.counter == 360:
            self.counter = 0
        else:
            self.counter += 1
        self.slider_FR.setValue(self.counter - 180)
        QTimer.singleShot(100, self._run)


def main():
    app = QApplication(sys.argv)
    gui = MyWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
