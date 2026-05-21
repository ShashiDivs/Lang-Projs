# proj-langchain

A LangChain project with support for Anthropic, Google Gemini, Groq, and OpenAI models — managed with [uv](https://docs.astral.sh/uv/).

---

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

---

## 1. Install uv

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, restart your terminal or run:

```bash
source $HOME/.local/bin/env
```

Verify:

```bash
uv --version
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart your terminal, then verify:

```powershell
uv --version
```

---

## 2. Clone & Navigate to the Project

```bash
git clone <your-repo-url>
cd proj-langchain
```

---

## 3. Create a New Project with uv (first-time setup only)

> Skip this step if you cloned an existing repo — a `pyproject.toml` is already present.

```bash
uv init proj-langchain
cd proj-langchain
```

This creates a `pyproject.toml` and a basic project structure.

---

## 4. Create the Virtual Environment

uv automatically creates a `.venv` when you sync or add a package. To create it explicitly:

```bash
uv sync
```

This reads `pyproject.toml` and `uv.lock`, creates `.venv/`, and installs all dependencies.

---

## 5. Add Dependencies

```bash
uv add langchain langchain-anthropic langchain-openai langchain-google-genai langchain-groq python-dotenv
```

uv updates `pyproject.toml` and `uv.lock` automatically. No `pip install` needed.

---

## 6. Activate the Virtual Environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

Deactivate when done:

```bash
deactivate
```

> **Tip:** With `uv run`, you can skip activation entirely — uv will use the project's venv automatically.

---

## 7. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# macOS / Linux
touch .env
```

```powershell
# Windows PowerShell
New-Item -Path .env -ItemType File
```

Add your API keys to `.env`:

```env
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_google_key_here
GROQ_API_KEY=your_groq_key_here
```

> `.env` is loaded automatically via `python-dotenv`. Never commit this file — add it to `.gitignore`.

---

## 8. Run Scripts

### With virtual environment activated

```bash
python main.py
python chat_models.py
```

### Without activating (using uv run)

```bash
uv run main.py
uv run chat_models.py
```

---

## Project Structure

```
proj-langchain/
├── .venv/                  # Virtual environment (auto-created by uv)
├── .env                    # API keys — do NOT commit
├── pyproject.toml          # Project metadata & dependencies
├── uv.lock                 # Locked dependency versions
├── main.py
├── chat_models.py          # Basic chat model examples
├── chat_models_stream.py   # Streaming responses
├── chat_models_multi.py    # Multiple models
├── chat_anthro.py          # Anthropic (Claude) examples
├── chat_gemini.py          # Google Gemini examples
└── chat_groq.py            # Groq examples
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `langchain` | Core LangChain framework |
| `langchain-anthropic` | Claude (Anthropic) integration |
| `langchain-openai` | OpenAI integration |
| `langchain-google-genai` | Google Gemini integration |
| `langchain-groq` | Groq integration |
| `langchain-community` | Community integrations |
| `python-dotenv` | Load `.env` variables |
| `ipykernel` | Jupyter notebook support |

---

## Common uv Commands

| Command | Description |
|---|---|
| `uv sync` | Install all dependencies from lock file |
| `uv add <package>` | Add a new dependency |
| `uv remove <package>` | Remove a dependency |
| `uv run <script>` | Run a script in the project venv |
| `uv pip list` | List installed packages |
| `uv lock` | Regenerate the lock file |
