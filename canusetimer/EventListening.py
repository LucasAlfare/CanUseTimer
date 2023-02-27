from enum import Enum


class AppEvent(Enum):
    """
    This class holds items to be used as non-value items, once
    they are important only to indicate stuff.
    """
    Timer_Toggle_Down, \
        Timer_Toggle_Up, \
        Timer_Ready, \
        Timer_Started, \
        Timer_Update, \
        Timer_Finished, \
        Timer_Finished_With_Penalty_Decision, \
        App_Menu_Entered, \
        App_Timer_Entered, \
        App_See_Solves_Entered, \
        App_Clear_Solves_Entered, \
        App_Mode_Exited, \
        App_Mode_Exit_Request, \
        Solves_Update, \
        Solves_Clear, \
        Penalty_Update, \
        Command_Request = range(17)


class EventManageable:
    """
    EventManageable is a class used to make entities either propagate events
    either receive events from others.

    To make this possible, all different instances of this must be subscribed
    to each other. For example, if some manager 'XXX' needs to listen events from
    another manager 'YYY' then 'YYY' must add 'XXX' as one of its listeners.

    In the other hand, if 'XXX' should send events for 'YYY', this means that
    'YYY' is a listener of 'XXX', then just need to be added to 'XXX' to receive
    its events notifications.
    """
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


# noinspection PyDefaultArgument
def setup_managers(managers=[]):
    """
    This auxiliary method automatically adds all managers from the parameter
    list to each other. Also, this method automatically calls all initialization
    code from all managers after subscription.

    TODO: make initialization calls asynchronous.
    """
    for m1 in managers:
        for m2 in managers:
            if m2 != m1:
                m1.add_listener(m2)

    for m in managers:
        m.initialize()
