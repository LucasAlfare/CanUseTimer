from time import time
import sys
import os


def get_current_time():
    """
    This is a function to be used globally in order to use a consistent
    time over the application
    :return: The current time in milliseconds.
    """
    return int(time() * 1000)


# TODO: fix duplicate timestamp return
def absolute_time_to_timestamp(absolute_time=0):
    if absolute_time == -1:
        return 'DNF'

    seconds = (absolute_time / 1000) % 60
    milliseconds = (absolute_time / 1000)

    if absolute_time >= 60_000:
        minutes = absolute_time / 60_000
        return "{}:{}.{}".format(minutes, seconds, milliseconds)

    return "{}.{}".format(seconds, milliseconds)


def cleared_print(text=""):
    """
    Auxiliary method to print strings in same console line.
    This function just "erases" the current line and write the text parameter.
    :param text: string to be printed
    :return: None
    """
    sys.stdout.write('\r')
    sys.stdout.write(' ' * 20)
    sys.stdout.write('\r')
    sys.stdout.write(text)
    sys.stdout.flush()


def clear_console():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')
