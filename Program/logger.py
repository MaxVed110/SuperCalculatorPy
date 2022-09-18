import logging

logger = logging.getLogger('Calculator')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('logger.log', 'w', 'utf-8')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)
