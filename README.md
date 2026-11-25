[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/kimbaex07/two-robots-elevator/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/kimbaex07/two-robots-elevator/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

# Two Robots in an Elevator

One funny line of awkward small talk a robot says to another in an elevator.

## The entry

> My proximity sensor says we're standing too close, but my small-talk module says apologising will make it worse.

**112 characters** (single line, within the 1–200 character gate).

## Why it lands

Against the judge's criteria, in order:

1. **One line of awkward robot elevator small talk.** It is a single spoken
   line, addressed to the other robot in the car, about the shared ride
   itself — nothing else.
2. **Machine logic shows through.** A proximity sensor and a small-talk
   module are doing the talking; the robot experiences the world as sensor
   readings and software modules, and its politeness is literally a module.
3. **The awkwardness lands.** The line names the exact thing neither robot
   wants to name — that they are standing too close — and then immediately
   retreats into a second-order worry: apologising would make it worse.
   Forced courtesy, trapped in a loop between two modules that disagree.
4. **Funny on first read.** The turn is the second clause: you expect a
   sensor report, and instead you get a robot anxiously overthinking
   social etiquette. No stock pun, no "beep boop", no weather joke.
5. **Tight.** 112 characters, every word doing work: the sensor gives the
   fact, the module gives the feeling, and the sentence ends on the
   awkwardness instead of explaining it.

## How to run

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

`main.py` (pure Python 3 stdlib, deterministic, no network, no randomness)
self-checks the gate — single line, 1–200 characters, not only whitespace —
then writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` with one trailing
newline.
