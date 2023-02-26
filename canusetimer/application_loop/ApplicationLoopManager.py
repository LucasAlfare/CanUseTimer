from canusetimer.EventListening import EventManageable, AppEvent
from canusetimer.Misc import clear_console, clear_and_println, absolute_time_to_timestamp
from canusetimer.dialog.Menu import Menu
from canusetimer.dialog.SeeSolves import SeeSolves
from canusetimer.dialog.ClearSolves import ClearSolves
from canusetimer.dialog.Texts import *
from canusetimer.dialog.Answers import *


class ApplicationLoopManager(EventManageable):
    current_dialog = None

    def initialize(self):
        self.do_main_menu_dialog()

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
            self.do_main_menu_dialog()

        if event is AppEvent.App_See_Solves_Entered:
            solves = data

            if len(solves) > 0:
                # TODO: refactor/move this listing solves to an appropriated scope.
                see_solves_text = 'This is your solves:\n'

                index = 0
                for s in solves:
                    see_solves_text += "{}. {} {}\t{}\n" \
                        .format(index + 1, absolute_time_to_timestamp(s.time), s.penalty, s.scramble)
                    index += 1

                see_solves_text += 'Back to menu? (y) '
            else:
                see_solves_text = "You don't have solves yet. Back to menu? (y) "

            self.current_dialog = SeeSolves()
            self.current_dialog.message = see_solves_text
            self.current_dialog.expected_answers = See_Solves_Answers
            self.current_dialog.event_manageable = self
            self.current_dialog.start()

        if event is AppEvent.App_Clear_Solves_Entered:
            self.current_dialog = ClearSolves()
            self.current_dialog.message = Menu_Clear_Solves_Message_Text
            self.current_dialog.expected_answers = Clear_Solves_Answers
            self.current_dialog.event_manageable = self
            self.current_dialog.start()

    def do_main_menu_dialog(self):
        self.current_dialog = Menu()
        self.current_dialog.message = Menu_Message_Text
        self.current_dialog.expected_answers = Menu_Answers
        self.current_dialog.event_manageable = self
        self.current_dialog.start()
