class BaseLLM:
    def __init__(self, **kwargs):
        pass

    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text from prompt"""
        raise NotImplementedError("Must implement generate method")
 
