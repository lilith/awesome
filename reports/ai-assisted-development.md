# AI-assisted development

Most code here is written with frontier AI agents (Claude Code, Codex, Devin and others) running on six development machines with different CPUs and operating systems. The agents work under rules that keep the output checkable: `#![forbid(unsafe_code)]`, resource limits on every decoder, bit-exact tests against C reference implementations where they exist, continual fuzzing, and perceptual metrics where pixels may differ. Codex reviews designs and changes; [quality-and-security.md](quality-and-security.md) has the details.

| Measured | Value |
|---|---|
| Instructions sent to AI agents in 2026 (input-history entries, every agent and host) | 58,076 |
| Prompts lilith typed | 47,124 (729,119 words) |
| Unpaid hours on open source (the 20 minutes before each typed prompt, overlaps merged; a lower bound) | >2,798 |
| Tokens processed 2026-09-28 to 2026-10-26 (29 days of complete records, every agent) | 105.6B |

Prompt text is never kept: the inventory counts entries and words. Live figures and their scopes: [https://stats.lilith.now/](https://stats.lilith.now/).
