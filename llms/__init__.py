from .custom_llm import CustomLLM
from .gemini_llm import GeminiLLM
from .hf_inference_llm import HFInferenceLLM
from .hf_local_llm import HFLocalLLM

def get_llm(provider, config):
    providers = {
        "custom": CustomLLM,
        "gemini": GeminiLLM,
        "hf_inference": HFInferenceLLM,
        "hf_local": HFLocalLLM,
    }
    if provider not in providers:
        raise ValueError(f"Unknown provider: {provider}")
    return providers[provider](**config)
 
