from threading import Thread

from finite_state_machine.TimerFiniteStateMachine import *
from Misc import *


class SolveState(TimerState):
    repeater = None
    repeating = False
    start = 0
    elapsed = 0

    def handle_input(self, input_type, data=None):
        if input_type is input_press:
            self.suspend()
            from finite_state_machine.FinishState import FinishState
            return FinishState()
        return None

    def update(self, event_manageable, data):

        def repeat():
            self.start = get_current_time()
            while self.repeating:
                self.elapsed = get_current_time() - self.start
                event_manageable.notify_listeners(
                    event=AppEvent.Timer_Update,
                    data=self.elapsed
                )
                import time as t
                t.sleep(1 / 1000)

        event_manageable.notify_listeners(event=AppEvent.Timer_Started)
        self.repeater = Thread(target=repeat)
        self.repeating = True
        self.repeater.start()

    def suspend(self):
        # cancel/finish/stop/destroy current active thread created by the update function
        self.repeating = False
        self.repeater = None
