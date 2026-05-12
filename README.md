# Maria - Agente de Inglês no Telegram

Bot do Telegram que atua como tutora de inglês chamada **Maria**. Utiliza o modelo **Google Gemini 2.5 Flash** para manter conversas contextuais, corrigir erros gramaticais e traduzir frases, com histórico persistido em PostgreSQL.

## Funcionalidades

- **Chat com IA** — Conversas em inglês com correção gramatical automática e traduções quando o usuário escreve em português
- **Histórico persistente** — O contexto da conversa é salvo em JSONB no banco, permitindo continuidade entre sessões
- **Cadastro de usuários** — Registro automático via `/start` com verificação por número de telefone
- **Reset de conversa** — Comando `/reset` para limpar o histórico e recomeçar
- **Reengajamento automático** — Job agendado (diário às 8h) que notifica usuários inativos há mais de 2 dias
- **Webhook e Polling** — Suporte a ambos os modos de operação do Telegram

## Tech Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12+ |
| Gerenciador de pacotes | Poetry |
| Bot Telegram | pyTelegramBotAPI |
| API Web | FastAPI + Uvicorn |
| IA Generativa | Google GenAI (Gemini 2.5 Flash) |
| ORM | SQLAlchemy 2.x |
| Banco de dados | PostgreSQL |
| Migrações | Alembic |
| Agendamento | APScheduler |
| Configuração | Pydantic Settings |

## Estrutura do Projeto

```
agente-telegram/
├── alembic/                          # Migrações do banco de dados
│   └── versions/
├── scripts/
│   └── set_webhook.py                # Configuração do webhook do Telegram
└── src/agente_telegram/
    ├── main.py                       # Entrypoint (uvicorn)
    ├── app.py                        # App FastAPI com rota /webhook
    ├── bot.py                        # Handlers do bot (mensagens, comandos)
    ├── config/
    │   └── settings.py               # Variáveis de ambiente via pydantic-settings
    ├── model/
    │   ├── users_telegram.py         # Modelo de usuários
    │   └── users_history.py          # Modelo de histórico (JSONB)
    ├── service/
    │   ├── google_ai.py              # Integração com Google Gemini
    │   ├── user_telegram.py          # CRUD de usuários
    │   └── users_history.py          # CRUD de histórico + query de inativos
    ├── util/
    │   ├── engine_postgre.py         # Factory de engine SQLAlchemy
    │   └── get_session.py            # Context manager de sessão
    └── jobs/
        └── inactive_user.py          # Job de notificação de usuários inativos
```

## Pré-requisitos

- Python >= 3.12
- [Poetry](https://python-poetry.org/) instalado
- PostgreSQL rodando e acessível
- Token de bot do Telegram (via [@BotFather](https://t.me/BotFather))
- Chave de API do [Google Gemini](https://ai.google.dev/)

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
TOKEN_TELEGRAM=123456:ABC-DEF...
DB_POSTGREE_USER=postgres
DB_POSTGREE_PASSWORD=sua_senha
DB_POSTGREE_DATABASE=agente_telegram
GOOGLE_GEMINI_API_KEY=AIza...
URL_WEBHOOK=https://seu-dominio.com/webhook
```

Variáveis opcionais (possuem valor padrão):

| Variável | Default | Descrição |
|---|---|---|
| `db_postgree_host` | `localhost` | Host do PostgreSQL |
| `DB_POSTGREE_PORT` | `5432` | Porta do PostgreSQL |

## Instalação

```bash
# Instalar dependências
poetry install

# Executar migrações do banco
poetry run alembic upgrade head
```

## Execução

```bash
# Modo webhook (FastAPI/Uvicorn na porta 8000)
poetry run api

# Modo polling
poetry run service
```

Para configurar o webhook do Telegram:

```bash
poetry run python scripts/set_webhook.py
```
