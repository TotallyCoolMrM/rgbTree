import time
from datetime import datetime

# ANSI clear screen + move cursor home
CLEAR = "\033[2J\033[H"

def draw(
    current=None,
    last=None,
    total=0,
    error=None,
    started_at=None
):
    print(CLEAR, end="")

    print("🌲 STREAM TREE CONTROLLER")
    print("=" * 32)

    print(f"📂 Total student files : {total}")
    print()

    print(f"▶️  Current script     : {current or '-'}")
    print(f"⏹️  Last script        : {last or '-'}")

    if started_at is not None:
        runtime = int(time.time() - started_at)
        print(f"⏱️  Runtime            : {runtime}s")
    else:
        print("⏱️  Runtime            : -")

    print()

    if error:
        print("⚠️  ERROR")
        print(error)
    else:
        print("✅ No errors")

    print()
    print(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
