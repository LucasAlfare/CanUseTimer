from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import *


class SolveState2(TimerState):
    def handle_input(self, input_type, data=None):
        if input_type is input_press:
            from canusetimer.timer.finite_state_machine.rework.StopState import StopState
            return StopState()
        return None

    def update(self, event_manageable, data):
        print("[SOLVE]")

    def suspend(self):
        pass
