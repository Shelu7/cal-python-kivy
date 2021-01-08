from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import math


class MainWindow(Screen):

    num_input = ObjectProperty(None)
    md = ObjectProperty(None)
    cl = ObjectProperty(None)
    bs = ObjectProperty(None)
    svn = ObjectProperty(None)
    egt = ObjectProperty(None)
    nne = ObjectProperty(None)
    mulpy = ObjectProperty(None)
    fr = ObjectProperty(None)
    fve = ObjectProperty(None)
    sx = ObjectProperty(None)
    plus = ObjectProperty(None)
    one = ObjectProperty(None)
    two = ObjectProperty(None)
    three = ObjectProperty(None)
    mns = ObjectProperty(None)
    zr = ObjectProperty(None)
    dt = ObjectProperty(None)
    eql = ObjectProperty(None)
    dvsn = ObjectProperty(None)
    num1 = ObjectProperty(None)
    num2 = ObjectProperty(None)
    op = ObjectProperty(None)
    tot = ObjectProperty(None)

    def add(self, plus):
        self.num1 = self.num_input.text
        self.num1 = float(self.num1)
        self.op = "+"
        self.reset()

    def multiply(self, mulply):
        self.num1 = self.num_input.text
        self.num1 = float(self.num1)
        self.op = "*"
        self.reset()

    def minus(self, mns):
        self.num1 = self.num_input.text
        self.num1 = float(self.num1)
        self.op = "-"
        self.reset()

    def division(self, dvsn):
        self.num1 = self.num_input.text
        self.num1 = float(self.num1)
        self.op = "/"
        self.reset()

    def mod(self, md):
        self.num1 = self.num_input.text
        self.num1 = float(self.num1)
        self.op = "%"
        self.reset()

    def equal(self, eql):
        self.num2 = self.num_input.text
        self.num2 = float(self.num2)
        if self.op == "+":
            self.tot = self.num1 + self.num2
            self.num_input.text = str(self.tot)
        elif self.op == "-":
            self.tot = self.num1 - self.num2
            self.num_input.text = str(self.tot)
        elif self.op == "*":
            self.tot = self.num1 * self.num2
            self.num_input.text = str(self.tot)
        elif self.op == "/":
            self.tot = self.num1 / self.num2
            self.num_input.text = str(self.tot)
        elif self.op == "%":
            self.tot = self.num1 % self.num2
            self.num_input.text = str(self.tot)

    def reset(self):
        self.num_input.text = ""

    def onee(self, one):
        self.num_input.text += "1"

    def tw(self, two):
        self.num_input.text += "2"

    def thr(self):
        self.num_input.text += "3"

    def four(self):
        self.num_input.text += "4"

    def five(self):
        self.num_input.text += "5"

    def six(self):
        self.num_input.text += "6"

    def seven(self):
        self.num_input.text += "7"

    def eight(self):
        self.num_input.text += "8"

    def nine(self):
        self.num_input.text += "9"

    def zero(self):
        self.num_input.text += "0"

    def dot(self):
        self.num_input.text += "."

    def backspace(self):
        while True:
            try:
                self.num_input.text = (str(self.num_input.text)[0:1])
                if str(self.num_input.text)[-1] == " ":
                    continue
                else:
                    break
            except IndexError:
                break


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")
sm = WindowManager()


class MyApp(App):
    def build(self):
        return sm


screens = [MainWindow(name="main")]

for screen in screens:
    sm.add_widget(screen)


if __name__ == "__main__":
    MyApp().run()
