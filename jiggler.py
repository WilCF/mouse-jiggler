#!/Users/a683040/Projects/jiggler/.venv/bin/python3
import pyautogui
import rumps
import time

class JigglerApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Jiggler",
            "start": "Start Jiggling",
            "stop": "Stop Jiggling",
            "interval": 5,
            "x": 5,
            "y": 5
        }
        self.running = False
        self.timer = rumps.Timer(self.move_mouse, 5)
        self.app = rumps.App(self.config["app_name"], "🖱")
        self.start_stop_button = rumps.MenuItem(title=self.config["start"], callback=self.toggle_jiggle)
        self.app.menu = [self.start_stop_button]

    def toggle_jiggle(self, sender):
        self.running = not self.running
        if self.running:
            self.timer.start()
            sender.title = self.config["stop"]

        else:
            self.timer.stop()
            sender.title = self.config["start"]

    def move_mouse(self, sender):
        current = pyautogui.position()
        next = (current[0]+self.config["x"], current[1]+self.config["y"])
        pyautogui.moveTo(*next)
        time.sleep(self.config["interval"])
        pyautogui.moveTo(*current)

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = JigglerApp()
    app.run()