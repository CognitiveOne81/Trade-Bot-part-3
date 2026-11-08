# Trade-Bot-part-3
Using Codex to auto trade

## Alpaca paper-trading setup

This repository intentionally does not store API credentials. Keep paper-trading
keys in a local `.env` file, which is excluded from Git.

```powershell
Copy-Item .env.example .env
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python account_status.py
```

Edit `.env` locally before running the final command. Use paper-account keys only.
