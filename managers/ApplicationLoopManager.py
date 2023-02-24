from EventListening import EventManageable, AppEvent
from Misc import clear_console


class ApplicationLoopManager(EventManageable):
    def initialize(self):
        self.do_menu_popup()

    def on_event(self, event, data):
        if event is AppEvent.AppModeExited:
            self.do_menu_popup()

        if event is AppEvent.AppTimerEntered:
            print(
                """
                >>> You are in the timer! Use the space bar to toggle/control start/stop.
                To quit/back to the menu, just hit "Esc"
                """.strip().lstrip()
            )

    def do_menu_popup(self):
        clear_console()
        print('Welcome to CanUseTimer!')
        print()
        menu_answer = input(
            """
            Enter a number:

            1: Start
            2: Delete a solution...
            3: See times
            4: Clear all times
            5: Settings
            6: Credits
            7: Quit CanUseTimer...
            """.strip().lstrip()
        )
        self.notify_listeners(AppEvent.AppMenuEntered, int(menu_answer) - 1)
