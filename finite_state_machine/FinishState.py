from finite_state_machine.TimerFiniteStateMachine import *


class FinishState(TimerState):
    def handle_input(self, input_type, data=None):
        if input_type is input_release:
            from finite_state_machine.ReadyState import ReadyState
            return ReadyState()
        return None

    def update(self, event_manageable, data):
        event_manageable.notify_listeners(event=AppEvent.Timer_Finished, data=40000)

    def suspend(self):
        pass
