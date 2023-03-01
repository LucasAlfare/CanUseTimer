from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import *


class StopState(TimerState):

    start_time = 0
    elapsed_time = 0

    def __init__(self, real_start_time=0):
        self.start_time = real_start_time
        pass

    def handle_input(self, input_type, data=None):
        if input_type is input_release:
            from canusetimer.timer.finite_state_machine.AskState import AskState
            return AskState(real_elapsed_time=self.elapsed_time)
        return None

    def update(self, event_manageable, data):
        self.elapsed_time = data - self.start_time
        event_manageable.notify_listeners(event=AppEvent.Timer_Stopped, data=self.elapsed_time)

    def suspend(self):
        pass
