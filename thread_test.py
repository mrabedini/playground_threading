import logging
from logging import StreamHandler
import time
import timeit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def do_something():
    logger.info("Waiting for 1 seconds.")
    time.sleep(1)
    logger.info("Wait was done")


start = timeit.default_timer()
do_something()
do_something()
end = timeit.default_timer()

logger.info("Execution took %f seconds", end - start)

