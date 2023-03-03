from canusetimer.application_loop.ApplicationLoopManager import *
from canusetimer.data.DataManager import DataManager
from canusetimer.keyboard.KeyboardManager import *
from canusetimer.scramble.ScrambleManager import ScrambleManager
from canusetimer.timer.TimerManager import *

setup_managers([
    ScrambleManager(),
    TimerManager(),
    DataManager(),
    ApplicationLoopManager(),
    KeyboardManager()
])
