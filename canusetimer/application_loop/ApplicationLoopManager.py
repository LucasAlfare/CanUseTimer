import random
import time
from threading import Thread

from canusetimer.EventListening import EventManageable
from canusetimer.Misc import clear_and_println


class ApplicationLoopManager(EventManageable):

    looper = None

    def initialize(self):
        def looper_target():
            self.initiated = True
            while True:
                # TODO: abstract items to components and update then here
                time.sleep(1 / 1000)

        self.looper = Thread(target=looper_target)
        self.looper.start()

    def on_event(self, event, data):
        pass
