from managers.ApplicationLoopManager import *
from managers.ConsoleManager import *
from managers.TimerManager import *

setup_managers([
    ApplicationLoopManager(),
    TimerManager(),
    ConsoleManager()
])
