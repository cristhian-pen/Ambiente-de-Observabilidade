# Base oficial do Python
FROM python:3.12-slim

# Diretório de trabalho
WORKDIR /app/App

# Copiar dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar sua aplicação inteira
COPY . .

# =============================
# Variáveis de OpenTelemetry
# =============================
ENV OTEL_LOGS_EXPORTER=otlp
ENV OTEL_METRICS_EXPORTER=otlp
ENV OTEL_TRACES_EXPORTER=otlp

# IMPORTANTE: no Docker, não usar localhost → use o nome do serviço no docker-compose
# Exemplo com otel-collector rodando no compose:
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317

# Nome do serviço (aparece no Grafana Tempo + Loki + Grafana Cloud)
ENV OTEL_SERVICE_NAME=lista-skins-cs2-app

# Expor porta da aplicação (caso precise)
EXPOSE 5000

# Comando de inicialização
CMD ["python", "App/app.py"]