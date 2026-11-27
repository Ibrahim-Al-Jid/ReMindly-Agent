**English** | [العربية](README.ar.md)

# ReMindly Agent

Turn raw explanations, lecture notes and technical text into clean, structured Markdown with an AI pipeline: generate, validate, review, retry.

FastAPI backend, a plain HTML/JS front end with live streaming, any OpenAI-compatible model.

## What it does

- Organizes unstructured text into headings, lists, tables and code blocks without changing the meaning.
- Streams progress and output live over Server-Sent Events.
- Detects Arabic, English or mixed input and checks the output language.
- Splits long input into chunks and processes them in parallel.
- Validates the generated Markdown, then runs a separate AI quality review and one retry if needed.
- Modes and detail levels: short, medium, detailed, preserve. Optional custom instruction.
- Preview, copy and download as `.md`.

```text
Raw text -> chunking -> generation -> validation -> quality review -> Markdown
```

## Quick start

Requires Python 3.12.

```bash
git clone https://github.com/Ibrahim-Al-Jid/ReMindly-Agent.git
cd ReMindly-Agent
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # set MODEL_API_KEY
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000.

## Configuration

Main variables (full table in [docs/guide.md](docs/guide.md)):

| Variable | Default | Purpose |
|---|---|---|
| `MODEL_API_KEY` | none | Key for the AI provider (required for generation) |
| `MODEL_BASE_URL` | `https://openrouter.ai/api/v1` | OpenAI-compatible endpoint |
| `MODEL_NAME` | `nvidia/nemotron-3-super-120b-a12b:free` | Model to use |
| `APP_API_KEY` | empty | Optional `X-API-Key` protection for the API |
| `ORGANIZE_RATE_LIMIT` / `STREAM_RATE_LIMIT` | `10/minute` / `5/minute` | Rate limits |

Keys stay on the server. Never commit `.env`.

## API

| Method | Path | Description |
|---|---|---|
| GET | `/api/health` | Service status |
| POST | `/api/organize` | Organize text, JSON response |
| POST | `/api/organize/stream` | Same, streamed as SSE (`progress`, `token`, `replace`, `completed`, `error`) |

```json
{ "text": "Raw text to organize...", "instruction": "optional", "mode": "balanced",
  "language": "english", "detail_level": "medium" }
```

## Tests and checks

```bash
pytest          # 34 tests, no real model calls, no key needed
black --check app tests
ruff check app tests
mypy app
```

All four pass. CI runs them on every push.

## Docker and Vercel

```bash
docker build -t remindly-agent .
docker run -p 8000:8000 --env-file .env remindly-agent
```

Vercel is configured through `vercel.json` and `index.py`. Details in [docs/guide.md](docs/guide.md).

## Structure

```text
app/        FastAPI app: api, core (config, security, rate limit), services, models
static/     web interface
tests/      pytest suite
docs/       extended guide
```
