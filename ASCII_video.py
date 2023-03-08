import pygame as pg
import cv2
import time


class VideoConverter:
    def __init__(self, path, size=12):
        pg.init()
        self.path = path
        self.capture = cv2.VideoCapture(path)
        self.image = self.get_data()
        self.width = self.image.shape[0]
        self.height = self.image.shape[1]
        self.size = self.width, self.height
        self.display = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        self.chars = ' .",:;!~+-xmo*#W&8@'
        self.k = 255 // (len(self.chars) - 1)
        self.font = pg.font.SysFont('Courier', size, bold=True)
        self.delta = int(size * 0.6)
        self.result_render = [self.font.render(char, False, 'white')
                              for char in self.chars]

    def get_data(self):
        ret, self.cv2_image = self.capture.read()
        if not ret:
            exit()
        # ret, cv2_image = self.capture.read()
        # if ret:
        #     self.cv2_image = cv2_image
        # else:
        #     self.total_time = time.process_time() - self.start_time
        transposed_image = cv2.transpose(self.cv2_image)
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def draw_converted_image(self):
        self.image = self.get_data()
        data = self.image // self.k
        for x in range(0, self.width, self.delta):
            for y in range(0, self.height, self.delta):
                char = data[x, y]
                if char:
                    self.display.blit(self.result_render[char], (x, y))

    def draw(self):
        self.display.fill('black')
        self.draw_converted_image()

    def run(self):
        end = False
        while True:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()
            self.draw()
            time.sleep(0.02)
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()
