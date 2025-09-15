import requests

class GeminiTranslator:
    def __init__(self, cfg):
        self.api_key = cfg["api_key"]
        self.model = cfg["model"]

    def translate(self, text, source="en", target="fr"):
        url = "https://api.gemini.com/v1/generate"  
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {
            "model": self.model,
            "prompt": f"Translate from {source} to {target}: {text}",
            "max_tokens": 256
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()["text"]
