import os
from typing import Any
from dotenv import load_dotenv
import httpx
from mcp.server.fastmcp import FastMCP

load_dotenv()

# Init MCP
mcp = FastMCP("github-info", host="0.0.0.0", port=10000)
GITHUB_API_BASE = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Optional

headers = {
    "Accept": "application/vnd.github+json",
}
if GITHUB_TOKEN:
    headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# Internal GitHub request helper
async def github_get(path: str, params: dict[str, Any] = {}) -> dict[str, Any] | None:
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{GITHUB_API_BASE}/{path}", headers=headers, params=params)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print("GitHub API error:", e)
            return None

@mcp.tool()
async def get_repo_info(owner: str, repo: str) -> str:
    """Get basic info about a GitHub repo."""
    data = await github_get(f"repos/{owner}/{repo}")
    if not data:
        return "Failed to fetch repository info."

    return (
        f"📘 {data['full_name']}\n"
        f"⭐ Stars: {data['stargazers_count']}\n"
        f"🍴 Forks: {data['forks_count']}\n"
        f"🐞 Open Issues: {data['open_issues_count']}\n"
        f"📝 Description: {data.get('description', 'None')}"
    )

@mcp.tool()
async def get_contributors(owner: str, repo: str, top_n: int = 5) -> str:
    """Get top contributors of a repo."""
    data = await github_get(f"repos/{owner}/{repo}/contributors")
    if not data:
        return "Failed to fetch contributors."

    top = data[:top_n]
    return "\n".join([f"{c['login']} ({c['contributions']} commits)" for c in top])

@mcp.tool()
async def get_latest_commit(owner: str, repo: str) -> str:
    """Get the latest commit message from default branch."""
    data = await github_get(f"repos/{owner}/{repo}/commits")
    if not data:
        return "Failed to fetch commits."

    commit = data[0]["commit"]
    return f"🔀 {commit['message']} (by {commit['author']['name']})"

if __name__ == "__main__":
    mcp.run(transport="stdio")
