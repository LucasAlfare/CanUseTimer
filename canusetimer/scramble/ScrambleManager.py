import random

from canusetimer.EventListening import EventManageable, AppEvent


class ScrambleManager(EventManageable):
    last_scramble = ''
    current_scramble = ''

    def initialize(self):
        self.generate_scramble()
        self.notify_scramble()
        self.initiated = True

    def on_event(self, event, data):
        if event is AppEvent.Request_Scramble_Generated:
            self.notify_scramble()

        if event is AppEvent.Timer_Finished:
            self.generate_scramble()

        if event is AppEvent.Timer_Ready:
            self.notify_scramble()

    def generate_scramble(self):
        self.last_scramble = self.current_scramble
        self.current_scramble = "Scramble KKKKK {}".format(random.randint(0, 99999))

    def notify_scramble(self):
        self.notify_listeners(
            event=AppEvent.Scramble_Generated,
            data=[
                self.last_scramble,  # 0
                self.current_scramble  # 1
            ]
        )
