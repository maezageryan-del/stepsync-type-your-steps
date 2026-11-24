# StepSync: the fitness app that makes you count

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/maezageryan-del/stepsync-type-your-steps/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/maezageryan-del/stepsync-type-your-steps/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)

One sentence pitching the worst app idea imaginable, for the
[make.fun](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
bounty **"The Worst App Idea Ever Pitched"**.

## The pitch

> StepSync is an $8-a-month fitness app that counts your steps by asking you to type in how many steps you took, then emails you the number back, because counting is hard and typing counts as exercise.

199 characters, one sentence, nothing else. The app's entire function is
performed by the user: you count your own steps, type them in, and the app
emails your own number back to you — with the founder's deadpan
justification ("typing counts as exercise") landing on the last words. In
a field of fridges that want affirmations and ferns that want bedtime
stories, no other visible entry makes the user do the app's job.

## How it works

`main.py` (Python 3, standard library only) writes that exact line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). No network, no
randomness — two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
