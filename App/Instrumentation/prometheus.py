from prometheus_client import start_http_server, Counter, Gauge, Summary, Histogram



def CreateCouter():
    quantidade_requests = Counter('http_request_total', 'Total de requisições')
    
    return quantidade_requests
    
    
def CreateGauge():
    
    gauge = Gauge('memory_usage_bytes', "Uso de memoria do sistema")
    

def CreateHistogram():
    
    summary = Histogram("http_server_duration_seconds", "Metrica que mede as requisições do sistema")