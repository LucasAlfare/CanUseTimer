from threading import Thread

from canusetimer.Misc import get_current_time
from canusetimer.timer.finite_state_machine.TimerFiniteStateMachine import *


class SolveState(TimerState):
    repeater = None
    repeating = False
    start = 0
    elapsed = 0

    def handle_input(self, input_type, data=None):
        if input_type is input_press:
            self.suspend()
            from canusetimer.timer.finite_state_machine.StopState import StopState
            return StopState(real_start_time=self.start)
        return None

    def update(self, event_manageable, data):
        print("[SOLVE]")

        def repeat():
            self.start = data
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
