from flask import Flask, render_template;
from routes.cadastrar import route
from routes.listar import listRoute
from Logs.logger import logger
from Instrumentation.otel import Instrumentation, InstrumentationLogs
import logging


app = Flask(
    __name__,
    template_folder="src/templates",
    static_folder="src/static"
)

log = logging.getLogger(__name__)

Instrumentation(app)
InstrumentationLogs()

@app.route("/")
def Home():
    logger("A pagina home foi acessada", "INFO")  
    return render_template("index.html")

app.register_blueprint(route)
app.register_blueprint(listRoute)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)