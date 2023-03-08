import unittest
import os
import pygame as pg
import numpy as np
import ASCII_application
import ASCII_video
from PyQt6.QtWidgets import (QApplication)
import sys


class TestSum(unittest.TestCase):

    def test_path(self):
        app = QApplication(sys.argv)
        window = ASCII_application.Window()
        result = os.path.abspath("bear.jpg").replace("\\", "/")
        print("chose bear.jpg in you directory")
        res = window.showDialog()
        self.assertEqual(res, result, "Should be " + result)

    def test_converter(self):
        path = os.path.abspath("bear.jpg").replace("\\", "/")
        video_converter = ASCII_video.VideoConverter(path)
        pg.display.set_mode((800, 600), flags=pg.HIDDEN)
        result = np.load('test.npy')
        a = video_converter.image
        self.assertEqual(a.all(), result.all(), "Wrong work of program")


if __name__ == '__main__':
    unittest.main()
