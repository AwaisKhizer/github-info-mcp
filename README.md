# 🧠 GitHub Info MCP Tool

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

```bash
git clone https://github.com/YOUR_USERNAME/github-info-mcp.git
cd github-info-mcp
pip install -r requirements.txt
