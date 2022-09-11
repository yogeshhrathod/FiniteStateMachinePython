
from States.AbstractState import AbstractState


class Ping(AbstractState):
    def action(self):
        print("PING")
