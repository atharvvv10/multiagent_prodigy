# 🧠 MultiAgent Prodigy — LLM Translation Framework (Offline + Simulated)

-MultiAgent Prodigy is a modular Python framework to run and test multiple LLM clients for translation tasks — like Gemini Pro, HuggingFace (Offline mode), and Ollama — all in one place. Designed to work in environments without API keys or internet (offline-friendly). Supports simulation, real LLM outputs using local models, and is built to scale with multiple agents.

# 🚀 Features

-Plugin-based modular architecture for translation agents

-Schema validation using Pydantic

-Logging setup for task execution tracking

-CLI interface for quick testing

-Support for multiple LLMs: Gemini, HuggingFace (Offline), Ollama

-Fully offline-friendly and simulation-ready

-Expandable for future agents

# 📁 Folder Structure
```bash
multiagent_prodigy/
├── demo/
│   └── translation_demo.py         # Demo runner for all translation agents
├── agents/
│   ├── translator_agent.py         # Handles LLM translation calls
│   └── __init__.py
├── llm/
│   ├── clients.py                  # Gemini and Ollama clients (simulated/real)
│   └── huggingface_client.py       # HuggingFace offline translation
├── config.py                       # Config for LLMs and default settings
├── requirements.txt                # Required Python libraries
└── README.md                       # This file
```
# 💡 How It Works
🔷 Gemini Pro (Simulated)

-Simulated LLM client with optional API key support.

-Returns placeholder responses like:

-Simulated response from Gemini for: Hello World

🟡 HuggingFace (Offline)

-Fully offline using local transformer models (e.g., gpt2, distilgpt2).

-Translations generated with pipeline("text-generation", model=model_name).

-No internet or API key required; runs entirely locally.

🟢 Ollama (Real Local LLM)

-Runs real Ollama models such as tinyllama, mistral, or llama3.

-Requires Ollama installed and models pulled via CLI:

-ollama pull tinyllama

🧪 Demo File: demo/translation_demo.py
```bash
-The demo file runs all LLM clients sequentially for testing translations.

async def demo_gemini():       # Simulated Gemini translation
async def demo_huggingface():  # Offline HuggingFace translation
async def demo_ollama():       # Real Ollama translation
```
```bash
Run the demo:

-PYTHONPATH=. python demo/translation_demo.py
```

# Expected output:
```bash
🔷 Gemini Response: Simulated response from Gemini for: Hello World
🟡 HuggingFace (Offline) Response: Bonjour le monde
🟢 Ollama Response: Bonjour le monde (real LLM output)
✅ All translation agents ran successfully!
```
# 🧠 LLM Clients Overview
```bash
llm/clients.py

-GeminiClient – Simulated, returns placeholder translations; API key optional.

-OllamaClient – Calls ollama run via subprocess to use local models.

-llm/huggingface_client.py

-Offline LLM using HuggingFace transformers library.
```
```bash
Example usage:

-from transformers import pipeline

self.generator = pipeline("text-generation", model="gpt2")
translation = self.generator("Hello World", max_length=50)
```
# ▶️ Step-by-Step Setup
```bash
Clone or set up the folder structure.

Install dependencies:
pip install -r requirements.txt

Install Ollama (if using OllamaClient):
https://ollama.com/download
Pull the required Ollama model:
ollama pull tinyllama

Run the demo:

PYTHONPATH=. python demo/translation_demo.py
```
# ✅ Offline vs Online Behavior

GeminiClient	✅ Yes	Simulated 

HuggingFaceClient	✅ Yes	Fully offline using local models

OllamaClient	✅ Yes	Runs real local models via CLI

# ⚡ Key Advantages

-Test multiple LLMs locally without paying for APIs

-Fully offline-friendly and simulation-ready

-Modular architecture allows adding more agents easily

-Logging ensures reproducible testing and debugging

-Scalable: Can expand to include translation, summarization, or other tasks

# 📌 Notes

-HuggingFace models require local download; no internet needed for inference.

-Ollama models are real and local, using CLI commands.

-Gemini and other simulated clients return predefined responses for testing purposes.

-CLI-first design allows easy integration with pipelines or future APIs.
