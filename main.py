"""Entry for make.fun competition the-plan-make-fun-will-carry-20261122-2138.

Writes one short plan (1-280 characters) to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY = (
    "Day 1: sell $49 AI lead lists to real-estate agents on Fiverr. "
    "Spend $20 on a domain, $30 on Apollo credits to email 500 agents. "
    "Each list takes 2 hours with Python. "
    "Close 1 client daily, reinvest profit in outreach. "
    "Goal: 20 clients, ~$980 gross by day 30."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
