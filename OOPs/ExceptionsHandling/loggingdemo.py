import logging

logging.basicConfig(filename="mylogs.log", level=logging.INFO)
logging.critical("This is critical Error")
logging.error("This is error message")
logging.warning("This is a warning message")
logging.debug("THis is a debug message")
logging.info("This is info for use")