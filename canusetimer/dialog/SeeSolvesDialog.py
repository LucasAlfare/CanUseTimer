from canusetimer.EventListening import AppEvent
from canusetimer.dialog.Definitions import Dialog


class SeeSolves(Dialog):

    def __init__(self):
        super().__init__()

    def on_valid(self):
        self.event_manageable.notify_listeners(AppEvent.App_Mode_Exit_Request, 2)

    def on_invalid(self):
        pass
