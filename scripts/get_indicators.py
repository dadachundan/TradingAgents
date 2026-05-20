#!/usr/bin/env python3
"""Technical indicator CLI wrapper around tradingagents.dataflows.

Supports a comma-separated list of indicators in --indicators; one route_to_vendor
call per indicator, results joined with blank lines.
"""

from __future__ import annotations

import argparse
import sys

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))

from tradingagents.dataflows.interface import route_to_vendor


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch technical indicators for a ticker.")
    parser.add_argument("ticker", help="Ticker symbol")
    parser.add_argument("trade_date", help="As-of date in YYYY-MM-DD")
    parser.add_argument(
        "--indicators",
        required=True,
        help="Comma-separated indicator names, e.g. close_50_sma,macd,rsi,boll,atr,vwma",
    )
    parser.add_argument("--look-back-days", type=int, default=30, help="Window length (default 30).")
    args = parser.parse_args()

    names = [n.strip().lower() for n in args.indicators.split(",") if n.strip()]
    blocks = []
    for name in names:
        try:
            blocks.append(route_to_vendor("get_indicators", args.ticker, name, args.trade_date, args.look_back_days))
        except ValueError as exc:
            blocks.append(str(exc))
    print("\n\n".join(blocks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
