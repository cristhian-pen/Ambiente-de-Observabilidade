import logging
from datetime import datetime

def crialogger():
   
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler()]
    )


def logger(mensagem, nivel):

    crialogger()
    log = logging.getLogger(__name__)

    match nivel:
        case "ERROR": log.error(mensagem)
        case "CRITICAL": log.critical(mensagem)
        case "INFO": log.info(mensagem)
        case "DEBUG": log.debug(mensagem)

        