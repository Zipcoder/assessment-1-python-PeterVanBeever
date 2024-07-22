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
    # 'strategy' = python syntax 
    result = [i for i in range(start, stop, step)]
    res_strategy = [strategy(i) for i in result]
    return res_strategy

# start value, number of values , increment,

#             ((1, 5, 1, lambda x: x**2), [1, 4, 9, 16]),
#             ((5, 10, 1, lambda x: x+5), [10, 11, 12, 13, 14]),
#             ((100, 0, -25, lambda x: x/5), [20, 15, 10, 5]),
#             ((100, 50, -10, lambda x: x-10), [90, 80, 70, 60, 50]),
    pass  # implement me
