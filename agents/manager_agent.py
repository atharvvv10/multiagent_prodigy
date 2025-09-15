from logger import logger
from .translator_agent import TranslatorAgent

class ManagerAgent:
    """Pipeline agent managing multiple sub-agents"""

    def __init__(self):
        logger.info("ManagerAgent initialized")
        self.translator = TranslatorAgent()

    def run_pipeline(self, text):
        logger.info("ManagerAgent running pipeline")
        translated = self.translator.run(text)
        return translated
 
