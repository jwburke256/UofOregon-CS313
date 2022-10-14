import math


class mathOps:
    """
    Simple math operations on a given pair of integers, u and v.

    This includes the lcm (least common multiple) and 
    gcd (greatest common divisor) functions, each of returns an integer.
    """

    def __init__(self, u, v):
        '''Set the values of u and v to be used in the math operations.'''
        self.u = u
        self.v = v

    def __repr__(self):
        return "mathOps({}, {})".format(self.u, self.v)

    def valid(self):
        """True if both u and v are integers."""
        return isinstance(self.u, int) and isinstance(self.v, int)

    def gcd(self):
        '''Compute the greatest common divisor of member variables u and v.'''
        # Find the greatest common divisor of a and b
        # Hint: Use Euclid's Algorithm
        # https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
        tempU = abs(self.u)  # abs accounts for negative arguments
        tempV = abs(self.v)  # abs accounts for negative arguments

        # corrects for floats:
        if type(tempU) == float:
            tempU = math.ceil(tempU)
        if type(tempV) == float:
            tempV = math.ceil(tempV)

        # checks for string argument
        try:
            if type(tempU) == str or type(tempV) == str:
                raise TypeError
        except TypeError:
            print("one or both the values of", tempU, " and ", tempV, "are strings, only allowed ints or floats")
            raise TypeError

        # checks for infinity argument
        try:
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError
        except OverflowError:
            print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
            raise OverflowError

        # checks for all zeroes argument
        try:
            if (tempU == 0) & (tempV == 0):
                raise ValueError
        except ValueError:
            print("both values of", tempU, " and ", tempV, "are 0s")
            raise ValueError

        # ENTER YOUR CODE HERE
        # Feel free to modify the exceptions, delete the try block etc or the entire function
        # Just keep the function name as gcd
        if tempU == 0:  # checks to see if floor is reached for tempU
            return tempV
        if tempV == 0:  # checks to see if floor is reached for tempV
            return tempU
        while tempU != tempV:
            if tempU < 0 or tempV < 0:  # returns none if gcd doesn't exist in loop
                return None
            if tempU > tempV:
                tempU = tempU - tempV
            else:
                tempV = tempV - tempU
        return tempU

    def lcm(self):
        """Compute the least common multiple of member variables u and v."""
        # Hint: Use the gcd of a and b
        tempU = abs(self.u)  # abs accounts for negative arguments
        tempV = abs(self.v)  # abs accounts for negative arguments

        # corrects for floats:
        if type(tempU) == float:
            tempU = math.ceil(tempU)
        if type(tempV) == float:
            tempV = math.ceil(tempV)

        # checks for string argument
        try:
            if type(tempU) == str or type(tempV) == str:
                raise TypeError
        except TypeError:
            print("one or both the values of", tempU, " and ", tempV, "are strings, only allowed ints or floats")
            raise TypeError

        # checks for infinity argument
        try:
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError
        except OverflowError:
            print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
            raise OverflowError

        # checks for single 0 lcm
        try:
            if (tempU == 0 and tempV != 0) or (tempV == 0 and tempU != 0):
                raise ValueError
        except ValueError:
            print("one of the values of", tempU, " and ", tempV, "are 0s, LCM undefined")
            raise ValueError

        # ENTER YOUR CODE HERE
        # Feel free to modify the exceptions, delete the try block etc or the entire function
        # Just keep the function name as lcm
        result = (tempU * tempV) / (mathOps(tempU, tempV).gcd())
        return result
