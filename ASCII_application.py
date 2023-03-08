#!/usr/bin/python
import sys
from pathlib import Path
from PyQt6.QtWidgets import (QMainWindow, QFileDialog,
                             QApplication, QPushButton, QWidget, QGridLayout)
import ASCII_video


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        layout = QGridLayout()
        self.setWindowTitle("My App")

        self.path = ""

        button = self.set_button()
        layout.addWidget(button, 0, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_button(self):
        button = QPushButton("Выбор файла!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        return button

    def the_button_was_clicked(self):
        self.path = self.showDialog()
        video_converter = ASCII_video.VideoConverter(self.path)
        video_converter.run()

    def showDialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        return fname[0]


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
