import logging


def log(name='main', file='logs.log', level='DEBUG'):
    # Levels logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logging_types = dict(
        DEBUG=logging.DEBUG,
        INFO=logging.INFO,
        WARNING=logging.WARNING,
        ERROR=logging.ERROR,
        CRITICAL=logging.CRITICAL)
    # Creating the new logger
    logger = logging.getLogger(name)
    # Set logging level
    logging_level = logging_types.get(level) \
        if logging_types.get(level) \
        else logging_types.get('DEBUG')
    logger.setLevel(logging_level)
    # Created file handler and set formatter
    file_handler = logging.FileHandler(file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    # Added file handler and formatter
    logger.addHandler(file_handler)
    return logger
