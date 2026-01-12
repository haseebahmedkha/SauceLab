

import logging

logging.basicConfig("test_execution.log",
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

def get_logger():
    return logging.getLogger()