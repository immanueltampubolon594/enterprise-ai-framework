import json
import re
from typing import Dict, Any, Optional

class LLMJsonParser:
    """
    Utility kelas untuk mengekstrak dan memvalidasi format JSON 
    dari output teks LLM yang seringkali berantakan.
    """
    
    @staticmethod
    def extract_json(llm_response: str) -> Optional[Dict[str, Any]]:
        try:
            return json.loads(llm_response)
        except json.JSONDecodeError:
            pass

        match = re.search(r'```(?:json)?\s*({.*?})\s*```', llm_response, re.DOTALL)
        if match:
            json_str = match.group(1)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass

        match_fallback = re.search(r'\{.*\}', llm_response, re.DOTALL)
        if match_fallback:
            json_str = match_fallback.group(0)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass

        return None

if __name__ == "__main__":
    messy_response = """
    Tentu, ini adalah hasil analisis data Anda:
    ```json
    {
        "status": "success",
        "confidence_score": 0.95,
        "tags": ["ai", "engineering", "python"]
    }
    ```
    Semoga membantu!
    """
    parsed_data = LLMJsonParser.extract_json(messy_response)
    print("Parsed Result:", parsed_data)