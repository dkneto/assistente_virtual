# Assistente Virtual com Reconhecimento de Voz

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-✔-success.svg)

Um assistente virtual que utiliza processamento de linguagem natural (PLN) para executar comandos por voz, com módulos de text-to-speech e speech-to-text.

## 📦 Instalação

### Pré-requisitos
- Docker instalado
- Python 3.9+
- Microfone funcional

### Passos para executar:
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/assistente_virtual.git
cd assistente_virtual

# Rode localmente para identificar corretamente o microfone
python src/main.py

# Construa e execute com Docker
docker-compose up --build

