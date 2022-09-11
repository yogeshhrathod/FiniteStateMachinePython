
from enum import Enum
from time import sleep
from typing import List

from States.AbstractState import AbstractState
from States.Ping import Ping
from States.Sync import Sync


class StateNames(Enum):
    INIT_STATE = 1
    PING = 2
    SYNC = 3
    FINAL = 4


class State:
    init_state = None
    end_state = None
    handler = None

    def __init__(self, init_state: str, handler: AbstractState, end_state: str) -> None:
        self.init_state = init_state
        self.handler = handler
        self.end_state = end_state


class StateMachine:
    _state_transitions = []
    _cur_state = None

    def __init__(self, state_transitions, initial_state: StateNames = StateNames.INIT_STATE) -> None:
        self._state_transitions = state_transitions
        self._cur_state = initial_state

    def _find_next_state(self, state: State) -> State:
        if not state:
            raise Exception("Empty State Found")
        for state in self._state_transitions:
            if state.init_state == self._cur_state:
                print(
                    f"state transtion from {state.init_state} to {state.end_state}")
                return state

    def _process_state_transition(self):
        next_state = self._find_next_state(self._cur_state)
        if next_state:
            self._cur_state = next_state.end_state
            next_state.handler.action()
        else:
            raise Exception(f"STATE NOT FOUND ->{self._cur_state}")

        sleep(1)

    def run(self):
        while True:
            try:
                self._process_state_transition()
            except Exception as e:
                print(e)
                print("Retring...")
                sleep(2)


if __name__ == '__main__':
    state_transitions: List = [
        State(StateNames.INIT_STATE, Ping(), StateNames.SYNC),
        State(StateNames.PING, Ping(), StateNames.SYNC),
        State(StateNames.SYNC, Sync(), StateNames.PING)
    ]

    app = StateMachine(state_transitions=state_transitions,
                       initial_state=StateNames.INIT_STATE)
    app.run()
