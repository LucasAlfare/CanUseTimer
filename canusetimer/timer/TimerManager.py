from canusetimer.EventListening import *
# from canusetimer.timer.finite_state_machine.ReadyState import ReadyState
from canusetimer.timer.finite_state_machine.rework.ReadyState2 import ReadyState2


class TimerManager(EventManageable):
    current_state = ReadyState2()

    def initialize(self):
        self.initiated = True

    def on_event(self, event, data):
        if event is AppEvent.Timer_Toggle_Down or \
                event is AppEvent.Timer_Toggle_Up or \
                event is AppEvent.Penalty_Update:
            next_state = self.current_state.handle_input(input_type=event)
            if next_state is not None:
                current_toggle_time = data
                self.current_state = next_state
                self.current_state.update(event_manageable=self, data=current_toggle_time)
