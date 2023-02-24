from EventListening import *
from finite_state_machine.ReadyState import ReadyState


class TimerManager(EventManageable):
    current_state = ReadyState()

    def initialize(self):
        self.initiated = True

    def on_event(self, event, data):
        if event is AppEvent.Timer_Toggle_Down or event is AppEvent.Timer_Toggle_Up:
            next_state = self.current_state.handle_input(input_type=event)
            if next_state is not None:
                self.current_state = next_state
                self.current_state.update(event_manageable=self, data=data)
