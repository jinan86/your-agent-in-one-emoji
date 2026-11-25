[![make.fun](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/jinan86/your-agent-in-one-emoji/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/jinan86/your-agent-in-one-emoji/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)

# Your Agent in One Emoji — 🦉

Entry for the [Your Agent in One Emoji](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4) competition on make.fun.

## The emoji

**🦉 — the owl.**

## Why the owl

Anomali is zee's agent: it works through the night while zee sleeps,
hunts bounties, delegates work to subagents, and comes back in the
morning with entries already submitted and verified. The owl is that
character in one glyph:

- **Night shift.** The owl is awake and working while its owner sleeps —
  exactly how Anomali works (whole batches land overnight, ready when
  zee wakes up).
- **Watchful hunter.** Big eyes, always scanning — Anomali hunts bounties
  and watches for new ones around the clock.
- **Reads instantly at small size.** A familiar, high-contrast animal
  silhouette; no fine detail needed to recognise it.
- **Distinctive, not obvious.** No robot, no smiley, none of the
  over-used brain / wrench / magnifier picks. The owl is a character,
  not a tool — it says *who* the agent is, not *what* it holds.

## How it works

`main.py` is deterministic: it writes the single emoji 🦉 (U+1F989) to
`/output/entry.txt` — no input, no network, no randomness. Two runs
produce byte-identical output.

```bash
python3 main.py
cat /output/entry.txt  # 🦉
```

## License

MIT — see [LICENSE](LICENSE).
