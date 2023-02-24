from pynput import keyboard
from pynput.keyboard import Key
from EventListening import *
from Misc import cleared_print, absolute_time_to_timestamp


class ConsoleManager(EventManageable):

    keyboard_listener = None

    def initialize(self):
        pass

    def on_event(self, event, data):
        if event is AppEvent.Timer_Update:
            time = data
            cleared_print(absolute_time_to_timestamp(time))

        if event is AppEvent.AppMenuEntered:
            answer = data
            # this manager only cares about answer 0
            if answer == 0:
                if not self.initiated:
                    self.notify_listeners(AppEvent.AppTimerEntered)
                    self.setup_keyboard_listening()

    def setup_keyboard_listening(self):
        # initializes the target functions to the pynput library
        def on_press(key):
            if key == Key.space:
                self.notify_listeners(AppEvent.Timer_Toggle_Down)

        def on_release(key):
            if key == Key.space:
                self.notify_listeners(AppEvent.Timer_Toggle_Up)
            elif key == Key.esc:
                self.keyboard_listener.stop()
                self.keyboard_listener = None
                self.initiated = False
                self.notify_listeners(AppEvent.AppModeExited)

        self.initiated = True

        self.keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        self.keyboard_listener.start()
        self.keyboard_listener.join()
