from EventListening import AppEvent

input_press = AppEvent.Timer_Toggle_Down
input_release = AppEvent.Timer_Toggle_Up


class TimerState:
    """
    This class describes what a timer state can do.
    Normally a timer state is a moment in what the timer is in.
    Also, these methods doesn't have any implementation in this file, all
    of its implementations goes to their appropriated children.
    """

    def handle_input(self, input_type, data=None):
        """
        This method is used to handle an incoming input with some
        optional data.

        :param input_type: one item from EventListening.AppEvent (Timer_Toggle_Down or Timer_Toggle_Up)
        :param data: ayn kind of information needed to decide what should be the next state
        :return: the next state based on the parameters
        """
        raise NotImplementedError("Not implemented yet.")

    def update(self, event_manageable, data):
        """
        All things related to update of this state is made in this method.

        :param event_manageable: a reference to an entity that can notify events
        :param data: some data to be carried with the event notification
        :return: None
        """
        raise NotImplementedError("Not implemented yet.")

    def suspend(self):
        """
        This method is used to cancel any kind of running task of this state.
        E.g.: looping threads.
        :return: None
        """
        raise NotImplementedError("Not implemented yet.")
