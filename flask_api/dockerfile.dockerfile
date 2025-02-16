# usando a versão slim do Python 3.9
FROM python:3.9-slim

# definir o diretório de trabalho dentro do container
WORKDIR /app

# copiar o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# instalar as dependências do projeto sem armazenar cache
RUN pip install --no-cache-dir -r requirements.txt

# copiar o código-fonte do aplicativo Flask para o container
COPY app.py .

# expõe a porta 5000 para permitir acessos externos à API Flask
EXPOSE 5000

# definir o comando padrão para rodar o aplicativo quando o container iniciar
CMD ["python", "app.py"]
