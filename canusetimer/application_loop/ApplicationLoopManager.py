from canusetimer.EventListening import EventManageable, AppEvent
from canusetimer.Misc import clear_console, cleared_print, absolute_time_to_timestamp
from canusetimer.data.Definitions import Penalty


class ApplicationLoopManager(EventManageable):

    def initialize(self):
        self.do_menu_popup()

    def on_event(self, event, data):
        if event is AppEvent.Timer_Started:
            clear_console()

        if event is AppEvent.Timer_Ready:
            clear_console()
            print(
                """
                >>> You are in the timer! Use the space bar to toggle/control start/stop.
                To quit/back to the menu, just hit "Esc" (this may cause console window lost focus).
                """.strip().lstrip()
            )

        if event is AppEvent.Timer_Update:
            time = data
            cleared_print(absolute_time_to_timestamp(time))

        if event is AppEvent.Timer_Finished:
            clear_console()
            time_penalty_decision_answer = input(
                """
                Your time: {}
                Change penalty to +2 (1) or DNF (2)?
                Leave blank (hit "Enter") to continue.
                """.format(absolute_time_to_timestamp(data))
            )

            if time_penalty_decision_answer.__eq__('1'):
                self.notify_listeners(event=AppEvent.Penalty_Update, data=Penalty.Plus_Two)
            elif time_penalty_decision_answer.__eq__('2'):
                self.notify_listeners(event=AppEvent.Penalty_Update, data=Penalty.Dnf)

            self.notify_listeners(event=AppEvent.Timer_Finished_Penalty_With_Decision)

        if event is AppEvent.App_Mode_Exited:
            self.do_menu_popup()

        if event is AppEvent.App_Timer_Entered:
            clear_console()
            print(
                """
                >>> You are in the timer! Use the space bar to toggle/control start/stop.
                To quit/back to the menu, just hit "Esc" (this may cause console window lost focus).
                """.strip().lstrip()
            )

        if event is AppEvent.App_See_Solves_Entered:
            solves = data
            clear_console()
            if len(solves) > 0:
                print('This is your solves:')
                index = 0
                for s in solves:
                    # print("{}. {}\t{}".format(index + 1, absolute_time_to_timestamp(s.time), s.scramble))
                    print(s.time)
                print('\n')
                while True:
                    back_to_menu_answer = input('Back to menu? (y)')
                    if back_to_menu_answer.__eq__('y'):
                        self.notify_listeners(AppEvent.App_Mode_Exit_Request, 2)
                        break
            else:
                print("You don't have solves yet. Back to menu (b) and go timer to perform some!")

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
        self.notify_listeners(AppEvent.App_Menu_Entered, int(menu_answer) - 1)
