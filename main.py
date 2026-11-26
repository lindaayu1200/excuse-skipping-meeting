import os
from pathlib import Path

LINE = "I'm skipping Fauzan's meeting: I found a race condition in his Zoom invite—every time I accept, it schedules another meeting, so I'm patching the organizer."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or Path(__file__).resolve().parent)
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
