
def drop_last(lst):
    """
    This function takes a list and returns a list with the last item removed.
    """
    # use pop?
    # return lst.pop()?
    lst.pop()
    # don't return pop()
    return lst
    pass  # implement me

def drop_mangle(lst):
    """
    This function takes a list and returns a list with the first two items AND last item removed.
    """

    # pop last
    lst.pop()
    # del
    del lst[0]
    # del lst[1] shifted?
    del lst[0]
    return lst
    pass  # implement me

def add_item_front(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item prepended to the list
    """
    pass  # implement me

def add_item_end(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item appended to the list
    """
    pass  # implement me

def drop_first_two(lst):
    """
    This function takes a list and returns a list with the first two items removed.
    """
    pass  # implement me

def drop_last_two(lst):
    """
    This function takes a list and returns a list with the last two items removed.
    """
    pass  # implement me

