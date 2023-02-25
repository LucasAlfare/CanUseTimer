class Command:

    def __init__(self, command):
        self.command = command

    def validate(self):
        raise NotImplementedError("Please Implement this method")
