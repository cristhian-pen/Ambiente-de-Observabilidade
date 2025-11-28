import logging
from datetime import datetime

def crialogger(nome_arquivo="app.log"):
   
    logging.basicConfig(
        filename=nome_arquivo,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def logger(mensagem, nivel):

    crialogger()
    
    log = logging.getLogger(__name__)

    if nivel == "ERROR":
        log.error(mensagem)

    elif nivel == "CRITICAL":
        log.critical(mensagem)

    elif nivel == "INFO":
        log.info(mensagem)
    
    elif nivel == "DEBUG":
        log.debug(mensagem)


    