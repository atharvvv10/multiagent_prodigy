
from config import LLM_CONFIG

class OllamaAgent:
    def __init__(self):
        self.model = LLM_CONFIG["ollama"]["model"]

    def translate(self, text, source_lang="en", target_lang="fr"):

        return f"[Ollama-{self.model}] Translate from {source_lang} to {target_lang}: {text}"
