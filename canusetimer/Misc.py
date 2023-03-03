import subprocess
import platform
import sys
from time import time


def get_current_time():
    """
    This is a function to be used globally in order to use a consistent
    time over the application
    :return: The current time in milliseconds.
    """
    return int(time() * 1000)


def absolute_time_to_timestamp(absolute_time=0):
    """
    This function converts an absolute time (in milliseconds) to a
    timestamp of format [mm:ss.SSS], where mm=minutes, ss=seconds and
    SSS=milliseconds.

    If minutes are processed as 0, the function doesn't insert it, being the
    final format for this case [ss.SSS].

    Also, this function automatically formats any time with -1 value to
    'DNF' (did not finish) stamp.
    """
    if absolute_time == -1:
        return 'DNF'

    seconds = str(int((absolute_time / 1000) % 60)).rjust(2, '0')
    milliseconds = str(absolute_time % 1000).rjust(3, '0')

    if absolute_time >= 60_000:
        minutes = str(absolute_time / 60_000).rjust(2, '0')
        return "{}:{}.{}".format(minutes, seconds, milliseconds)
    return "{}.{}".format(seconds, milliseconds)


def clear_and_println(text=""):
    """
    Auxiliary method to print strings in same console line.
    This function just "erases" the current line and write the text parameter.
    :param text: string to be printed
    """
    clear_console()
    print(text)


def clear_console():
    """
    This method just clears the console.
    Source: https://stackoverflow.com/a/23075152
    """
    if platform.system() == "Windows":
        if platform.release() in {"10", "11"}:
            # Needed to fix a bug regarding Windows 10;
            # not sure about Windows 11
            subprocess.run("", shell=True)
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else:  # Linux and Mac
        print("\033c", end="")
