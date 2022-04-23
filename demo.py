import logging

logging.basicConfig(level=logging.INFO)  # optional, logging also works without this line


try:
    # error: to many arguments
    logging.info("test message 1: %d(%s)", 100, "blah", "more blah")
except Exception:
    pass

print()

logging.info("test message 2: %d(%s)", 100, "blah")  # OK

print()

try:
    # error: not enough arguments
    logging.info("test message 3: %d(%s)", 100)
except Exception:
    pass

print()

try:
    # error: not enough arguments
    logging.info("test message 4: %d(%s)")
except Exception:
    pass

print()

logging.debug("with the default logging level this message won't show")

logging.setLevel(logging.DEBUG)

logging.debug("debug output")
logging.info("this is informational")
logging.warning("this is a warning")
logging.error("this is an error")
logging.critical("this is critical")

try:
    1 / 0
except Exception as e:
    logging.exception(e, "oops %s is an exception", "this")

print()

# incorrect format string will raise an exception when used
#
logging.basicConfig(format="%(levelname)s %(unknown)s")

try:
    # error because of incorrect format string
    logging.info("test message")
except Exception:
    pass

print()

# when using logging in multiple modules create a logger per module
#
logging.basicConfig(format="%(asctime)s:%(levelname)-7s:%(name)s:%(message)s")

logger = logging.getLogger("another_logger")

logger.info("this message comes from a separate logger, note the name")

# log to file
#
logging.basicConfig(filename="log.txt", filemode='w')

logging.critical("last message")
