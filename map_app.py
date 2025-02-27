import sys

import requests
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('map.ui', self)
        self.scale = 0.005
        self.cords_x = 37.299989
        self.cords_y = 55.481457
        img = self.get_map_image()
        self.map.setPixmap(img)
        self.scale = 0.005

    def get_map_image(self, **params):
        map_params = {
            "ll": params.get("ll", f'{self.cords_y},{self.cords_x}'),
            "spn": params.get("spn", f"{self.scale},{self.scale}"),
            "apikey": "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
        }
        map_api_server = "https://static-maps.yandex.ru/v1"
        response = requests.get(map_api_server, params=map_params)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        return pixmap

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_PageUp:
            self.scale *= 2
            self.map.setPixmap(self.get_map_image())
        elif event.key() == Qt.Key.Key_PageDown:
            self.scale /= 2
            self.map.setPixmap(self.get_map_image())
        elif event.key() == Qt.Key.Key_Up:
            self.cords_x += 0.001
            self.map.setPixmap(self.get_map_image())
        elif event.key() == Qt.Key.Key_Down:
            self.cords_x -= 0.001
            self.map.setPixmap(self.get_map_image())
        elif event.key() == Qt.Key.Key_Right:
            self.cords_y += 0.001
            self.map.setPixmap(self.get_map_image())
        elif event.key() == Qt.Key.Key_Left:
            self.cords_y -= 0.001
            self.map.setPixmap(self.get_map_image())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
