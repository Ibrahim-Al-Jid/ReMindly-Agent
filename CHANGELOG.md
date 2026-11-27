**English** | [العربية](CHANGELOG.ar.md)

# Changelog

## 2026-11-27: Fixes and documentation

**What was wrong**
- `pytest` crashed at import on a clean machine and in CI: the app validates settings on import and `MODEL_API_KEY` was missing. Every CI run on a fresh runner would fail.
- `requirements.txt` was saved as UTF-16, which many tools (editors, Dependabot, some deploy platforms) cannot read.
- The 1,360-line README had a long author section, links to an old GitHub account (`Al-Jid`) and a placeholder clone URL (`YOUR_USERNAME`).
- No Arabic documentation and no repository description or topics.

**Fixed**
- Added `tests/conftest.py` that sets a dummy key, so the suite runs anywhere with no real key. Result: 34 passed. `black`, `ruff` and `mypy` also pass.
- Converted `requirements.txt` to UTF-8. Installs cleanly on Python 3.12.
- All links point to `Ibrahim-Al-Jid/ReMindly-Agent`.

**Removed**
- The author and credit section.

**Added**
- Short `README.md` and `README.ar.md` with a language switch.
- `docs/guide.md`: the original full guide (architecture, full variable table, security, performance, roadmap).
- This changelog in English and Arabic.
- Repository About, topics and a social preview image.

## Original history (2026-08)

- 2026-08-12: first version, README improvements.
- 2026-08-13: production deployment preparation, UI and GitHub integration update, Vercel Python deployment fix.
