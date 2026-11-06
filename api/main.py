import uvicorn
import logging
from fastapi import FastAPI
from api.routes import router

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Enterprise AI Agent System",
    version="1.0.0",
    description="Production-ready microservices architecture for AI Agents and RAG systems."
)

# Daftarkan router API
app.include_router(router, prefix="/api")

@app.get("/health")
def health_check():
    """Endpoint untuk health check container/server."""
    return {"status": "healthy", "service": "ai-agent-system"}

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)