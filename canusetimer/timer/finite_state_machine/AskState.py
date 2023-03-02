from canusetimer.EventListening import AppEvent
from canusetimer.Misc import absolute_time_to_timestamp
from canusetimer.dialog.Answers import Ask_Penalty_Answers
from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import TimerState
from canusetimer.dialog.AskPenaltyDialog import AskPenaltyDialog


class AskState(TimerState):
    elapsed_time = 0

    def __init__(self, real_elapsed_time=0):
        self.elapsed_time = real_elapsed_time
        pass

    def handle_input(self, input_type, data=None):
        if input_type is AppEvent.Timer_Finished:
            from canusetimer.timer.finite_state_machine.ReadyState import ReadyState
            return ReadyState()
        return None

    def update(self, event_manageable, data):

        ask_text = """
            Your time: {}
            Set penalty to DNF (1) or +2 (2)?
            Enter (y) to continue.
            """.format(absolute_time_to_timestamp(self.elapsed_time)).strip()

        ask_dialog = AskPenaltyDialog()
        ask_dialog.message = ask_text
        ask_dialog.expected_answers = Ask_Penalty_Answers
        ask_dialog.event_manageable = event_manageable
        ask_dialog.start()

    def suspend(self):
        pass
