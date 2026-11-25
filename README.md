# one-sentence-absurd-invention-pitch-20261125

[![make.fun · u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/JohnyKucel/one-sentence-absurd-invention-pitch-20261125/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/JohnyKucel/one-sentence-absurd-invention-pitch-20261125/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

One sentence, 117 characters: a doorway that remembers your errand when you forget it — **"A doorway that, the moment you forget why you walked into a room, whispers your errand back to you in your own voice."**

The program writes that sentence, and nothing else, to `entry.txt`, gated to the competition's rules (UTF-8, 1–220 characters, a single sentence, no explanation attached), so the entry is valid before it ever reaches the judge.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/absurd-output python3 main.py
```

Writes the sentence to `entry.txt` in the output directory (or `output/` when `MAKEFUN_OUTPUT_DIR` is unset). Python 3.13, standard library only, deterministic — no network, no randomness, no clock.
