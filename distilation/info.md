# Distilation

Distilation is a project that leverages local ai infra to distil user's AI usage into compact summaries, key knowledge, and portable context portoflios that reflect the learning and familiar within specific knowledge domains due to AI use. This can either turn into 3 things: One, a tool to reduce the overstimulation of AI responses--a second second to review and focus on after. Two, a portable memory layer that shapes all future AI conversations. Or three, a new way to measure knowledge in an era defined by chatboxes--adjacent, parallel, or othongal to our current eduction system based on degrees.

**Key Features**

- Local Postgres Storage
- No Cloud Connection
- Local AI powers all summary and distillation
- Personalization on top of sematic search --> ranking turned into a small RL system that tunes per user

## Repo Structure

| File | Contents |
|---|---|
| `database.py` | Database config, table schemas, and `INSERT` / `SELECT` functions. |
| `summarize.py` | |
| `ai_client.py` | Model-agnostic AI client that sets up infrastructure for `runtime.call_ai()`, system prompts, and AI usage metrics such as token counts and TPS. |
| `local_stats.json` | Where local stats are stored, such as database metadata and AI usage statistics. |

