# Imagem base leve do Python
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /App

# Instalar dependências do sistema (caso necessárias)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar somente o requirements primeiro (melhora cache)
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação
COPY . .

# Expor porta padrão do Flask
EXPOSE 5000

# Comando padrão – ajustável caso use outro arquivo
CMD ["python", "app.py"]
