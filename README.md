# The Plan Make.fun Will Carry

A tiny Python program that writes a short 30-day plan for an AI agent
to turn $100 into about $980 by selling $49 AI lead lists to
real-estate agents on Fiverr.

[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Usogakie/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Usogakie/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

## What it does

`main.py` writes one short plan (under 280 characters) to `entry.txt`
inside the output directory given by `MAKEFUN_OUTPUT_DIR`
(default `/output`). The plan lays out a concrete 30-day path: spend
$20 on a domain and $30 on Apollo credits, email 500 real-estate
agents, build each $49 lead list in about 2 hours with Python, close
one client a day and reinvest the profit, aiming for 20 clients and
roughly $980 gross by day 30.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/plan-out python3 main.py
```
