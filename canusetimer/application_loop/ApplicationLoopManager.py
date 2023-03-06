from canusetimer.EventListening import EventManageable, AppEvent
from canusetimer.Misc import clear_console, clear_and_println, absolute_time_to_timestamp
from canusetimer.dialog.MenuDialog import Menu
from canusetimer.dialog.SeeSolvesDialog import SeeSolves
from canusetimer.dialog.ClearSolvesDialog import ClearSolves
from canusetimer.dialog.Texts import *
from canusetimer.dialog.Answers import *
from threading import Thread


class ApplicationLoopManager(EventManageable):
    current_dialog = None
    tmp_scramble = ''
    scramble_thread = None
    scramble_updated = False

    def initialize(self):
        self.do_main_menu_dialog()
        self.notify_listeners(AppEvent.Request_Scramble_Generated)

    def on_event(self, event, data):
        if event is AppEvent.Timer_Started:
            clear_console()

        if event is AppEvent.App_Timer_Entered:
            print(Timer_Menu_Greeting_Text.strip())

        if event is AppEvent.Timer_Ready:
            # clear_console()
            print(Timer_Menu_Greeting_Text.strip())

        if event is AppEvent.Scramble_Generated:
            self.scramble_updated = False
            self.setup_scramble_thread(target_data=data)

        if event is AppEvent.Timer_Update:
            time = data
            clear_and_println(absolute_time_to_timestamp(time))

        if event is AppEvent.App_Mode_Exited:
            self.do_main_menu_dialog()

        if event is AppEvent.App_See_Solves_Entered:
            solves = data

            if len(solves) > 0:
                # TODO: refactor/move this listing solves to an appropriated scope.
                see_solves_text = See_Solves_Header_Text

                index = 0
                for s in solves:
                    see_solves_text += See_Solves_Solve_Row_Text.format(
                        index + 1,
                        absolute_time_to_timestamp(s.time),
                        s.penalty,
                        s.scramble
                    )
                    index += 1

                see_solves_text += See_Solves_Footer_Text
            else:
                see_solves_text = See_Solves_Empty_Text

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

    def do_timer_greet_process(self):
        # clear_console()
        print(Timer_Menu_Greeting_Text.strip())
        print(Timer_Scramble_Presentation_Text.format(self.tmp_scramble))

    def setup_scramble_thread(self, target_data):
        def scramble_thread_target():
            while not self.scramble_updated:
                self.tmp_scramble = target_data[1]
                print(self.tmp_scramble)
                self.scramble_updated = True

        self.scramble_thread = Thread(target=scramble_thread_target)
        self.scramble_thread.start()
