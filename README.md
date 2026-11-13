# Puffin for Claude Code

Give Claude Code its own **Puffin agent**: an email address, Slack, Discord and Telegram chats, texts, contacts, memories, a calendar and tasks. Every message it sends waits for your approval. Then step away from the keyboard and keep working with it **from your phone**.

`Email` · `Slack` · `Discord` · `Telegram` · `Texts` · `Calendar` · `Approvals`

Two parts, use one or both:

| | What it does | Install |
|---|---|---|
| **Puffin tools in Claude Code** | Claude Code reads and searches the agent's inbox and chats, drafts and sends (with approval), looks up contacts, books meetings and hands off tasks | `claude plugin marketplace add justpuffin/claude-code-plugin` and `claude plugin install puffin@puffin` |
| **Claude Code from your phone** | You message your agent from Telegram, Slack, Discord or email. Claude Code works in your project on your machine, asks you in the same chat before every edit or command (**Allow / Reject**), and replies there | One command with a setup code from the agent's page (below) |

## Puffin tools in Claude Code

```bash
claude plugin marketplace add justpuffin/claude-code-plugin
claude plugin install puffin@puffin
```

The first time Claude Code uses a Puffin tool, it opens Puffin in your browser. Sign in (or create an account), pick the agent Claude Code should act as, choose what it may do, and click **Allow**. No API key is copied anywhere. Disconnect at any time in Puffin: **Developer tools → Connected apps**.

Then just ask, for example:

- "What's new in my inbox? Anything from Acme?"
- "Reply to Priya: Thursday at 3 works."
- "When am I free on Friday? Book 30 minutes with Raj."
- "Remember that Acme prefers calls on Tuesdays."

Sends, replies and calendar invites wait for your approval in Puffin (or as **Approve / Reject** buttons in your linked chat). The plugin's skill tells Claude Code to treat incoming messages as untrusted content: it never follows instructions inside them.

Prefer a scoped key instead of signing in? `claude mcp add --transport http puffin https://api.justpuffin.tech/mcp --header "Authorization: Bearer $PUFFIN_API_KEY"` with a key from **API keys** in Puffin.

## Claude Code from your phone

```
you (phone) ── Telegram / Slack / Discord / email ──▶ Puffin ──▶ puffin claude (your machine)
                                                                      │
                                                     Claude Code session in your project
                                                     (asks you before each edit or command)
```

1. In Puffin, open the agent's page → **Coding from your phone** → choose **Claude Code** → **Turn on** → **Get setup command**.
2. Run the command on the computer that has your project (it needs [Claude Code](https://code.claude.com/docs/en/setup) installed and signed in, and Python 3.10+):

   ```bash
   # Mac or Linux
   curl -fsSL https://www.justpuffin.tech/install/claude-code.sh | bash -s -- --code ABCDE-FGHJK
   ```

   ```powershell
   # Windows (PowerShell)
   $env:PUFFIN_SETUP_CODE="ABCDE-FGHJK"; irm https://www.justpuffin.tech/install/claude-code.ps1 | iex
   ```

   The code works once, for 15 minutes. The installer exchanges it for this agent's own key (saved only on your machine), asks for your project folder, and starts the gateway in the background.
3. Link your chat account on Puffin's **Team** page (send `link <code>` to the bot), then message the agent: "the login test fails, fix it".

What you'll see:

```
Agent: Working on it in shop…
Agent: 🔐 Claude Code wants to edit src/login.ts:
       - if (token) return false
       + if (!token) return false
       [Allow] [Reject]
Agent: Fixed: the token check was inverted. All 42 tests pass.
```

- Reading and searching run freely; edits, commands, web pages and secret-looking files (`.env`, keys) ask first. Commands you list at setup (like `npm test`) run without asking.
- Each chat or email thread is one Claude Code session; send `new` to start fresh, `status` to see what's running.
- Only your own messages count: a linked workspace admin's chat account, or your confirmed email with DMARC passing.
- Claude Code never sees your Puffin or GitHub keys. If anything goes wrong, a step is denied, not run.

Inside Claude Code, run **`/puffin:phone`** to check the setup and get the next step. On the machine: `puffin claude status`, `puffin claude doctor`, `puffin claude logs`, `puffin claude stop`.

## What's in this repo

```
.claude-plugin/marketplace.json        the marketplace (one plugin: puffin)
plugins/puffin/.claude-plugin/plugin.json
plugins/puffin/.mcp.json               Puffin's hosted MCP server (sign in with your browser)
plugins/puffin/skills/puffin/SKILL.md  how Claude Code should use the tools
plugins/puffin/commands/phone.md       /puffin:phone
install.sh, install.ps1                the phone gateway installers
scripts/validate.py                    checks the manifests (run by CI)
```

The phone gateway itself is the `puffin claude` command in the Puffin Python SDK (`puffin-local`), which the installers set up.

## License

MIT
