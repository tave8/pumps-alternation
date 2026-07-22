import time
from typing import Callable


def run_machine_in_loop(func: Callable,
                        memory: dict,
                        on_iteration_end: Callable) -> None:
    """
    Run a function in a loop.
    """

    while True:
        func(memory, on_iteration_end)
        time.sleep(.01)


