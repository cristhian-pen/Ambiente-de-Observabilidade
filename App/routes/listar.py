from flask import Blueprint, jsonify
from functions.listarSkins import ListarSkins
from Logs.logger import logger
from Instrumentation.prometheus import CreateCouter


listRoute = Blueprint("listRoute",__name__)


@listRoute.get("/listaSkins")
def Listar():
    
    CreateCouter().inc()
    
    try:
        logger("Skins Listadas!","INFO")
        return jsonify(ListarSkins())
        
    except Exception as e:
        logger(f'Ocorreu um erro ao listar as skins: {e}', "ERROR")

