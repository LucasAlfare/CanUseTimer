from canusetimer.Misc import clear_console


class Dialog:
    """
    This class describes a single dialog message in the console.

    All user interactions should be done over dialogs, so all then
    must implement this interface in order to make its behaviour consistent.
    """
    def __init__(self, message='', actual_answer='', expected_answers=None, event_manageable=None):
        """
        Creates a standard dialog, where:

        :param message: is the main message that this dialog should prompt
        :param actual_answer: is the actual answer that user input to this dialog
        :param expected_answers: is a list with the target accepted possible answers this dialog accepts
        :param event_manageable: is a reference to an entity that can propagate events to other listeners.
        """
        if expected_answers is None:
            expected_answers = ['']

        self.message = message.strip()
        self.expected_answers = expected_answers
        self.actual_answer = actual_answer.strip()
        self.event_manageable = event_manageable

    def actual_answer_is_valid(self):
        """
        This function is used to check if the actual answer input by the user is valid.

        :return: True if valid or False if not.
        """
        return self.expected_answers.__contains__(self.actual_answer)

    def on_valid(self):
        """
        This method is called when a valid answer was input.
        """
        raise NotImplementedError("Not implemented yet.")

    def on_invalid(self):
        """
        This method is called when an invalid answer was input.
        """
        raise NotImplementedError("Not implemented yet.")

    def start(self):
        """
        Starts this current dialog.

        This will run indefinitely until a valid
        answer enters through an ```input()``` call.
        """
        while True:
            self.ask_for_answer()
            if self.advance():
                break

    def advance(self):
        """
        This method checks is the current answer that came from input
        is valid and call the target interface method depending on the
        analysis.

        :return: True if the dialog was successfully processed or False if
        the dialog successfully processed the target invalid function.
        """
        if self.actual_answer_is_valid():
            self.on_valid()
            return True
        else:
            self.on_invalid()
            return False

    def ask_for_answer(self):
        """
        This method clear the console and throw the specified
        dialog text message to the console, while keeps stopped
        waiting by some input.
        """
        clear_console()
        self.actual_answer = input(self.message).strip()
