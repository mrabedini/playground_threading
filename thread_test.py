import logging
from logging import StreamHandler
import threading
import time
import timeit


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def do_something():
    logger.info("Waiting for 1 seconds.")
    time.sleep(1)
    logger.info("Wait was done")

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

start = timeit.default_timer()
t1.start()
t2.start()
t1.join()
t2.join()
end = timeit.default_timer()

logger.info("Execution took %f seconds", end - start)

