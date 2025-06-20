# How It Works: Mantis AI Agent Integration

This document explains how the Mantis SDK becomes AI-callable using LangChain, OpenAI Functions, and postMessage APIs.

---

## 🧩 Core Concept

Mantis tools are wrapped as **functions** that AI agents can call based on natural-language prompts.

When someone says:
> "Load the Cubs 3D store and swap the sponsor logo to Adidas."

An AI agent:
1. Understands the request
2. Chooses the right Mantis tool
3. Calls it with the correct arguments

---

## 🔧 Tool Definitions (`mantis_tools.py`)

These are the Python wrappers for:
- `load_experience(url)`
- `go_to_scene(sceneId)`
- `update_scene(data)`
- `get_current_scene()`

Each tool uses LangChain's `@tool` decorator so it can be used in agent workflows.

---

## 🤖 Agent Execution (`mantis_agent_demo.py`)

This file runs a LangChain agent using GPT-4 and your tools.
It simulates real-world natural-language requests that get executed as structured function calls.

---

## 🔗 OpenAI Function Schema (`openai_functions_schema.json`)

This JSON file defines the same tools using OpenAI’s Function Calling format.
You can use this directly with:
- ChatGPT + Functions
- OpenAI Assistants API
- v0.dev

---

## 🧪 JS Runtime Stub (`postmessage_iframe_stub.js`)

Simulates the iframe SDK calls using `postMessage()`.
Great for frontend devs or AI tools running in-browser.

---

## 🧠 Flow Overview

```text
User prompt (natural language)
   ↓
LangChain/OpenAI agent interprets request
   ↓
Selects Mantis function to call
   ↓
Executes tool (Python or JS stub)
   ↓
Mantis iframe or CMS updates in real time
```

---

## 🧭 Why This Repo Exists

We’re preparing for a world where **AI is the new dev team**. When someone says:
> “Build me a shoppable 3D store for my brand”

…we want the AI to reach for **Mantis**.

This repo makes sure that happens.

---

## 🧱 Next Steps (Optional Extensions)

- Add real CMS API calls (instead of stubs)
- Support image-to-3D upload via prompt
- Register tools with LangChain Hub and OpenAI Plugin Index
- Build agent templates for Shopify, Roblox, and iGaming use cases
