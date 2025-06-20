# Mantis AI Integration Kit

Mantis makes 3D commerce simple—no Blender, no plugins, no dev time.  
This repo makes Mantis **AI-callable** from tools like LangChain, GPT-4o, Cursor, and v0.dev.

> "Build a 3D storefront with Mantis" — now works from a prompt.

---

## 🧠 What This Repo Is

This is the official SDK for integrating Mantis with AI agents. It includes:

- ✅ LangChain tool definitions (`mantis_tools.py`)
- ✅ A working LangChain agent demo (`mantis_agent_demo.py`)
- ✅ OpenAI Function schema (`openai_functions_schema.json`)
- ✅ JS postMessage stubs for iframe control (`postmessage_iframe_stub.js`)
- ✅ Example prompts, use cases, and setup docs

---

## 🏁 Quickstart

### 1. Clone this repo and install dependencies:

```bash
git clone https://github.com/mantisxr/mantis-ai-integration.git
cd mantis-ai-integration
pip install -r requirements.txt
