#!/usr/bin/env python3
"""Fundamentals CLI wrapper. --view selects profile / balance_sheet / cashflow / income_statement."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))

from tradingagents.dataflows.interface import route_to_vendor


VIEW_TO_METHOD = {
    "profile": "get_fundamentals",
    "balance_sheet": "get_balance_sheet",
    "cashflow": "get_cashflow",
    "income_statement": "get_income_statement",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch company fundamentals.")
    parser.add_argument("ticker", help="Ticker symbol")
    parser.add_argument(
        "--view",
        required=True,
        choices=list(VIEW_TO_METHOD.keys()),
        help="Which fundamental slice to fetch.",
    )
    parser.add_argument(
        "--trade-date",
        default=datetime.today().strftime("%Y-%m-%d"),
        help="As-of date YYYY-MM-DD (default today).",
    )
    parser.add_argument(
        "--freq",
        default="quarterly",
        choices=["quarterly", "annual"],
        help="Reporting frequency for statements (default quarterly).",
    )
    args = parser.parse_args()

    method = VIEW_TO_METHOD[args.view]
    if method == "get_fundamentals":
        print(route_to_vendor(method, args.ticker, args.trade_date))
    else:
        print(route_to_vendor(method, args.ticker, args.freq, args.trade_date))
    return 0


if __name__ == "__main__":
    sys.exit(main())
