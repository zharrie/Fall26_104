# Local RAG classroom demo

A small, runnable demonstration of retrieval-augmented generation (RAG) for the
final mini project. The program reads fictional records from
`data/garden_records.csv`, retrieves the most relevant rows using Python
keyword matching, and asks a **local** Ollama model to answer using only those
rows. It prints the cited record IDs with the answer. If Ollama is unavailable,
it tells you the local model could not be reached.

It shows the two things the handout asks for:

- **Ask questions** about a local file ("What greenhouse maintenance is still
  pending?") and get a grounded, cited answer.
- **Summarize** the whole file in one command (`--summarize`, or type
  `summarize`).

Everything runs on your machine using only the Python standard library plus a
local Ollama model — no API keys, no cloud services.

This is a demo of the RAG portion of the handout, not a complete
capstone submission: it does not implement the required menu-driven application,
classes/inheritance, persistence, algorithms.

## What is RAG?

**RAG** stands for **Retrieval-Augmented Generation**. It is a simple idea:
instead of trusting a language model to answer from memory (where it can
confidently make things up), you first **retrieve** the relevant facts from
*your own files* and then ask the model to **generate** an answer using *only*
those facts.

Think of it as an open-book exam for the model:

- **Without RAG:** "Answer this from memory." → The model may guess or invent.
- **With RAG:** "Here are the 3 records that matter — answer using only these,
  and cite them." → The answer is grounded in your data and checkable.

Your program stays in charge: *your Python code* decides which records are
relevant (the retrieval step), and the model only rephrases and summarizes what
you handed it (the generation step). This is why the model is never the "source
of truth" — your files are.

The pipeline this demo follows:

```text
Your question
      │
      ▼
[1] LOAD      read data/*.csv into a list of records (each with an ID)
      │
      ▼
[2] RETRIEVE  plain Python ranks records by keyword overlap, keeps the top few
      │
      ▼
[3] GENERATE  send ONLY the question + those records to the local model
      │        (POST http://localhost:11434/api/generate — Ollama, on your machine)
      ▼
[4] ANSWER    print the reply and the IDs it used: "Sources: G-002, G-016"
```

**The rule that matters most:** if the retrieved records do not contain the
answer, the assistant must say so instead of inventing one. This demo shows that
by refusing to call the model when nothing matches, and by instructing the model
to reply `NOT_IN_SOURCES` when the records do not support an answer.

## What you need

- Python 3.9 or later. No third-party Python packages are used.
- Ollama and a local model for the live AI part. The demo's default is
  `qwen3:1.7b` (about 1.4 GB to download; first response may take longer).
- Internet access once to download Ollama and the model. After that, the model
  and demo run locally.

## Install Ollama

Use the official download page: <https://ollama.com/download>. Choose the
installer for your operating system. Ollama's installer and menus may change;
follow any current prompts shown by the official installer.

### macOS

1. Download the macOS version from <https://ollama.com/download>.
2. Open the downloaded `.dmg` and drag **Ollama** into **Applications** if
   prompted.
3. Open **Ollama** from Applications. Approve the macOS security prompt if one
   appears, and allow the app to run in the menu bar. This starts the local
   Ollama service.
4. Open **Terminal** and download/start the class model:

   ```sh
   ollama run qwen3:1.7b
   ```

5. Wait for the model download, then type a short test question. At the Ollama
   prompt, type `/bye` to exit the chat. Keep Ollama running in the background.
6. Verify it is installed:

   ```sh
   ollama list
   ```

### Windows

1. Download the Windows installer from <https://ollama.com/download>.
2. Run the downloaded installer and follow its prompts.
3. Launch **Ollama** from the Start menu. It runs in the background (look for
   its tray icon).
4. Open **PowerShell** and download/start the class model:

   ```powershell
   ollama run qwen3:1.7b
   ```

5. Wait for the model download, then type a short test question. At the Ollama
   prompt, type `/bye` to exit the chat. Leave Ollama running in the background.
6. Verify it is installed:

   ```powershell
   ollama list
   ```

The first model download is roughly 1.4 GB and can take several minutes. Check
available disk space and your computer's memory before class. If `qwen3:1.7b`
is too slow or does not fit, download the lighter handout alternative:

```sh
ollama pull gemma3:1b
```

Then pass `--model gemma3:1b` when running the demo. The local Ollama API is
normally available at `http://localhost:11434`; this demo sends requests only
to that address and needs no API key.

## Run and manage Ollama

Ollama runs as a small background service (the menu-bar app on macOS, the tray
app on Windows). These are the only commands you need. They are the same in
macOS Terminal and Windows PowerShell:

| Command | What it does |
| --- | --- |
| `ollama run qwen3:1.7b` | Download (first time) and chat with the model directly. Type `/bye` to leave that chat. |
| `ollama list` | Show which models are installed. |
| `ollama ps` | Show whether a model is currently loaded in memory. |
| `ollama pull qwen3:1.7b` | Download a model without starting a chat. |
| `ollama serve` | Start the local service manually if the app is not running. |

**Starting Ollama:** launch the Ollama app (macOS menu bar / Windows tray), or
run `ollama serve`. You do **not** need `ollama run` open to use this demo — the
demo talks to the background service on its own.

**Stopping Ollama:** quit the app from its menu-bar / tray icon. (Stopping it is
useful for demonstrating how the demo reports the model as unavailable — see the
walkthrough below.)

## Run the demo

Open Terminal (macOS) or PowerShell (Windows), change directory to this project
folder, and run:

```sh
# macOS
python3 demo_rag.py

# Windows
py demo_rag.py
```

Interactive mode lets you ask multiple questions about the same CSV. Each
question is independent; the demo does not retain chat history. Type
`summarize` for a whole-file overview, or `quit`/`exit` to end the session. Try
questions such as:

```text
Summarize the open irrigation issues
What greenhouse maintenance is still pending?
What happened in compost bay one?
```

To ask one question and exit:

```sh
python3 demo_rag.py --question "Summarize the open irrigation issues"
```

```powershell
py demo_rag.py --question "Summarize the open irrigation issues"
```

To summarize the entire file and exit:

```sh
python3 demo_rag.py --summarize
```

```powershell
py demo_rag.py --summarize
```

To use the lighter model, add `--model gemma3:1b` to any of the commands above:

```sh
python3 demo_rag.py --model gemma3:1b
```

```powershell
py demo_rag.py --model gemma3:1b
```

When the demo starts it loads the records and waits for your question. If Ollama
is not running, it tells you the local model is unavailable instead of inventing
an answer.

## What the code does

The whole program is about 200 lines of commented Python, meant to be read
top to bottom:

1. **Load** (`load_records`) — reads every `.csv` file under `data/` with
   Python's standard-library `csv.DictReader`. Each row becomes one record; the
   `record_id` column (or `id`) supplies its citation.
2. **Retrieve** (`retrieve`) — scores every record by how many keywords it
   shares with the question, drops the zero-overlap records, and keeps the top
   three. This is intentionally simple, visible Python — not a vector database
   or embeddings.
3. **Generate** (`build_prompt` + `generate`) — POSTs the question plus only the
   retrieved records to Ollama's local `/api/generate` endpoint with
   `urllib`, and returns the answer. Summarize mode sends every record and asks
   for a cited overview.
4. **Show** (`ask_model`) — prints the retrieved record IDs, then the model's
   answer, then the sources it used. If no records match, the model is not
   called. If Ollama is stopped, it reports that the local model is unavailable.

For visibility into Ollama itself on macOS, open a second Terminal and run
`tail -f ~/.ollama/logs/server.log`. On Windows, open the Ollama logs with
`explorer %LOCALAPPDATA%\Ollama`; the current server log is `server.log`.
`ollama ps` shows whether a model is loaded. You do not need to open
`http://localhost:11434` in a browser.

The generated text is model output, not verified fact. Review it against the
cited fictional CSV rows. Do not put private or sensitive information in the
demo data or prompts.

## Use your own local CSV

To try a student's own data, place a **fictional or otherwise safe** `.csv`
file in `data/`. Include a stable `record_id` column (or `id`); each row becomes
a source the retriever can cite. Keep useful descriptive values in the other
columns, such as status, category, date, or notes. The loader reads every CSV
in that folder. Restart the demo after editing or adding files.

For example, a task manager could write:

```csv
record_id,title,status,due_date,details
TASK-001,Prepare slides,open,2026-10-20,Add a diagram of the local RAG pipeline
```

Then ask about matching titles, statuses, or details. The current retriever is
simple keyword overlap: phrase questions using words that appear in the CSV.
For privacy, keep real personal, medical, financial, or student records out of
the demo; local execution does not make sensitive classroom data appropriate
for prompts.

## Troubleshooting

- **`ollama` is not recognized / command not found:** Open the Ollama app, then
  open a new Terminal or PowerShell window. If it persists, follow the
  installation troubleshooting guidance at <https://ollama.com/download>.
- **Connection refused or model unavailable:** Start the Ollama app and check
  `ollama list`. If needed, run `ollama pull qwen3:1.7b`. You can also start
  the local service manually with `ollama serve`.
- **Slow or out of memory:** Try `gemma3:1b` with `--model gemma3:1b`.
- **No matching CSV records:** Rephrase using terms present in the sample
  values, or open `data/` and edit/add fictional records. Retrieval is keyword
  based, so it may not match semantically related wording.

## What this project expects (through RAG)

This demo shows the RAG *pattern*; your mini project must build a complete
application around it. Use the demo to understand the AI assistant piece, then
meet the handout's expectations in your own submission:

**The surrounding application (not shown in this demo) must also:** be a
menu-driven program with classes and inheritance, three or more modules plus a
thin `main.py`, file persistence, custom exception handling, and at least one
algorithm you implement yourself (sorting, searching, or recursion). Keep the AI
code in its own module so the core app works with the AI feature switched off.

Separation of responsibilities is the whole point: **your application owns the
data and the rules; the model is only a presentation layer** that explains and
summarizes facts you already retrieved. The complete requirements, project
options, grading rubric, and the five required tests are in
`Final_Mini_Project_Handout.pdf`.
