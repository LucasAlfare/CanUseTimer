class Dialog:
    """
    This class describes a single dialog message in the console.

    All user interactions should be done over dialogs, so all then
    must implement this interface in order to make its behaviour consistent.
    """
    def __init__(self, message='', actual_answer='', target_answers=None, event_manageable=None):
        """
        Creates a standard dialog, where:

        :param message: is the main message that this dialog should prompt
        :param actual_answer: is the actual answer that user input to this dialog
        :param target_answers: is a list with the target accepted possible answers this dialog accepts
        :param event_manageable: is a reference to an entity that can propagate events to other listeners.
        """
        if target_answers is None:
            target_answers = ['']

        self.message = message
        self.target_answers = target_answers
        self.actual_answer = actual_answer
        self.event_manageable = event_manageable

    def actual_answer_is_valid(self):
        """
        This function is used to check if the actual answer input by the user is valid.

        :return: True if valid or False if not.
        """
        raise NotImplementedError("Please Implement this method")

    def on_valid(self):
        """
        This method is called when a valid answer was input.
        """
        raise NotImplementedError("Please Implement this method")

    def on_invalid(self):
        """
        This method is called when an invalid answer was input.
        """
        raise NotImplementedError("Please Implement this method")
