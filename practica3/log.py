import logging

def my_log(name):
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    c_logger = logging.StreamHandler()
    c_logger.setLevel(logging.INFO)

    C_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_logger.setFormatter(C_format)

    logger.addHandler(c_logger)

    return logger