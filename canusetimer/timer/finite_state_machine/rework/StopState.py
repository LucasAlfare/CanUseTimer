from canusetimer.Misc import clear_console, absolute_time_to_timestamp
from canusetimer.data.Definitions import Penalty
from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import *


class StopState(TimerState):

    real_start_time = 0

    def __init__(self, real_start_time=0):
        self.real_start_time = real_start_time
        pass

    def handle_input(self, input_type, data=None):
        if input_type is input_release:
            from canusetimer.timer.finite_state_machine.rework.AskState import AskState
            return AskState()
        return None

    def update(self, event_manageable, data):
        print("[STOP]")
        real_elapsed_time = data - self.real_start_time

        # TODO: refactor this decision block to an appropriated scope
        clear_console()
        time_penalty_decision_answer = input(
            """
            Your time: {}
            Set penalty to DNF (1) or +2 (2)?
            Leave blank (hit "Enter") to continue.
            """.format(absolute_time_to_timestamp(real_elapsed_time)).strip()
        ).strip()

        if time_penalty_decision_answer.__eq__('1'):
            event_manageable.notify_listeners(event=AppEvent.Penalty_Update, data=Penalty.Dnf)
        elif time_penalty_decision_answer.__eq__('2'):
            event_manageable.notify_listeners(event=AppEvent.Penalty_Update, data=Penalty.Plus_Two)

        event_manageable.notify_listeners(event=AppEvent.Timer_Finished, data=real_elapsed_time)

    def suspend(self):
        pass
