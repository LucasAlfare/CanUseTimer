from canusetimer.EventListening import EventManageable, AppEvent
from canusetimer.Misc import clear_console, clear_and_println, absolute_time_to_timestamp
from canusetimer.console_dialog.Answers import *
from canusetimer.console_dialog.Menu import Menu
from canusetimer.console_dialog.Texts import *


class ApplicationLoopManager(EventManageable):
    current_dialog = None

    def initialize(self):
        self.do_menu_dialog()

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
            self.do_menu_dialog()

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

        if event is AppEvent.App_Clear_Solves_Entered:
            clear_console()
            clear_solves_confirmation = input("Delete all your solves? (y/n)")
            if clear_solves_confirmation.__eq__('y'):
                self.notify_listeners(AppEvent.Solves_Clear)
                clear_console()
                input("""All your solves was deleted. Hit "Enter" to back to menu...""")
                self.notify_listeners(AppEvent.App_Mode_Exit_Request, 3)

    def do_menu_dialog(self):
        self.current_dialog = Menu()
        self.current_dialog.message = Menu_Message_Text
        self.current_dialog.expected_answers = Menu_Answers
        self.current_dialog.event_manageable = self
        self.current_dialog.start()
