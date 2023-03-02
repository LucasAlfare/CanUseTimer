from canusetimer.EventListening import AppEvent
from canusetimer.Misc import clear_console
from canusetimer.dialog.Definitions import Dialog


class ClearSolves(Dialog):

    def __init__(self):
        super().__init__()

    def on_valid(self):
        clear_console()
        # TODO: should be created a custom [dialog] only for this..?
        if self.actual_answer.__eq__('y'):
            self.event_manageable.notify_listeners(AppEvent.Solves_Clear)
            print("All your solves was deleted.")
        input("""Hit "Enter" to back to menu...""")
        self.event_manageable.notify_listeners(AppEvent.App_Mode_Exit_Request, 3)

    def on_invalid(self):
        pass
