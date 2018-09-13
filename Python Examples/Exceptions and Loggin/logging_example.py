import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

# Create and configure logger
# if file does not exist python will create it
""" BasicConfig has a default level of WARNING = 30
logging.basicConfig(filename = "lumberjack.log")"""
# This garantees that we will see all logging mesages.
logging.basicConfig(filename = "lumberjack.log", level = logging.DEBUG, format = LOG_FORMAT)

logger = logging.getLogger()

# you can give a logger a name, but it can have some issues
# Working just with one logger as in this example, it is know as working with a 
# ROOT LOGGER

#Test the Logger
# Info has a level of 20
logger.info("Our Second Message")
print(logger.level)

# Test Messages in all levels
logger.debug("This is a harmeless debug message.")
logger.info("Just some useful information") 
logger.warning("I am sorry I can not do that.")
logger.error("Did you just try to divide by zero")
logger.critical("The entire internet has been deleted")