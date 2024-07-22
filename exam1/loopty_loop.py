from typing import Callable, List


def generate_list(start: int, stop: int, step: int = 1) -> List[int]:
    """
    Generate a list of integers.

    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param step: How many digits apart each number is from the others around it.
    :return: A list of integers.
    """
    # 
    # parity?
    # stop stop step
    result = [i for i in range(start, stop, step)]
    return result
    pass  # implement me

    # if parity == Parity.ODD:
    #     #if divisible by 2 (not odd)
    #     return [i for i in range(start, stop) if i  % 2 != 0]

def generate_list_with_strategy(start: int, stop: int, step: int, strategy: Callable) -> List[int]:
    """
    Generate a list of integers.

    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param step: How many digits apart each number is from the others around it.
    :param strategy: A function to manipulate each digit .
    :return: A list of integers.
    """
    pass  # implement me
