import logging


# logging.basicConfig(
#     level=logging.DEBUG
# )

#logging.debug("Ovo je debug")

#create logger i give name
logger = logging.getLogger(__name__)

#set level
logger.setLevel(logging.INFO)

#namjestimo formatiranje
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

#file logger
file_handler = logging.FileHandler('log1.log')

#console logger
stream_handler = logging.StreamHandler()

#dodaj format
file_handler.setFormatter(formatter)

#dodaj handler
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info("Kako si?")