from canusetimer.EventListening import EventManageable, AppEvent
from canusetimer.data.Definitions import Solve, Penalty


class DataManager(EventManageable):

    solves = []
    tmp_elapsed_time = 0
    tmp_scramble = ''
    tmp_penalty = Penalty.Ok

    def initialize(self):
        pass

    def on_event(self, event, data):
        if event is AppEvent.App_Menu_Entered:
            menu_option = data
            if menu_option == 2:
                self.notify_listeners(AppEvent.App_See_Solves_Entered, self.solves)
            elif menu_option == 3:
                self.solves = []
                self.notify_listeners(AppEvent.App_See_Solves_Entered, self.solves)

        if event is AppEvent.App_Mode_Exit_Request:
            active_menu_id = data
            if active_menu_id == 2:
                self.notify_listeners(AppEvent.App_Mode_Exited)

        if event is AppEvent.Penalty_Update:
            self.tmp_penalty = data

        if event is AppEvent.Timer_Finished:
            self.tmp_elapsed_time = data
            next_solve = Solve(
                time=self.tmp_elapsed_time,
                scramble=self.tmp_scramble,
                penalty=self.tmp_penalty
            )
            self.solves.append(next_solve)
            self.notify_listeners(AppEvent.Solves_Update, self.solves)
