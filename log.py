import logging
import os
from multi_process_logger import MultiProcessRotatingFileHandler as mprf

def init_log():
    log_dir = './log'
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    format = '%(asctime)s, %(levelname)s %(message)s'
    filename = os.path.join(log_dir, 'server.log')
    level = logging.INFO

    logger = logging.getLogger()
    logger.setLevel(level)
    logging .getLogger('requests').setLevel(logging.WARNING)
    logging .getLogger('werkzeug').setLevel(logging.WARNING)
    formatter = logging.Formatter(format)


    handler = mprf(filename=filename, when='midnight')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    ch = logging.StreamHandler()
    formatter = logging.Formatter(format)
    ch.setFormatter(logging.Formatter(format))
    ch.setLevel(logging.INFO)
    logging .getLogger('requests').setLevel(logging.WARNING)
    logging .getLogger('werkzeug').setLevel(logging.WARNING)
    logger.addHandler(ch)
