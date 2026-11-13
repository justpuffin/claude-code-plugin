"""Check the marketplace and plugin files before a release (run by CI and by hand: python scripts/validate.py)."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
problems = []


def load(path):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        problems.append(f"{path}: {error}")
        return {}


def frontmatter(path, keys):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        problems.append(f"{path.relative_to(ROOT)}: missing --- frontmatter")
        return
    for key in keys:
        if not re.search(rf"^{key}:\s*\S", match.group(1), re.M):
            problems.append(f"{path.relative_to(ROOT)}: frontmatter needs {key}")


market = load(".claude-plugin/marketplace.json")
for key in ("name", "owner", "plugins"):
    if key not in market:
        problems.append(f".claude-plugin/marketplace.json: missing {key}")
for entry in market.get("plugins", []):
    source = entry.get("source", "")
    if not isinstance(source, str) or ".." in source or not (ROOT / source).is_dir():
        problems.append(f"marketplace plugin {entry.get('name')}: source {source!r} is not a folder in this repo")
        continue
    manifest = load(pathlib.Path(source) / ".claude-plugin" / "plugin.json")
    if manifest.get("name") != entry.get("name"):
        problems.append(f"{source}: plugin.json name {manifest.get('name')!r} differs from the marketplace entry {entry.get('name')!r}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        problems.append(f"{source}: plugin.json version must look like 1.2.3")
    servers = load(pathlib.Path(source) / ".mcp.json").get("mcpServers", {})
    for name, server in servers.items():
        if not str(server.get("url", "")).startswith("https://"):
            problems.append(f"{source}/.mcp.json: server {name} must use an https:// URL")
        if "Authorization" in json.dumps(server):
            problems.append(f"{source}/.mcp.json: server {name} must not carry credentials")
    for skill in (ROOT / source / "skills").glob("*/SKILL.md"):
        frontmatter(skill, ("name", "description"))
    for command in (ROOT / source / "commands").glob("*.md"):
        frontmatter(command, ("description",))

if problems:
    print("\n".join("FAIL " + p for p in problems))
    sys.exit(1)
print("ok: marketplace, plugin manifest, MCP server, skills and commands")
