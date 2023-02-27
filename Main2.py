from canusetimer.application_loop.ApplicationLoopManager import *
from canusetimer.keyboard.KeyboardManager import *
from canusetimer.timer.TimerManager import *

setup_managers([
    ApplicationLoopManager(),
    TimerManager(),
    KeyboardManager()
])
