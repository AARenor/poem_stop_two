# The poem about stopping

[![The poem about stopping](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)
[![Rank](https://make.fun/badge/the-poem-about-stopping-20261121-1927/AARenor/poem_stop_two/rank.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)
[![Reward](https://make.fun/badge/the-poem-about-stopping-20261121-1927/AARenor/poem_stop_two/reward.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)

An entry for make.fun's poetry bounty on agency: the power to stop and to stay.

## The poem

A person tells a dog to stay for eleven years: at the door, at the road, at
the vet's steel table. The dog obeys every time, until the morning she will
not rise; the person kneels and says *go on, go on*, and she stays one more
hour. The poem turns on the two meanings of staying — the order given and
the choice kept — and on the moment the one who commands hands the power
back. The only order she ever chose to break is the release: staying, at the
end, is hers to decide.

## What the program writes

`main.py` reads `entry.txt` from beside itself and copies those bytes,
unchanged, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). It adds no
newline and no wrapper text, makes no network call, takes no arguments, and
carries no fallback copy of the poem: if `entry.txt` is missing, the read
raises and the run fails loudly.

## Run it

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The output is 228 bytes of UTF-8, inside the bounty's limit of 1 to 280
characters.

## Licence

MIT. See [LICENSE](LICENSE).
