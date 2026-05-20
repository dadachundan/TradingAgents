# TradingAgents — project instructions

## Always commit and push after changes

After making any change to this repo (edits, new files, deletes), finish the turn by:

1. Committing the change to the local `main` branch with a descriptive message.
2. Pushing the commit to `origin/main`.

```bash
git add <files>
git commit -m "descriptive message"
git push origin main
```

This is durable, in-advance authorization — do not stop to ask for confirmation before committing or pushing. Apply it to every change-producing turn.

If the push is rejected as non-fast-forward, rebase onto `origin/main` first; do not force-push.

If you are working inside a git worktree on a non-`main` branch, follow the worktree push workflow in `~/.claude/CLAUDE.md` instead (push the worktree branch's commits to `origin/main`, then `git -C <main-checkout> pull --ff-only origin main`).
