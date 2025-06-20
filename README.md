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

Create a .env file with your OpenAI key based on .env.example

2. Run the LangChain agent demo
python mantis_agent_demo.py
The agent will simulate a natural-language request to load a 3D experience and update its content.

🧱 Available Tools (MCP Spec)
Tool	Description
load_experience	Load a Mantis storefront by URL
go_to_scene	Navigate to a specific scene
update_scene	Dynamically update scene content (logo, video)
get_current_scene	Return the active scene ID

🔗 OpenAI Function Calling
You can also plug openai_functions_schema.json directly into:

GPT-4o agents

v0.dev workflows

OpenAI Assistant APIs

🧪 Examples
See /examples/sneaker_store_prompt.md for natural-language use cases like:

“Load the Cubs 3D store and swap the sponsor logo to Adidas.”

📚 Docs
See /docs/how-it-works.md for a step-by-step breakdown of how the agent and tools work together.

👀 What’s Coming
Full CMS API integration

Live iframe demo + hosted preview

Shopify/Roblox/Amazon-specific agent starters

🔒 License
MIT. Use, remix, and build with it.

💬 Questions?
Visit mantisxr.com
