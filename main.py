import logging
import sys
import argparse
from agents.translator_agent import TranslatorAgent

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] ProdigalAI - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("ProdigalAI")


def main():
    parser = argparse.ArgumentParser(description="MultiProdigy Translator CLI")
    parser.add_argument("text", type=str, help="Text to translate")
    parser.add_argument("--source", type=str, default="en", help="Source language")
    parser.add_argument("--target", type=str, default="fr", help="Target language")
    parser.add_argument("--provider", type=str, default=None,
                        choices=["hf_inference", "hf_local", "gemini", "ollama", "custom"],
                        help="LLM provider to use")
    args = parser.parse_args()

    agent = TranslatorAgent(provider=args.provider)

    translation = agent.translate(args.text, source=args.source, target=args.target)

    logger.info(f"Translate from {args.source} to {args.target}: {translation}")
    print(translation)


if __name__ == "__main__":
    main()
