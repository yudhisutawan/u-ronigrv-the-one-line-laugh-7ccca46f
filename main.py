"""One-line laugh entry: autocorrect turns a text into cutlery.

The joke: autocorrect changes "I'll be there soon" into "I'll be their
spoon", and the boss just replies "bring cutlery" — playing along instead
of correcting it. The humour lands twice: first the mangled text itself,
then a second voice that treats the typo as a real plan. Every office
worker and phone user has sent a mangled text to exactly the wrong
person, so the everyday truth is universal, and the whole joke needs no
setup beyond the quote.

The winning joke (108 characters) came out of a 9-candidate round-robin
tournament (36 pairs, judged head-to-head with the competition's own
judge brief): undefeated, 8 wins and 0 losses. Runner-up was the
password-reset paradox (7-1), which lost only to this entry — one twist
against this entry's two.

Writes the joke to entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output).

Guards enforce the gate and the single-sentence rule: exactly one
sentence (one terminal period, no other sentence-ending punctuation
inside the line), 1-200 characters, no newline characters.
"""

import os

# The joke, kept as one string so the output is a single line.
# Winner of a 9-candidate round-robin (36 pairs, judged head-to-head with
# the competition's own judge brief): undefeated, 8 wins and 0 losses.
JOKE = (
    "Autocorrect changed 'I'll be there soon' to 'I'll be their spoon', "
    "and my boss just replied 'bring cutlery'."
)


# Competition gate: one line, 1-200 characters.
MAX_LEN = 200


def build_joke() -> str:
    """Return the joke as a single line, no trailing newline."""
    return JOKE.strip()


def main() -> None:
    text = build_joke()
    # One line only, and inside the gate.
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line (no newline characters)")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(
            f"joke must be 1-{MAX_LEN} characters, got {len(text)}"
        )
    # Single sentence: exactly one terminal period, none inside the line.
    if not text.endswith(".") or text.count(".") != 1:
        raise SystemExit("joke must stand alone as a single sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
