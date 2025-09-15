from .base import BaseLLM
from transformers import pipeline

class HFInferenceLLM(BaseLLM):
    def __init__(self, hf_api_token=None, model_id="gpt2", **kwargs):
        self.generator = pipeline("text-generation", model=model_id, tokenizer=model_id)

    def generate(self, prompt: str, **kwargs) -> str:
        output = self.generator(prompt, max_length=100)
        return output[0]["generated_text"]
 
