# Claude Code from your phone, with Puffin (Windows PowerShell). Same as the website installer:
#   $env:PUFFIN_SETUP_CODE="ABCDE-FGHJK"; irm https://raw.githubusercontent.com/justpuffin/claude-code-plugin/main/install.ps1 | iex
# Get the code on the agent's page in Puffin: Coding from your phone > Claude Code > Get setup command.
$ErrorActionPreference = "Stop"
Invoke-Expression (Invoke-RestMethod https://www.justpuffin.tech/install/claude-code.ps1)
