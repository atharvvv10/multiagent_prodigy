# 📦 MultiProdigy AI Agents Framework - Phase 2
```bash
MultiProdigy is a **modular, schema-driven, multi-agent framework** built with **Pydantic**.  
It enables **scalable and orchestrated communication** between autonomous agents with a **shared message bus**, runtime engine, and support infrastructure.
```
---

## 🚀 Features
```bash
- Plugin-based architecture  
- Schema validation with Pydantic  
- Logging setup with configurable log file  
- Health checks for agent services  
- Service discovery for agents  
- Centralized error reporting  
- Dynamic schema registration system  
```
---

## 🧰 Phase 2 Enhancements
```bash
- Support for multiple LLM models: **Gemini Pro**, **Hugging Face**, **Custom LLMs**  
- Guidelines for integrating new/custom LLM agents  
- Modular folder structure for future scalability  
```
---

## 📄 Documentation
```bash
- **Getting Started**  
- **Architecture Overview**  
- **Module Reference**  
- **Sample Demo**  
```
---

## ⚡ Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/multiagent_prodigy.git
cd multiagent_prodigy

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
Usage
bash
Copy code
# Run CLI with Hugging Face model
python -m src.main "Hello World" --provider hf_inference

# Run CLI with Gemini Pro
python -m src.main "Hello World" --provider gemini

# Run CLI with Custom LLM
python -m src.main "Hello World" --provider custom
```
# 🤝 Contributing
```bash
If you want to contribute to the project:

Read our CODE OF CONDUCT first.

Fork the repository

Create a branch for your feature (git checkout -b feature/YourFeature)

Make changes and commit (git commit -m 'Add your message')

Push to your branch (git push origin feature/YourFeature)

Open a Pull Request
```
# 📌 Notes
```bash
Currently, OpenAI models are not integrated.

Gemini Pro requires an API key to function.

Hugging Face models can be run locally or via inference API.

Custom LLMs can be added by updating the config.py with their identifiers.
```

# 🛠️ License
```bash
This project is licensed under the MIT License.
```
