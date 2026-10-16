"""RAG demo: ask a local Ollama model about your own CSV file.

Retrieval-augmented generation (RAG) in three small steps:

1. LOAD     read the CSV rows in ``data/`` into a list of records.
2. RETRIEVE pick the rows most relevant to the question with plain Python
            keyword matching (no vector database, no extra packages).
3. GENERATE send ONLY those rows plus the question to a local Ollama model and
            print the answer with the record IDs it was based on.

Ways to run it:
    python3 demo_rag.py                      # interactive questions
    python3 demo_rag.py --question "..."      # answer one question and exit
    python3 demo_rag.py --summarize           # summarize the whole file
    python3 demo_rag.py --model gemma3:1b     # use a lighter model

If Ollama is not running, the demo says so instead of inventing an answer.
"""

import argparse
import csv
import json
import re
from pathlib import Path
from urllib import request

DATA_DIR = Path(__file__).parent / "data"
OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen3:1.7b"
TOP_K = 7              # how many records to send to the model per question
TIMEOUT = 180         # seconds to wait (the first answer loads the model)

# Common words ignored when matching a question to the records.
STOPWORDS = {
    "about", "after", "again", "also", "and", "are", "could", "does", "from",
    "for", "have", "how", "into", "its", "just", "me", "more", "only", "please",
    "should", "that", "the", "their", "them", "then", "there", "these", "this",
    "through", "what", "when", "where", "which", "with", "would", "you",
}


class OllamaUnavailable(RuntimeError):
    """Raised when the local Ollama model cannot be reached."""


def keywords(text):
    """Return the meaningful lowercase words in ``text`` (drops short/common ones)."""
    return {
        word
        for word in re.findall(r"[a-z0-9]+", text.lower())
        if len(word) > 2 and word not in STOPWORDS
    }


def load_records(data_dir=DATA_DIR):
    """Read every CSV in ``data_dir`` into a list of ``{"id", "text"}`` records.

    Each row becomes one record; its ``record_id`` (or ``id``) column is the
    citation. Rows without an id are skipped.
    """
    records = []
    for path in sorted(data_dir.glob("*.csv")):
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                record_id = (row.get("record_id") or row.get("id") or "").strip()
                values = {
                    key: value.strip()
                    for key, value in row.items()
                    if key and value and value.strip()
                }
                if record_id and values:
                    text = json.dumps(values, ensure_ascii=False)
                    records.append({"id": record_id, "text": text})
    return records


def retrieve(question, records, top_k=TOP_K):
    """Return the ``top_k`` records that share the most keywords with the question."""
    query = keywords(question)
    scored = [(len(query & keywords(record["text"])), record) for record in records]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [record for score, record in scored[:top_k] if score]


def build_prompt(question, sources):
    """Build a grounded prompt telling the model to use only ``sources``."""
    blocks = "\n\n".join(f"[Source {s['id']}]\n{s['text']}" for s in sources)
    return (
        "You are a helpful assistant for a classroom RAG demo.\n"
        "Answer using ONLY the sources below. Do not invent details. If the "
        "sources do not answer the question, reply exactly NOT_IN_SOURCES. "
        "Keep the answer concise.\n\n"
        f"Question: {question}\n\n"
        f"Sources:\n{blocks}"
    )


def generate(prompt, model=DEFAULT_MODEL, timeout=TIMEOUT):
    """Send ``prompt`` to the local Ollama model and return its answer text.

    Raises:
        OllamaUnavailable: if the local model cannot be reached or replies badly.
    """
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2, "num_ctx": 4096, "num_predict": 1024},
    }).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    try:
        with request.urlopen(
            request.Request(OLLAMA_URL, data=body, headers=headers), timeout=timeout
        ) as response:
            answer = json.loads(response.read())["response"]
    except (OSError, ValueError, KeyError) as exc:
        raise OllamaUnavailable(str(exc)) from exc
    # Thinking models (e.g. qwen3) wrap reasoning in <think>...</think>; drop it.
    return re.sub(r"<think>.*?</think>", "", answer, flags=re.DOTALL).strip()


def ask_model(question, sources, model):
    """Call the model with ``sources`` and print the answer, or a clear notice."""
    print("Asking the local model (the first answer can be slow)...")
    try:
        answer = generate(build_prompt(question, sources), model)
    except OllamaUnavailable as exc:
        print(
            f"\n[Ollama unavailable] Could not reach the local model ({exc}).\n"
            "Start Ollama (open the app or run 'ollama serve') and try again."
        )
        return
    if "NOT_IN_SOURCES" in answer:
        print("\n[The retrieved records do not contain enough information.]")
    else:
        print(f"\n{answer}")
    print(f"\nSources: {', '.join(s['id'] for s in sources)}")


def answer_question(question, records, model):
    """Retrieve records for ``question`` and ask the model to answer."""
    sources = retrieve(question, records)
    if not sources:
        print(
            "No matching records found, so the model was not asked. Try words "
            "that appear in the file, or type 'summarize' for an overview."
        )
        return
    print(f"Retrieved sources: {', '.join(s['id'] for s in sources)}")
    ask_model(question, sources, model)


def summarize(records, model):
    """Summarize the whole file by sending every record to the model."""
    if not records:
        print("There are no records to summarize.")
        return
    print(f"Summarizing all {len(records)} record(s)...")
    ask_model(
        "Give a short summary of all these records, citing a few record IDs.",
        records,
        model,
    )


def main():
    """Parse arguments, load the records, and run the requested mode."""
    parser = argparse.ArgumentParser(
        description="Ask a local Ollama model about your CSV file."
    )
    parser.add_argument("--question", help="Ask one question and exit.")
    parser.add_argument(
        "--summarize", action="store_true", help="Summarize the file and exit."
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Ollama model tag (default: {DEFAULT_MODEL}).",
    )
    args = parser.parse_args()

    records = load_records()
    if not records:
        print(f"No CSV records found in {DATA_DIR}. Add a CSV with a 'record_id' column.")
        return

    if args.summarize:
        summarize(records, args.model)
    elif args.question is not None:
        answer_question(args.question, records, args.model)
    else:
        print(f"Loaded {len(records)} records from {DATA_DIR}.")
        print("Ask a question, type 'summarize', or type 'quit' to exit.")
        while True:
            try:
                question = input("\n> ").strip()
            except EOFError:
                break
            if question.lower() in {"quit", "exit"}:
                break
            if question.lower() in {"summarize", "summary"}:
                summarize(records, args.model)
            elif question:
                answer_question(question, records, args.model)


if __name__ == "__main__":
    main()
