def to_usd(my_price):
    """
    This functions formats numbers to follow conventional US currency formatting.
    The parameters of this function is my_price which is a float.

    Invoke like this: to_usd(9.99)
    """
    return '${:,.2f}'.format(my_price)