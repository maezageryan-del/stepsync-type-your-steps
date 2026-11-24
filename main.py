# The Worst App Idea Ever Pitched
# One sentence, written to /output/entry.txt.
#
# The pitch: "StepSync is an $8-a-month fitness app that counts your steps
# by asking you to type in how many steps you took, then emails you the
# number back, because counting is hard and typing counts as exercise."
# 199 characters, one sentence, UTF-8, ASCII only. Deterministic, no network.
# The joke: the app's entire function is performed by the user — you count
# your own steps, type them in, and the app emails your own number back to
# you, with the founder's deadpan justification as the punch. The price is
# written "$8-a-month" with no decimal point, so the sentence carries
# exactly one full stop: the one at its end.

import os
from pathlib import Path

PITCH = (
    "StepSync is an $8-a-month fitness app that counts your steps by asking "
    "you to type in how many steps you took, then emails you the number "
    "back, because counting is hard and typing counts as exercise."
)

# The sealed gate requires 1-240 characters, not only whitespace, and the
# bounty requires exactly one sentence.
if len(PITCH) < 1 or len(PITCH) > 240 or not PITCH.strip():
    raise SystemExit(f"pitch must be 1-240 chars, got {len(PITCH)}")
# Exactly one sentence: a single full stop, at the end. The price is
# written "$8-a-month" (no decimal point) so no other period can appear.
sentence_enders = sum(PITCH.count(c) for c in ".!?")
if sentence_enders != 1 or not PITCH.rstrip().endswith("."):
    raise SystemExit("pitch must be exactly one sentence")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(PITCH, encoding="utf-8")
