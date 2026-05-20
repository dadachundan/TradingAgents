#!/usr/bin/env python3
"""Memory log CLI — read past context, append pending decisions, resolve with outcomes.

Wraps tradingagents.agents.utils.memory.TradingMemoryLog. The log lives at
memory/trading_memory.md (repo-relative) by default; override with --log-path.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))

from tradingagents.agents.utils.memory import TradingMemoryLog


DEFAULT_LOG = "memory/trading_memory.md"


def _log(args) -> TradingMemoryLog:
    return TradingMemoryLog(config={"memory_log_path": args.log_path})


def cmd_read(args) -> int:
    log = _log(args)
    print(log.get_past_context(args.ticker, n_same=args.n_same, n_cross=args.n_cross))
    return 0


def cmd_list(args) -> int:
    log = _log(args)
    entries = log.get_pending_entries() if args.pending else log.load_entries()
    for e in entries:
        suffix = " pending" if e.get("pending") else ""
        print(f"[{e['date']} | {e['ticker']} | {e['rating']}]{suffix}")
    return 0


def cmd_append(args) -> int:
    decision = Path(args.decision_file).read_text(encoding="utf-8")
    _log(args).store_decision(args.ticker, args.trade_date, decision)
    return 0


def cmd_resolve(args) -> int:
    reflection = Path(args.reflection_file).read_text(encoding="utf-8")
    _log(args).update_with_outcome(
        ticker=args.ticker,
        trade_date=args.trade_date,
        raw_return=args.raw_return,
        alpha_return=args.alpha_return,
        holding_days=args.holding_days,
        reflection=reflection,
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="TradingAgents memory log CLI.")
    parser.add_argument("--log-path", default=DEFAULT_LOG, help=f"Log file path (default {DEFAULT_LOG}).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_read = sub.add_parser("read", help="Format past context for the orchestrator.")
    p_read.add_argument("--ticker", required=True)
    p_read.add_argument("--n-same", type=int, default=5)
    p_read.add_argument("--n-cross", type=int, default=3)
    p_read.set_defaults(func=cmd_read)

    p_list = sub.add_parser("list", help="List entries (tag lines only).")
    p_list.add_argument("--pending", action="store_true", help="Only pending entries.")
    p_list.set_defaults(func=cmd_list)

    p_append = sub.add_parser("append", help="Append a pending decision.")
    p_append.add_argument("--ticker", required=True)
    p_append.add_argument("--trade-date", required=True)
    p_append.add_argument("--decision-file", required=True)
    p_append.set_defaults(func=cmd_append)

    p_resolve = sub.add_parser("resolve", help="Resolve a pending entry with realized returns.")
    p_resolve.add_argument("--ticker", required=True)
    p_resolve.add_argument("--trade-date", required=True)
    p_resolve.add_argument("--raw-return", type=float, required=True)
    p_resolve.add_argument("--alpha-return", type=float, required=True)
    p_resolve.add_argument("--holding-days", type=int, required=True)
    p_resolve.add_argument("--reflection-file", required=True)
    p_resolve.set_defaults(func=cmd_resolve)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
