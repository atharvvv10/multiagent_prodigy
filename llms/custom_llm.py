from .base import BaseLLM

class CustomLLM(BaseLLM):
    def generate(self, prompt: str, **kwargs) -> str:
        return f"[Custom Echo] {prompt}"
 
