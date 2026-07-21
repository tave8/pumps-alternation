import random


def ottieni_livello_variato(livello_attuale: float, input_min: float, input_max: float, step_max: float = 5) -> float:
    livello_attuale = max(input_min, min(input_max, livello_attuale))
    delta = round(random.uniform(-step_max, step_max), 2)
    nuovo_livello = round(livello_attuale + delta, 2)

    if nuovo_livello > input_max:
        nuovo_livello = input_max
    elif nuovo_livello < input_min:
        nuovo_livello = input_min

    return nuovo_livello