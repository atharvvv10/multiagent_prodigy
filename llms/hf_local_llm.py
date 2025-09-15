from .base import BaseLLM
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class HFLocalLLM(BaseLLM):
    def __init__(self, model_name="gpt2", device=-1, **kwargs):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.device = "cuda" if device != -1 and torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def generate(self, prompt: str, max_length=100, **kwargs) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
 
