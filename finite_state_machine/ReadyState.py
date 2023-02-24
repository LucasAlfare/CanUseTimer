from finite_state_machine.TimerFiniteStateMachine import *
from EventListening import *


class ReadyState(TimerState):

    def handle_input(self, input_type, data=None):
        if input_type is input_release:
            from finite_state_machine.SolveState import SolveState
            return SolveState()
        return None

    def update(self, event_manageable, data):
        event_manageable.notify_listeners(event=AppEvent.Timer_Ready)

    def suspend(self):
        pass
