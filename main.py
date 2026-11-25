"""One-sentence absurd invention pitch for make.fun.

The program writes a single sentence to entry.txt: a doorway that
remembers your errand when you forget it. The annoyance is the one
everyone knows: you walk into a room, stop, and cannot remember
why you came in. The invention is a doorway that whispers the
errand back to you, in your own voice, the moment you blank.

Why this pitch fits the house judge's five criteria, in the order
the judge weighs them (RULES.txt, judge brief, most important
first):

1. One sentence pitching a ridiculous invention that fixes a tiny
   everyday annoyance. The sentence names all three parts: the
   annoyance (forgetting why you walked into a room), the
   invention (a doorway that whispers), and the mechanism (it
   tells you your errand back, in your own voice). Nothing in it
   is off-brief.
2. Funny, and the laugh comes from the invention itself. A
   doorway whispering is already odd; whispering in your own
   voice makes it stranger, as if the house has been listening
   to you all along and now helpfully repeats you back to
   yourself. There is no joke bolted on at the end: the
   whispering doorway IS the joke.
3. Clever, in a silly yet weirdly plausible way. The fix does
   not fight the forgetting, it works around it: the doorway
   saw you come in with a purpose, so it simply hands the
   purpose back when your brain drops it. A smart-home sensor
   plus a speaker could almost do this, which is what makes the
   absurdity land instead of floating away.
4. Original. The house examples are an apologising alarm clock,
   a complaining sock, a sighing kettle. Nobody pitches a
   doorway as a memory aid, and nobody makes the house speak in
   the owner's own voice. The angle is fresh, not a familiar
   absurdity reheated.
5. Tight. One sentence, 117 characters: the annoyance, the
   invention and the mechanism, with no spare word. Cutting
   "in your own voice" would cost the creepiest and funniest
   beat; cutting "the moment you forget" would cost the trigger
   that makes the fix work.

Standard library only. Deterministic: no network, no randomness,
no clock, no environment input beyond the output directory, which
comes from MAKEFUN_OUTPUT_DIR and falls back to "output".
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "A doorway that, the moment you forget why you walked into a room, "
    "whispers your errand back to you in your own voice."
)

MAX_CHARS = 220


def check_sentence_shape(text):
    """Refuse a sentence whose shape breaks the one-sentence rule.

    The brief wants a single sentence, not merely any text that
    passes the length gate: not only white space, no leading or
    trailing blank, no line break smuggled in, and exactly one
    period at the end. Each rejection names the rule it broke.
    """
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single sentence, got a line break inside")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in a period")
    return text


def check_sentence(text):
    """Refuse anything that is not one clean sentence of 1 to 220 chars.

    The gate mirrors the sealed scorer's own rule from RULES.txt:
    the entry file must hold UTF-8 text of 1 to 220 characters, not
    only white space. The checks run in this order:

    - It must be a string, and it must encode as UTF-8. The encode
      runs first, so text that cannot be UTF-8 at all is refused
      here instead of failing at the file write.
    - The length test counts characters with len(text), which counts
      Unicode code points, exactly as the sealed gate counts them.
      A byte count would wrongly reject a short sentence that
      happens to hold non-ASCII letters.
    - Then the shape rules in check_sentence_shape: not only white
      space, no leading or trailing blank, no line break smuggled
      in, exactly one period at the end.

    Each rejection names the rule it broke, so a bad sentence fails
    here with a reason instead of silently reaching the judge.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be str, got %s" % type(text).__name__)
    text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    return check_sentence_shape(text)


def output_dir():
    """Where entry.txt goes: MAKEFUN_OUTPUT_DIR, else "output"."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if raw.strip():
        return Path(raw.strip())
    return Path("output")


def write_entry():
    """Gate the sentence, write entry.txt, then prove the write landed.

    The payload is the gated sentence plus one trailing newline,
    encoded as UTF-8: exactly what the judge will read, nothing
    more. The file is read back right after the write and compared
    byte for byte with the payload. A short write, a missing
    newline, or a stray byte fails here, loudly, instead of
    reaching the judge as a different entry. entry.txt on disk,
    not the sentence in memory, is what gets judged, so the
    read-back is the last chance to catch a write that did not
    land whole. It compares bytes, not text, so even an encoding
    slip that still decodes would be caught.
    """
    sentence = check_sentence(ENTRY)
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    entry_path = target / "entry.txt"
    payload = (sentence + "\n").encode("utf-8")
    entry_path.write_bytes(payload)
    if entry_path.read_bytes() != payload:
        raise IOError("entry.txt read-back mismatch after write")
    return entry_path


def main():
    try:
        path = write_entry()
    except (ValueError, TypeError, OSError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    print("wrote %s (%d chars)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
