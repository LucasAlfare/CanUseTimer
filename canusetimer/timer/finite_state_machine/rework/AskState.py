from canusetimer.EventListening import AppEvent
from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import TimerState


class AskState(TimerState):
    def handle_input(self, input_type, data=None):
        if input_type is AppEvent.Penalty_Update:
            from canusetimer.timer.finite_state_machine.rework.ReadyState2 import ReadyState2
            return ReadyState2()
        return None

    def update(self, event_manageable, data):
        answer = input("[ASKING]")
        print("answer=[{}]".format(answer))
        event_manageable.notify_listeners(AppEvent.Penalty_Update)

    def suspend(self):
        pass
