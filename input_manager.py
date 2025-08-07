from pynput import mouse, keyboard
from time import sleep

mctl = mouse.Controller()
kctl = keyboard.Controller()

STANDARD_INPUT_SLEEP = 0.05


class inputManager():
    mctl = mouse.Controller()
    kctl = keyboard.Controller()

    def lclick(self, x, y):
        mctl.position = (x, y)
        mctl.click(mouse.Button.left)
        sleep(STANDARD_INPUT_SLEEP)

    def rclick(self, x, y):
        mctl.position = (x, y)
        mctl.click(mouse.Button.right)
        sleep(STANDARD_INPUT_SLEEP)

    def ldrag(self, x1, y1, x2, y2):
        mctl.position = (x1, y1)
        mctl.press(mouse.Button.left)
        sleep(STANDARD_INPUT_SLEEP)
        mctl.position = (x2, y2)
        sleep(STANDARD_INPUT_SLEEP)
        mctl.release(mouse.Button.left)
        sleep(STANDARD_INPUT_SLEEP)

    def scroll(self, x, y, dy):
        mctl.position = (x, y)
        mctl.scroll(0, dy)
        sleep(STANDARD_INPUT_SLEEP + 0.2)

    def walk(self, time, key: str | keyboard.Key | keyboard.KeyCode):
        kctl.press(key)
        sleep(time)
        kctl.release(key)
        sleep(0.1)


input = inputManager()


class CameraManager:
    def __init__(self, zoom=4, yaw=0, roll=0):
        self.zoom = zoom
        self.yaw = yaw
        self.roll = roll

    def __str__(self):
        return f"({self.zoom}, ({self.yaw}, {self.roll}))"

    def set_zoom(self, new_zoom):
        assert new_zoom >= 1
        assert new_zoom <= 25

        while (new_zoom > self.zoom):
            kctl.tap('o')
            self.zoom += 1
            sleep(STANDARD_INPUT_SLEEP)
        while (new_zoom < self.zoom):
            kctl.tap('i')
            self.zoom -= 1
            sleep(STANDARD_INPUT_SLEEP)

    def set_yaw(self, new_yaw):
        diff = (new_yaw - self.yaw) % 8

        if (diff > 0) and (diff <= 4):
            for _ in range(0, diff):
                kctl.tap('.')
                self.yaw = (self.yaw + 1) % 8
                sleep(STANDARD_INPUT_SLEEP)
        elif (diff > 4):
            for _ in range(0, 8 - diff):
                kctl.tap(',')
                self.yaw = (self.yaw - 1) % 8
                sleep(STANDARD_INPUT_SLEEP)

    def set_roll(self, new_roll):
        assert new_roll <= 4
        assert new_roll >= -6

        while (new_roll > self.roll):
            kctl.tap(keyboard.Key.page_up)
            self.roll += 1
            sleep(STANDARD_INPUT_SLEEP)
        while (new_roll < self.roll):
            kctl.tap(keyboard.Key.page_down)
            self.roll -= 1
            sleep(STANDARD_INPUT_SLEEP)

    def set_all(self, zoom=None, yaw=None, roll=None):
        if not type(zoom) == 'NoneType':
            self.set_zoom(zoom)
        if not type(yaw) == 'NoneType':
            self.set_yaw(yaw)
        if not type(roll) == 'NoneType':
            self.set_roll(roll)

    def resync(self, keep_old=False):
        correct_zoom = self.zoom
        self.zoom = 1
        correct_yaw = self.yaw
        self.yaw = 0
        correct_roll = self.roll
        self.roll = 0

        kctl.tap(keyboard.Key.esc)
        sleep(STANDARD_INPUT_SLEEP)
        kctl.tap('r')
        sleep(STANDARD_INPUT_SLEEP)
        kctl.tap(keyboard.Key.enter)
        sleep(STANDARD_INPUT_SLEEP)
        for _ in range(0, 26):
            kctl.tap('i')
            sleep(STANDARD_INPUT_SLEEP)
        kctl.tap('o')
        sleep(STANDARD_INPUT_SLEEP)

        if keep_old:
            self.set_all(correct_zoom, correct_yaw, correct_roll)


camera = CameraManager()
