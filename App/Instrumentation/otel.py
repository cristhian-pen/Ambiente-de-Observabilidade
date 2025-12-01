from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry import trace
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
import logging

def Instrumentation(app):
    
    resource = Resource({
        "service_name": "skins-cs2-api API",
        "service_version": "1.0.0",
        "deployment_enviroment": "development"
    })
    
    
    provider = TracerProvider(resource=resource)
    
    
    #Alterar o endpoint do Tempo
    exporter = OTLPSpanExporter(
        
        endpoint="http://otel-collector:3200/v1/traces"
    )
    
    span_processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(span_processor)
    
    trace.set_tracer_provider(provider)
    
    FlaskInstrumentor().instrument_app(app)
    
    RequestsInstrumentor().instrument()
    
def InstrumentationLogs():
    
    resouce = Resource.create({
            "service_name": "skins-cs2-api API"
        })
    
    logProvider = LoggerProvider(resource=resouce)
    
    
    #Alterar o endpoint do Loki
    exporter = OTLPSpanExporter(
        endpoint="http://loki:3100/v1/logs"
    )
    
    logProvider.add_log_record_processor(
        BatchLogRecordProcessor(exporter)
    )
    
    handler = LoggingHandler(level=logging.INFO, logger_provider=logProvider)
    
    logging.getLogger().addHandler(handler)
    
    LoggingInstrumentor().instrument(set_logging_format=True)