from canusetimer.EventListening import EventManageable, AppEvent
from canusetimer.Misc import clear_console, clear_and_println, absolute_time_to_timestamp


class ApplicationLoopManager(EventManageable):

    def initialize(self):
        self.do_menu_popup()

    def on_event(self, event, data):
        if event is AppEvent.Timer_Started:
            clear_console()
            pass

        if event is AppEvent.Timer_Ready or event is AppEvent.App_Timer_Entered:
            clear_console()
            print(
                """
                >>> You are in the timer! Use the space bar to toggle/control the start/stop.
                To quit/back to the menu, just hit "Esc" (this may cause console window lost focus).
                """.strip()
            )

        if event is AppEvent.Timer_Update:
            time = data
            clear_and_println(absolute_time_to_timestamp(time))

        if event is AppEvent.App_Mode_Exited:
            self.do_menu_popup()

        if event is AppEvent.App_See_Solves_Entered:
            solves = data
            clear_console()
            if len(solves) > 0:
                print('This is your solves:')
                index = 0
                for s in solves:
                    print("{}. {} {}\t{}".format(
                        index + 1,
                        absolute_time_to_timestamp(s.time),
                        s.penalty,
                        s.scramble)
                    )
                    index += 1
                print('\n')
                while True:
                    back_to_menu_answer = input('Back to menu? (y) ')
                    if back_to_menu_answer.__eq__('y'):
                        self.notify_listeners(AppEvent.App_Mode_Exit_Request, 2)
                        break
            else:
                while True:
                    back_to_menu_answer = input("You don't have solves yet. Back to menu? (y) ")
                    if back_to_menu_answer.__eq__('y'):
                        self.notify_listeners(AppEvent.App_Mode_Exit_Request, 2)
                        break

    def do_menu_popup(self):
        clear_console()
        print('Welcome to CanUseTimer!')
        print()
        menu_answer = input(
            """
            Enter a number:

            1: Start
            3: See times
            4: Clear all times
            """.strip()
        )
        self.notify_listeners(AppEvent.App_Menu_Entered, int(menu_answer) - 1)
