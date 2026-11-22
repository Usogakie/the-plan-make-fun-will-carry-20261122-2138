"""Write a short 30-day plan for turning $100 into profit.

The plan describes selling $49 AI lead lists to real-estate agents on
Fiverr: spend $20 on a domain and $30 on Apollo credits, email 500
agents, build each list in about 2 hours with Python, close one client
a day, reinvest the profit, and reach roughly $980 gross by day 30.
The program writes the plan to entry.txt in the directory given by
MAKEFUN_OUTPUT_DIR (default "/output").
"""

import os


PLAN = (
    "Day 1: spend $20 on a domain and $30 on Apollo credits. "
    "Email 500 real-estate agents offering $49 AI lead lists on Fiverr. "
    "Build each list in ~2 hours with Python. "
    "Close 1 client a day, reinvest profits in outreach. "
    "Goal: 20 clients, ~$980 gross by day 30."
)


def main() -> None:
    if not PLAN.strip() or len(PLAN) > 280:
        raise ValueError("plan must be 1-280 non-blank characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN + "\n")


if __name__ == "__main__":
    main()
