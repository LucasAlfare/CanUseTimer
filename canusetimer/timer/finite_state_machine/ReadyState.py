from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import *


class ReadyState(TimerState):
    def handle_input(self, input_type, data=None):
        if input_type is input_release:
            from canusetimer.timer.finite_state_machine.SolveState import SolveState
            return SolveState()
        return None

    def update(self, event_manageable, data):
        pass

    def suspend(self):
        pass
