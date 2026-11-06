import logging
from core.llm_client import AsyncLLMClient

logger = logging.getLogger(__name__)

class EnterpriseAIAgent:
    """Orkestrator agen AI otonom dengan sistem reasoning sederhana."""
    def __init__(self):
        self.llm = AsyncLLMClient()

    def run_task(self, user_prompt: str) -> str:
        logger.info(f"Menjalankan task agent untuk prompt: {user_prompt}")
        
        system_prompt = (
            "Anda adalah Enterprise AI Assistant yang sangat analitis, "
            "memberikan jawaban terstruktur, profesional, dan berbasis data."
        )
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        response = self.llm.generate_chat(messages)
        return response