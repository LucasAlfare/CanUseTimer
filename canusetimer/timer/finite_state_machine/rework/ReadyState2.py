from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import *


class ReadyState2(TimerState):
    def handle_input(self, input_type, data=None):
        if input_type is input_release:
            from canusetimer.timer.finite_state_machine.rework.SolveState2 import SolveState2
            return SolveState2()
        return None

    def update(self, event_manageable, data):
        print("[READY]")

    def suspend(self):
        pass
