from canusetimer.EventListening import AppEvent
from canusetimer.data.Definitions import Penalty
from canusetimer.dialog.Definitions import Dialog


class AskPenaltyDialog(Dialog):

    def __init__(self):
        super().__init__()

    def on_valid(self):
        if self.actual_answer.__eq__('1'):
            self.event_manageable.notify_listeners(event=AppEvent.Penalty_Update, data=Penalty.Dnf)
        elif self.actual_answer.__eq__('2'):
            self.event_manageable.notify_listeners(event=AppEvent.Penalty_Update, data=Penalty.Plus_Two)
        self.event_manageable.notify_listeners(event=AppEvent.Timer_Finished)

    def on_invalid(self):
        pass
