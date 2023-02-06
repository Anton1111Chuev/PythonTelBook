import sys
from PyQt6.QtWidgets import QApplication
from telBook.views import MainWindow
from views_bot import init_bot

class Control():
    def __init__(self, type_of_view):
        if type_of_view == 1:
            self.app = QApplication(sys.argv)
            self.window = MainWindow()
            self.window.show()
            self.__start_app()
        elif type_of_view == 2:
            init_bot()
        else:
            print("Не известный тип view проверьте настройку параметра type_of_view")

    def __start_app(self):
        self.app.exec()