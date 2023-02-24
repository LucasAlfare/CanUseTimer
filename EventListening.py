from enum import Enum


class AppEvent(Enum):
    """
    This class holds items to be used as non-value items, once
    then are important only to indicate stuff.
    """
    Timer_Toggle_Down,\
        Timer_Toggle_Up,\
        Timer_Ready, \
        Timer_Started, \
        Timer_Update, \
        Timer_Finished,\
        AppMenuEntered, \
        AppTimerEntered, \
        AppModeExited = range(9)


class EventManageable:
    listeners = []
    initiated = False

    def initialize(self):
        raise NotImplementedError("Please Implement this method")

    def on_event(self, event, data):
        raise NotImplementedError("Please Implement this method")

    def add_listener(self, li):
        if not self.listeners.__contains__(li):
            self.listeners.append(li)

    def notify_listeners(self, event, data=None):
        for listener in self.listeners:
            listener.on_event(event, data)


def setup_managers(managers):
    for m1 in managers:
        for m2 in managers:
            if m2 != m1:
                m1.add_listener(m2)

    for m in managers:
        m.initialize()
