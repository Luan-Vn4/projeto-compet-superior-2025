# Use uma imagem oficial do Python como base
FROM python:3.12-slim

# Crie um diretório de trabalho
WORKDIR /app

# Copie os arquivos requirements e app
COPY requirements.txt .
COPY src/ src/

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta que a aplicação usará
EXPOSE 5000

ENV PYTHONPATH=/app

# Defina o comando padrão para rodar a aplicação
CMD ["python", "./src/main.py"]
