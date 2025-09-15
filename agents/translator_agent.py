import os
import logging


from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


import requests  

from config import LLM_CONFIG, DEFAULT_LLM

logger = logging.getLogger("ProdigalAI")


class TranslatorAgent:
    def __init__(self, provider=None):
        self.provider_name = provider or DEFAULT_LLM
        if self.provider_name not in LLM_CONFIG:
            logger.warning(f"{self.provider_name} not found in config. Falling back to default.")
            self.provider_name = DEFAULT_LLM

        self.cfg = LLM_CONFIG[self.provider_name]
        self.provider = self.cfg["provider"]

        logger.info(f"TranslatorAgent initialized with {self.provider_name}")

        if self.provider.startswith("hf"): 
            self.tokenizer = AutoTokenizer.from_pretrained(self.cfg["model_name"])
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.cfg["model_name"])

        elif self.provider == "gemini":
            self.api_key = self.cfg.get("api_key")
            self.model_name = self.cfg.get("model")

        elif self.provider in ["ollama", "custom"]:
            pass
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def translate(self, text, source="en", target="fr"):
        if self.provider.startswith("hf"):
            input_ids = self.tokenizer.encode(text, return_tensors="pt")
            outputs = self.model.generate(input_ids)
            translated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return translated

        elif self.provider == "gemini":
          
            return f"[Gemini-{self.model_name}] Translate from {source} to {target}: {text}"

        elif self.provider == "ollama":

            return f"[Ollama-llama2] Translate from {source} to {target}: {text}"

        elif self.provider == "custom":

            return f"[Custom Echo] Translate from {source} to {target}: {text}"

        else:
            raise ValueError(f"Unsupported provider: {self.provider}")
