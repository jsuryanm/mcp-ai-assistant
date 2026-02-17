# MCP AI assistant tutorial project

A beginner-friendly project to learn how **MCP (Model Context Protocol)** works with LLMs using Groq + LangChain + MCP servers.

---

## 🚀 What This Project Does

This project creates a simple AI assistant that can:

* Chat using a Groq LLM
* Use MCP tools (browser, search, etc.)
* Remember conversation history
* Run in your terminal

It demonstrates how MCP **Host → Client → Server → Tool** works in practice.

---

## 🧠 MCP Architecture

```
User → MCP Agent → LLM (Groq)
                     ↓
               MCP Client
                     ↓
               MCP Servers
                     ↓
                  Tools
```

* **Host** → Your Python app
* **Client** → MCPClient
* **Server** → Playwright / Search MCP servers
* **Tools** → Browser automation, search, etc.

---

## 📦 Requirements

* Python 3.10 or 3.11
* Node.js (for MCP servers)
* Groq API key
* uv or pip package manager

---

## ⚙️ Installation

### 1. Clone the project

```bash
git clone <your-repo-url>
cd ai-assistant
```

### 2. Create virtual environment (uv recommended)

```bash
conda create --name mcp python=3.12
conda activate mcp
```

### 3. Install dependencies

```bash
 pip install -r requirements.txt
```

MCP servers are started automatically from `browser_mcp.json`.

---

## 🔑 Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python main.py
```

You will see an interactive chat like:

```
You: search web for python tutorial
Assistant: ...
```

Commands:

* `exit` → quit chat
* `clear` → clear memory

---

## 🧩 MCP Config File

Example `browser_mcp.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

You can add more MCP servers later.

---

## ⚠️ Common Issues

### 1. ModuleNotFoundError

Fix import paths:

```python
from langchain_groq import ChatGroq
```


### 2. Search or Airbnb MCP fails

Some MCP servers use scraping and may be blocked.
Use official APIs instead.

### 3. Token limit errors

Reduce:

* number of MCP tools
* conversation memory
* max_steps

---
