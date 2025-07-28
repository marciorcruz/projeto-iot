# Projeto IoT - Sistema de Telemetria

Este projeto implementa um sistema completo de IoT para coleta e armazenamento de dados de telemetria usando MQTT, FastAPI e PostgreSQL.

## 🏗️ Arquitetura

O sistema é composto por 4 serviços principais:

- **PostgreSQL**: Banco de dados para armazenar os dados de telemetria
- **Mosquitto**: Broker MQTT para comunicação entre dispositivos
- **Web API**: Serviço FastAPI para receber e armazenar dados via MQTT
- **Simulator**: Simulador de dispositivo IoT que envia dados de temperatura e umidade

## 🚀 Como executar

### Pré-requisitos
- Docker
- Docker Compose

### Executando o projeto

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd projeto-iot
```

2. Execute o projeto:
```bash
docker-compose up -d
```

3. Verifique se todos os serviços estão rodando:
```bash
docker-compose ps
```

## 📊 Testando o sistema

### Endpoints da API

- **Status da API**: `GET http://localhost:8000/`
- **Health Check**: `GET http://localhost:8000/health`
- **Dados de Telemetria**: `GET http://localhost:8000/telemetry?limit=10`
- **Documentação Swagger**: `http://localhost:8000/docs`

### Exemplos de uso

```bash
# Verificar status da API
curl http://localhost:8000/

# Obter últimos 10 dados de telemetria
curl http://localhost:8000/telemetry

# Obter últimos 5 dados de telemetria
curl http://localhost:8000/telemetry?limit=5

# Health check
curl http://localhost:8000/health
```

### Resposta da API de telemetria

```json
{
  "count": 10,
  "data": [
    {
      "id": 20,
      "device_id": "device123",
      "temperature": 21.49,
      "humidity": 51.47,
      "timestamp": "2025-07-28T17:33:29.424703"
    }
  ]
}
```

## 🔧 Configuração

### Portas utilizadas

- **8000**: API Web (FastAPI)
- **1883**: Broker MQTT (Mosquitto)
- **9001**: WebSocket MQTT (Mosquitto)
- **15432**: PostgreSQL

### Variáveis de ambiente

O projeto usa as seguintes variáveis de ambiente:

- `DATABASE_URL`: URL de conexão com PostgreSQL
- `MQTT_BROKER`: Endereço do broker MQTT
- `MQTT_PORT`: Porta do broker MQTT
- `MQTT_TOPIC`: Tópico MQTT para telemetria

## 📁 Estrutura do projeto

```
projeto-iot/
├── docker-compose.yml
├── mosquitto/
│   └── mosquitto.conf
├── simulator/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── simulator.py
└── web/
    ├── Dockerfile
    ├── requirements.txt
    ├── main.py
    ├── database.py
    ├── models.py
    └── mqtt.py
```

## 🛠️ Desenvolvimento

### Logs dos serviços

```bash
# Ver logs de todos os serviços
docker-compose logs

# Ver logs de um serviço específico
docker-compose logs web
docker-compose logs simulator
docker-compose logs mosquitto
docker-compose logs postgres
```

### Parar o projeto

```bash
docker-compose down
```

### Reconstruir os serviços

```bash
docker-compose build
docker-compose up -d
```

## 📈 Monitoramento

O simulador envia dados a cada 20 segundos com:
- Temperatura: entre 20°C e 30°C
- Umidade: entre 30% e 60%
- Device ID: "device123"
- Timestamp: Unix timestamp

Os dados são automaticamente salvos no PostgreSQL e podem ser consultados via API REST.

## 🔍 Troubleshooting

### Verificar conectividade MQTT

```bash
# Verificar se o Mosquitto está aceitando conexões
docker-compose logs mosquitto

# Verificar se o simulador está enviando dados
docker-compose logs simulator

# Verificar se a API está recebendo dados
docker-compose logs web
```

### Acessar banco de dados

```bash
# Conectar ao PostgreSQL
docker exec -it postgres-iot psql -U iotuser -d iot

# Verificar dados na tabela
SELECT * FROM telemetry ORDER BY timestamp DESC LIMIT 10;
```
