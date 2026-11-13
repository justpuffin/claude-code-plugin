---
description: Set up or check Claude Code from your phone (message your Puffin agent from Telegram, Slack, Discord or email; Claude Code works in this project and asks before each edit or command)
allowed-tools: Bash(puffin claude status:*), Bash(puffin claude doctor:*), Bash(puffin --help:*), Bash(python3 -m pip show puffin-local:*), Bash(pip show puffin-local:*)
---

Help the user set up or check **Claude Code from your phone** for this project. It is Puffin's gateway (`puffin claude`): it turns the user's own messages to their Puffin agent into Claude Code sessions in a project folder, asks them in the same chat before every edit or command (Allow / Reject), and replies there.

Follow these steps and keep each reply short and plain.

1. Check whether the `puffin` command is installed: run `puffin --help`. If it is missing, tell the user to run the installer in their own terminal (not here, because it asks for their project folder). The installer comes with a one-time code from the agent's page in Puffin:
   - Mac or Linux: `curl -fsSL https://www.justpuffin.tech/install/claude-code.sh | bash -s -- --code <CODE>`
   - Windows (PowerShell): `$env:PUFFIN_SETUP_CODE="<CODE>"; irm https://www.justpuffin.tech/install/claude-code.ps1 | iex`

   To get the code, they open the agent's page in Puffin, go to **Coding from your phone**, choose **Claude Code**, click **Turn on**, then **Get setup command**. The code works once, for 15 minutes.
2. If `puffin` is installed, run `puffin claude status` and `puffin claude doctor`, then explain each `FIX` line in plain words, with the exact command or dashboard step to fix it.
3. If `puffin` is installed but not set up, tell them to run `puffin claude setup --code <CODE>` in their own terminal (it asks for the project folder and approval mode), then `puffin claude start`.
4. When everything is `ok`, tell them to message the agent from their phone, for example "what does this project do?", and that edits and commands will come as Allow / Reject prompts. In the chat, `new` starts a fresh session and `status` shows what's running.

Never ask the user to paste an API key or setup code into this conversation.
