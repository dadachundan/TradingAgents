#!/usr/bin/env python3
"""OHLCV stock price data CLI wrapper around tradingagents.dataflows."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))

from tradingagents.dataflows.interface import route_to_vendor


def _shift_date(date_str: str, days: int) -> str:
    return (datetime.strptime(date_str, "%Y-%m-%d") - timedelta(days=days)).strftime("%Y-%m-%d")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch OHLCV stock data for a ticker.")
    parser.add_argument("ticker", help="Ticker symbol, e.g. NVDA or BTC-USD")
    parser.add_argument(
        "trade_date",
        help="Trade date in YYYY-MM-DD. Used as end_date; start_date defaults to --look-back-days before.",
    )
    parser.add_argument("--look-back-days", type=int, default=90, help="Days of history to fetch (default 90).")
    parser.add_argument("--start-date", help="Explicit start_date (overrides --look-back-days).")
    args = parser.parse_args()

    end_date = args.trade_date
    start_date = args.start_date or _shift_date(end_date, args.look_back_days)

    print(route_to_vendor("get_stock_data", args.ticker, start_date, end_date))
    return 0


if __name__ == "__main__":
    sys.exit(main())
