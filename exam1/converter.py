def meters_to_feet(meters: float) -> float:
    """
    This function takes a float representing a measurement in meters
    and returns the corresponding value converted to feet.
    The result is rounded to 2 decimal places.

    :param meters: A float representing a measurement in meters.
    :return: A float representing the input measurement converted to feet.
    """
    # converstion rate = 3.280839895
    meter2feet = 3.280839895
    # multiply/round
    return round((meters * meter2feet),2)
    pass  # implement me


def feet_to_meters(feet: float) -> float:
    """
    This function takes a float representing a measurement in feet
    and returns the corresponding value converted to meters.
    The result is rounded to 2 decimal places.

    :param feet: A float representing a measurement in feet.
    :return: A float representing the input measurement converted to meters.
    """

    # conversion rate 3.280839895
    # divide 
    feet2meter = (1/3.280839895)
    # multiply/round
    return round((feet * feet2meter), 2)
    pass  # implement me


def kilometer_to_miles(kilometers: float) -> float:
    """
    This function takes a float representing a measurement in kilometers
    and returns the corresponding value converted to miles.
    The result is rounded to 2 decimal places.

    :param kilometers: A float representing a measurement in kilometers.
    :return: A float representing the input measurement converted to miles.
    """
    # conversion rate 0.62137119
    kilom2mile = 0.62137119
    # multiply and round 
    return round((kilom2mile * kilometers), 2)
    pass  # implement me


def miles_to_kilometers(miles: float) -> float:
    """
    This function takes a float representing a measurement in miles
    and returns the corresponding value converted to kilometers.
    The result is rounded to 2 decimal places.

    :param miles: A float representing a measurement in miles.
    :return: A float representing the input measurement converted to kilometers.
    """

    # conversion rate 0.62137119
    mile2kilom = 0.62137119
    # divide and round 
    return round((miles/mile2kilom),2)

    pass  # implement me


