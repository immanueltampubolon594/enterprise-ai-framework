import os
import logging
from typing import List, Dict, Any
from openai import OpenAI

logger = logging.getLogger(__name__)

class AsyncLLMClient:
    """Wrapper profesional untuk memanggil LLM dengan manajemen error & retry."""
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            logger.warning("OPENAI_API_KEY tidak ditemukan di environment variables!")
        self.client = OpenAI(api_key=self.api_key)

    def generate_chat(self, messages: List[Dict[str, str]], model: str = "gpt-4o-mini") -> str:
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Gagal menghasilkan respons LLM: {e}")
            raise RuntimeError(f"LLM Generation Error: {e}")