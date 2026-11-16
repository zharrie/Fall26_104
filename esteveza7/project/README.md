The chosen project is Music library organizer and playlist builder working solo

Ollama tests conducted + code used
python3 demo_rag.py --model llama3.2:1b
Loaded 18 records from /home/rei_jackolantern/data.
Ask a question, type 'summarize', or type 'quit' to exit.

> summarize
Summarizing all 18 record(s)...
Asking the local model (the first answer can be slow)...

Here is a short summary of the records, citing a few record IDs:

* Record G-002 is open and has a status of "open", indicating that the filter inspection is still pending.
* Record G-005 is complete and has a status of "complete", indicating that the plant labels and basil trays have been moved away from the cold window.
* Record G-009 is scheduled and has a status of "scheduled", indicating that the label the brown-material bin before the weekend drop-off is due.
* Record G-013 is scheduled and has a status of "scheduled", indicating that the plant native flower plugs after the forecast rain are due.

Sources: G-001, G-002, G-003, G-004, G-005, G-006, G-007, G-008, G-009, G-010, G-011, G-012, G-013, G-014, G-015, G-016, G-017, G-018

python3 demo_rag.py --model llama3.2:1b --question "What tools are missing from the tool shed?"
Retrieved sources: G-010, G-011, G-012, G-009
Asking the local model (the first answer can be slow)...

The tools missing from the tool shed are:

* Two hand trowels
* Wheelbarrow tire

Sources: G-010, G-011, G-012, G-009
