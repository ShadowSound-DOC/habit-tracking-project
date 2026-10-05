# Habit Tracking Project (Pixela)

Logs daily coding hours to a Pixela graph.

## Setup
1. Copy `.env.example` → `.env` and set `PIXELA_TOKEN`, `PIXELA_USERNAME` (and optional `PIXELA_GRAPH_ID`).
2. `pip install requests python-dotenv`
3. Uncomment the one-time user/graph creation lines in `main.py` if the account/graph does not exist yet.

## Run
```
python main.py
```
