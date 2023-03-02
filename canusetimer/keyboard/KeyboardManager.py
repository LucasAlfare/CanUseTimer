from pynput import keyboard
from pynput.keyboard import Key
from canusetimer.EventListening import *
from canusetimer.Misc import get_current_time


class KeyboardManager(EventManageable):

    keyboard_listener = None

    def initialize(self):
        pass

    def on_event(self, event, data):
        if event is AppEvent.App_Menu_Entered:
            answer = data
            # this manager only cares about answer 0
            if answer == 0:
                if not self.initiated:
                    self.notify_listeners(AppEvent.App_Timer_Entered)
                    self.setup_keyboard_listening()

    def setup_keyboard_listening(self):
        # initializes the target functions to the pynput library
        def my_on_press(key):
            if key == Key.space:
                self.notify_listeners(event=AppEvent.Timer_Toggle_Down, data=get_current_time())

        def my_on_release(key):
            if key == Key.space:
                self.notify_listeners(event=AppEvent.Timer_Toggle_Up, data=get_current_time())
            elif key == Key.esc:
                self.keyboard_listener.stop()
                self.keyboard_listener = None
                self.initiated = False
                self.notify_listeners(AppEvent.App_Mode_Exited)

        self.initiated = True

        self.keyboard_listener = keyboard.Listener(
            on_press=my_on_press, on_release=my_on_release
        )
        self.keyboard_listener.start()
        self.keyboard_listener.join()
