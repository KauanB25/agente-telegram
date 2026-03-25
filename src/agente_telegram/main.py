import uvicorn


def start_api():
    uvicorn.run(
        app="agente_telegram.app:app",
        host="0.0.0.0",
        port=8000
    )

if __name__ == "__main__":
    start_api()
