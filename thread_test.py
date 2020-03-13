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


threads = list()

for _ in range(10):
    t = threading.Thread(target=do_something)
    threads.append(t)


start = timeit.default_timer()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
end = timeit.default_timer()

logger.info("Execution took %f seconds", end - start)

