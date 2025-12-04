#!/bin/bash

# Script para subir toda a stack de observabilidade

echo "Parando e removendo containers antigos..."
docker-compose down -v

echo "Construindo a aplicação Flask..."
docker-compose build app

echo "Subindo todos os serviços em background..."
docker-compose up 

echo "Aguardando alguns segundos para os containers iniciarem..."
sleep 5

echo "Containers em execução:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo "Exibindo logs iniciais de cada serviço (últimas 10 linhas):"
for container in lista_skins_cs2-flask loki tempo grafana otel-collector; do
    echo "==================== $container ===================="
    docker logs --tail 10 $container
done

echo "Stack iniciada com sucesso!"
