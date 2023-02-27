from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import *


class StopState(TimerState):
    def handle_input(self, input_type, data=None):
        if input_type is input_release:
            from canusetimer.timer.finite_state_machine.rework.AskState import AskState
            return AskState()
        return None

    def update(self, event_manageable, data):
        print("[STOP]")

    def suspend(self):
        pass
