import os
from pathlib import Path


LINE = "I can’t join, Fauzan—the meeting bot detected your agenda is recursive and opened a follow-up meeting to decide when to discuss this meeting’s follow-up."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", Path(__file__).resolve().parent))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
