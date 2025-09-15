import os

DEFAULT_LLM = "custom"

LLM_CONFIG = {
    "hf_inference": {
        "provider": "huggingface",
        "model_name": "Helsinki-NLP/opus-mt-en-fr",  
        "device": "cpu", 
    },
    "hf_local": {
        "provider": "huggingface_local",
        "model_name": "Helsinki-NLP/opus-mt-en-fr",  
        "device": "cpu",
    },
    "gemini": {
        "provider": "gemini",
        "model": "gemini-pro",
        "api_key": os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_KEY"),  
    },
    "ollama": {
        "provider": "ollama",
        "model": "llama2", 
    },
    "custom": {
        "provider": "custom",
        "description": "Echo agent for testing purposes"
    }
}
