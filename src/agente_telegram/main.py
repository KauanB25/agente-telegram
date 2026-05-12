"""Entrypoint para inicialização da API via Uvicorn."""

import uvicorn


def start_api():
    """Inicia o servidor Uvicorn com a aplicação FastAPI na porta 8000."""
    uvicorn.run(
        app="agente_telegram.app:app",
        host="0.0.0.0",
        port=8000
    )

if __name__ == "__main__":
    start_api()
