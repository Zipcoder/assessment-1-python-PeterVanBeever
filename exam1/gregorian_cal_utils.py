def is_leap_year(year: int) -> bool:
    """
    Given a year, this function returns a boolean indicating whether or not it is a leap year.

    :param year: an integer indicating a year.
    :return: A boolean indicating whether or not the year parameter is a leap year.
    """
    # leap year every 4yrs
    # 400 not 100
    # boolean
    # modulous 4
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    pass  # implement me
