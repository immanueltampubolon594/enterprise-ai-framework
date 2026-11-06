import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.agent import EnterpriseAIAgent

logger = logging.getLogger(__name__)
router = APIRouter()
agent = EnterpriseAIAgent()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    status: str
    response: str

@router.post("/v1/agent/run", response_model=PromptResponse)
def run_agent_task(payload: PromptRequest):
    """Endpoint utama untuk memicu AI Agent menjalankan tugas."""
    if not payload.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt tidak boleh kosong.")
    
    try:
        result = agent.run_task(payload.prompt)
        return {"status": "success", "response": result}
    except Exception as e:
        logger.error(f"API Error pada Agent Run: {e}")
        raise HTTPException(status_code=500, detail=str(e))