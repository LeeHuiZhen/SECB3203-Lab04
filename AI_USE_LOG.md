# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 4
- Student name: Lee Hui Zhen
- Matric no: A24CS0259
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 12 November 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 12 November 2026, 4:45 PM
- Tool: Google (2026). Gemini. Retrieved 12 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "In filter_panel, why do we iterate over the genes list instead of using set intersection like in shared_genes?"
- Output: Explained that sets do not preserve order and remove duplicates, whereas filter_panel must keep the original panel order and retain duplicate entries. Iterating over the list while checking membership in the priority set preserves order and runs in O(1) lookup time per item.
- Verified by: Tested `filter_panel(["BRCA1", "TP53", "BRCA1"], {"BRCA1"})` to confirm it returns `["BRCA1", "BRCA1"]`.
- My change: Used a list comprehension `[gene for gene in genes if gene in priority]` in `filter_panel`.
- Used in: src/panel.py (filter_panel)

## Entry 2

- Date: 12 November 2026, 5:05 PM
- Tool: Google (2026). Gemini. Retrieved 12 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "How does _chrom_key work in panel.py? Why can't we just sort chromosome names directly?"
- Output: Explained that comparing strings puts '10' before '2' alphabetically. Returning a tuple key `(0, int(name), "")` for numeric autosomes and `(1, order, name)` for X, Y, M ensures numeric sorting first, and converting `.upper()` before `.removeprefix("CHR")` handles uppercase prefixes.
- Verified by: Tested sorting `Variant("10", 5, "A", "G")` and `Variant("2", 9, "C", "T")` in Python.
- My change: Used `chrom.upper().removeprefix("CHR")` and the tuple sort key in `_chrom_key`.
- Used in: src/panel.py (_chrom_key, sort_variants)

## Entry 3

- Date: 12 November 2026, 5:20 PM
- Tool: Google (2026). Gemini. Retrieved 12 November 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: "In lookup.py, how do I make sure shared_genes works even if the input lists have duplicate genes, and why did my f-string in translate print True?"
- Output: Suggested wrapping inputs with `set(panel) & set(detected)` so list inputs with duplicates are safely converted before set intersection. Also pointed out that `{len(dna) is not a multiple of 3}` evaluates a boolean expression inside the f-string instead of `{len(dna)}`.
- Verified by: Ran `python -m pytest tests/test_visible.py` and checked the ValueError message formatting.
- My change: Updated `shared_genes` to `set(panel) & set(detected)` and fixed the f-string to `f"length {len(dna)} is not a multiple of 3"`.
- Used in: src/lookup.py (shared_genes, translate)

## Entry 4

- Date: 12 November 2026, 5:35 PM
- Tool: Google (2026). Gemini. Retrieved 12 November 2026 from https://gemini.google.com
- Purpose: tests-plan
- Prompt: "What test cases should I write in test_lab04_own.py for Task 5, and should I read from the data folder or make my own inputs?"
- Output: Advised using self-contained inputs to cover the four required tests: verifying `sorted_copy` does not modify the original list, sorting chromosomes including X and M, testing `kmer_counts` with empty strings and `k` larger than sequence length, and testing `safe_expression` with missing keys and `0.0`.
- Verified by: Checked Task T5 and Rubric R6 in the Lab 4 brief.
- My change: Wrote four unit tests in `tests/test_lab04_own.py` and ran `ruff check --fix src tests` to remove unused imports.
- Used in: tests/test_lab04_own.py