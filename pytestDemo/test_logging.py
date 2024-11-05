import logging

def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) #filehandler object

    logger.setLevel(logging.INFO) #you will see logs above INFO level included INFO
    logger.debug("A debug statement is executed")
    logger.info("An info statement is executed")
    logger.warning("Warning executed")
    logger.error("error occured")
    logger.critical("critical issue")