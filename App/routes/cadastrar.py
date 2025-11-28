from flask import Blueprint, request
from functions.cadastrarNovaSkin import CadastrarNovaSkin;
from Logs.logger import logger

route = Blueprint("route", __name__)

@route.route("/cadastraSkin", methods=["POST"])
def cadastra_skin():
    try:
        nomeSkin = request.form["nome"]
        modeloSkin = request.form["modelo"]
        statrackSkin = request.form.get("stattrak","false")
        souvenirSkin = request.form.get("souvenir", "false")
        
        CadastrarNovaSkin(nomeSkin,modeloSkin, statrackSkin, souvenirSkin)
        
        logger("Skin cadastrada no banco!", "INFO")
        
        return "<h3>Skin cadastrada com sucesso!</h3>"
        
    except Exception as e:
        
        logger(f'Ocorreu um erro ao cadastrar a skin: {e}', "ERROR")
    
    finally:
        logger("Retornando a pagina inicial", "DEBUG")
