#!/usr/bin/env python3
"""Ticker-specific news CLI wrapper."""

from __future__ import annotations

import argparse
import sys

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))

from tradingagents.dataflows.interface import route_to_vendor


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch ticker-specific news for a date window.")
    parser.add_argument("ticker", help="Ticker symbol")
    parser.add_argument("start_date", help="Start date YYYY-MM-DD")
    parser.add_argument("end_date", help="End date YYYY-MM-DD")
    args = parser.parse_args()

    print(route_to_vendor("get_news", args.ticker, args.start_date, args.end_date))
    return 0


if __name__ == "__main__":
    sys.exit(main())
