import concurrent.futures
import logging
from logging import StreamHandler
import time
import timeit


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def do_something(wait_time):
    logger.info("Waiting for %d seconds.", wait_time)
    time.sleep(wait_time)
    return f"Wait was done for {wait_time} seconds."


start = timeit.default_timer()

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executer:
    secs = [5, 4, 3, 2, 1]
    results = [executer.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        logger.info("result %s", f.result())

end = timeit.default_timer()
logger.info("Execution took %f seconds", end - start)

