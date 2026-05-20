#!/usr/bin/env python3
"""Insider transactions CLI wrapper."""

from __future__ import annotations

import argparse
import sys

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))

from tradingagents.dataflows.interface import route_to_vendor


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch insider transactions for a ticker.")
    parser.add_argument("ticker", help="Ticker symbol")
    args = parser.parse_args()

    print(route_to_vendor("get_insider_transactions", args.ticker))
    return 0


if __name__ == "__main__":
    sys.exit(main())
