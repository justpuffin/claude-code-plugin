# Puffin

Puffin gives Claude Code its own agent identity: an email address, Slack, Discord and Telegram chats, texts, contacts, memories, a calendar and tasks. Claude Code can read and search the agent's messages, draft and reply, look up contacts, check free times and book meetings. Every message, reply and calendar invite it sends waits for your approval in Puffin, or as Approve / Reject buttons in your linked chat.

**Install:** `/plugin install puffin --marketplace justpuffin/claude-code-plugin` (or `claude plugin marketplace add justpuffin/claude-code-plugin`, then `claude plugin install puffin@puffin`).

**Setup:** after installing, the first Puffin tool call opens Puffin in your browser. Sign in, pick the agent, choose what Claude Code may do and click Allow. No API key is copied. Disconnect any time in Puffin under Developer tools, Connected apps.

**From your phone:** run `/puffin:phone` to set up Claude Code from your phone. You message your agent from Telegram, Slack, Discord or email, and Claude Code works in your project on your machine, asking you in the same chat before each edit or command.
