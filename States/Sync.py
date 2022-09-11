from States.AbstractState import AbstractState


class Sync(AbstractState):
    def action(self):
        print("SYNC")
