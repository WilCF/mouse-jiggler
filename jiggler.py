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
            "y": 5,
            "double_click_interval": 10
        }
        self.running = False
        self.timer = rumps.Timer(self.move_mouse, 5)
        self.double_click_timer = rumps.Timer(self.double_click, self.config["double_click_interval"])
        self.app = rumps.App(self.config["app_name"], "🖱")
        self.start_stop_button = rumps.MenuItem(title=self.config["start"], callback=self.toggle_jiggle)
        self.quit_button = rumps.MenuItem(title="Quit", callback=self.quit_app)  # Add a Quit button
        self.app.menu = [self.start_stop_button, self.quit_button]  # Add the Quit button to the menu

    def toggle_jiggle(self, sender):
        self.running = not self.running
        if self.running:
            self.timer.start()
            self.double_click_timer.start()
            sender.title = self.config["stop"]

        else:
            self.timer.stop()
            self.double_click_timer.stop()
            sender.title = self.config["start"]

    def move_mouse(self, sender):
        current = pyautogui.position()
        next = (current[0]+self.config["x"], current[1]+self.config["y"])
        pyautogui.moveTo(*next)
        time.sleep(self.config["interval"])
        pyautogui.moveTo(*current)

    def double_click(self, sender):
        pyautogui.doubleClick()

    def quit_app(self, sender):  # Add a quit_app method
        self.running = False
        self.timer.stop()
        self.double_click_timer.stop()
        rumps.quit_application()

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = JigglerApp()
    app.run()
