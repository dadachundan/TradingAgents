#!/usr/bin/env python3
"""Social sentiment CLI wrapper — supports StockTwits and Reddit sources."""

from __future__ import annotations

import argparse
import sys

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))

from tradingagents.dataflows.reddit import fetch_reddit_posts
from tradingagents.dataflows.stocktwits import fetch_stocktwits_messages


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch social sentiment from StockTwits or Reddit.")
    parser.add_argument("source", choices=["stocktwits", "reddit"], help="Which platform to query.")
    parser.add_argument("ticker", help="Ticker symbol (used as cashtag for StockTwits).")
    parser.add_argument("--limit", type=int, default=30, help="Max items (StockTwits only; default 30).")
    args = parser.parse_args()

    if args.source == "stocktwits":
        print(fetch_stocktwits_messages(args.ticker, limit=args.limit))
    else:
        print(fetch_reddit_posts(args.ticker))
    return 0


if __name__ == "__main__":
    sys.exit(main())
