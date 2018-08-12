def integerdivision_(x=5,a=3):
    """x: a non-negative integer argument 
    a: a positive integer argument
    returns: integer, the integer division of x divided by a."""
    count_ = 0 
    while x >= a:
        count_ += 1
        x = x - a
    return count_
print(integerdivision_())