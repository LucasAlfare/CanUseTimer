class Penalty:
    Ok, Plus_Two, Dnf = range(3)


class Solve:

    def __init__(self, time=0, scramble='[no scramble]', penalty=Penalty.Ok):
        self.time = time
        self.scramble = scramble
        self.penalty = penalty
