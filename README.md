# 🧠 GitHub Info MCP Tool

[![smithery badge](https://smithery.ai/badge/@AwaisKhizer/github-info-mcp)](https://smithery.ai/server/@AwaisKhizer/github-info-mcp)

This project is a **Model Context Protocol (MCP)** server that exposes tools for interacting with the GitHub API. It allows LLMs to fetch GitHub repository information, contributors, and latest commits via function calls.

## 🚀 Features

- Get basic repo information (stars, forks, issues, description)
- Get top contributors
- Get latest commit message
- Token support for authenticated API requests

## 🛠️ Technologies Used

- [Model Context Protocol (FastMCP)](https://github.com/modelcontextprotocol)
- Python 3.11+
- [httpx](https://www.python-httpx.org/) (Async HTTP requests)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (for `.env` support)

---

## 📦 Installation

### Installing via Smithery

To install github-info-mcp for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@AwaisKhizer/github-info-mcp):

```bash
npx -y @smithery/cli install @AwaisKhizer/github-info-mcp --client claude
```

### Manual Installation
```bash
git clone https://github.com/YOUR_USERNAME/github-info-mcp.git
cd github-info-mcp
pip install -r requirements.txt
```
