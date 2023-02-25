from canusetimer.EventListening import AppEvent
from canusetimer.console_dialog.Definitions import Dialog


class Menu(Dialog):

    def __init__(self):
        super().__init__()

    def on_valid(self):
        self.event_manageable.notify_listeners(
            event=AppEvent.App_Menu_Entered,
            data=int(self.actual_answer) - 1
        )

    def on_invalid(self):
        pass

