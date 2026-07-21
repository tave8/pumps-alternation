import time
from typing import Callable


def run_machine_in_loop(func: Callable, memory: dict) -> None:
    """
    Run a function in a loop.
    """

    while True:
        func(memory)
        time.sleep(1)


