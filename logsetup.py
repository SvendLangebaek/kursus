import logging
from logging.handlers import RotatingFileHandler


def setup_logging():
	handler = RotatingFileHandler(
		filename='log_output',
		maxBytes=1024*1024,
		backupCount=3,
		encoding='utf-8'
	)

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler.setFormatter(formatter)

	root_logger = logging.getLogger()
	root_logger.setLevel(logging.INFO)
	root_logger.addHandler(handler)
