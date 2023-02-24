from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import *


class FinishState(TimerState):

    def __init__(self, real_start_time=0):
        self.real_start_time = real_start_time
        pass

    def handle_input(self, input_type, data=None):
        if input_type is input_release:
            from canusetimer.timer.finite_state_machine.ReadyState import ReadyState
            return ReadyState()
        return None

    def update(self, event_manageable, data):
        real_elapsed_time = data - self.real_start_time
        event_manageable.notify_listeners(event=AppEvent.Timer_Finished, data=real_elapsed_time)

    def suspend(self):
        pass
