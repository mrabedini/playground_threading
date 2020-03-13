import logging
from logging import StreamHandler
import threading
import time
import timeit


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def do_something(wait_time):
    logger.info("Waiting for %d seconds.", wait_time)
    time.sleep(wait_time)
    logger.info("Wait was done for %d seconds.", wait_time)


t1 = threading.Thread(target=do_something,args=[1])
t2 = threading.Thread(target=do_something,args=[2])

start = timeit.default_timer()
t1.start()
t2.start()
t1.join()
t2.join()
end = timeit.default_timer()

logger.info("Execution took %f seconds", end - start)

