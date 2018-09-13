import logging
import math
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

# This garantees that we will see all logging mesages.
# filemode = 'w' will delete all the logging when the script is run
logging.basicConfig(filename = "in_action.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')

logger = logging.getLogger()

def quadratic_formula(a, b, c):
    """ Return the solutions to the equation ax^2 + bx + c = 0"""
    logger.info("Quadratic formula({0}, {1}, {2}".format(a,b,c))

    # Compute the Discriminant (The number under the square root sign)
    logger.debug("#Compute the Discriminant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug("#Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    #Return the 2 roots as a tuple
    logger.debug("#Return the 2 roots as a tuple")
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)