import sys

import requests
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('map.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner
        img = self.get_map_image()
        self.map.setPixmap(img)

    def get_map_image(self, **params):
        map_params = {
            "ll": params.get("ll", "37.300611,55.483988"),
            "spn": params.get("spn", "0.005,0.005"),
            "apikey": "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
        }
        map_api_server = "https://static-maps.yandex.ru/v1"
        response = requests.get(map_api_server, params=map_params)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        return pixmap


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
