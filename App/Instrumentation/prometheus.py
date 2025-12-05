from prometheus_client import Counter, Gauge, Histogram
from flask import request
import time


request_total = Counter(
    "api_request_total",
    "Total de requisições recebidas",
    ["http_route", "http_request_method"]
)

api_latency = Histogram(
    "http_server_request_duration_seconds",
    "Tempo de latencia da aplicação",
    ["http_route", "", "http_request_method"]
)

active_users = Gauge(
    "active_users",
    "Quantidade de usuarios"
)


def InitMetrics(app):
    
    
    @app.before_request
    def before():
        app.start_time = time.time()    
        
    @app.after_request
    def after(response):
        
        latency = time.time() - app.start_time
        
        request_total.labels(
            http_request_method = request.method,
            http_route = request.path
        ).inc()
        
        api_latency.labels(
            http_route=request.path,
            http_request_method=request.method
        ).observe(latency)
    
        return response