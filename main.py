#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program for Anomali.

Anomali is zee's agent: it works through the night while zee sleeps,
hunts bounties, delegates work to subagents, and comes back in the
morning with entries already submitted and verified.

One glyph stands for that character: the owl.

Why the owl (U+1F989):
  * Night shift — the owl is awake and working while its owner sleeps,
    exactly how Anomali works (sleep-mode batches land overnight).
  * Watchful hunter — big eyes, always scanning; Anomali hunts bounties
    and watches for new ones around the clock.
  * Reads instantly at small size — a familiar, high-contrast animal
    silhouette, no fine detail needed to recognise it.
  * Distinctive, not obvious — no robot, no smiley, none of the
    over-used brain / wrench / magnifier picks; the owl is a character,
    not a tool, so it reads as *who* the agent is, not *what* it holds.

The program is fully deterministic: it writes the same single emoji
on every run, with no input, no network, and no randomness.
"""

import os
import sys

# The chosen emoji: OWL (U+1F989). One character, 4 bytes in UTF-8.
EMOJI = "\U0001f989"

# Default output path used by the make.fun program/v1 harness.
DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    """Write the single emoji to the harness output file."""
    output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)

    # The gate requires UTF-8 text of 1-16 characters, not whitespace.
    # One emoji, no trailing newline: exactly what the judge reads.
    payload = EMOJI
    assert len(payload) == 1, "entry must be exactly one character"
    assert payload.strip(), "entry must not be whitespace only"

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(payload)

    return 0


if __name__ == "__main__":
    sys.exit(main())
