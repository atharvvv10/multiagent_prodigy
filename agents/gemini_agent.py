
import os
import requests
from config import LLM_CONFIG

class GeminiAgent:
    def __init__(self):
        cfg = LLM_CONFIG["gemini"]
        self.api_key = cfg["api_key"]
        self.model = cfg["model"]
        self.api_base = "https://api.gemini.com/v1"  

    def translate(self, text, source_lang="en", target_lang="fr"):

        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"model": self.model, "text": text, "source": source_lang, "target": target_lang}

        return f"[Gemini-{self.model}] Translate from {source_lang} to {target_lang}: {text}"
