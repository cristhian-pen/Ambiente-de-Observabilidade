from flask import Flask, render_template;
from routes.cadastrar import route
from routes.listar import listRoute
from Logs.logger import logger
from Instrumentation.otel import Instrumentation, InstrumentationLogs
import logging
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(
    __name__,
    template_folder="src/templates",
    static_folder="src/static"
)

log = logging.getLogger(__name__)
metrics = PrometheusMetrics(app)
Instrumentation(app)
InstrumentationLogs()

#Configurações dos containers
grafana = 3000
loki = 3200
tempo = 3100
otel = 4317
prometheus = 5000

@app.route("/")
def Home():
    logger("A pagina home foi acessada", "INFO")  
    return render_template("index.html")

app.register_blueprint(route)
app.register_blueprint(listRoute)


if __name__ == "__main__":
    print(f"""
Serviços da aplicação:
          
- {otel}: OpenTelemetry GRPC endpoint
- {grafana}: Grafana (http://localhost:3000). User: admin, password: admin
- {loki}: Loki 
- {tempo}: Tempo
- {prometheus}: Prometheus endpoint
          """)
    app.run(host="0.0.0.0", port=5000)