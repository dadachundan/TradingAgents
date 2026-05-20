#!/usr/bin/env python3
"""Global / macro news CLI wrapper."""

from __future__ import annotations

import argparse
import sys

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))

from tradingagents.dataflows.interface import route_to_vendor


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch global / macro news.")
    parser.add_argument("trade_date", help="As-of date YYYY-MM-DD")
    parser.add_argument("--look-back-days", type=int, default=None, help="Days to look back (default from config).")
    parser.add_argument("--limit", type=int, default=None, help="Max articles (default from config).")
    args = parser.parse_args()

    print(route_to_vendor("get_global_news", args.trade_date, args.look_back_days, args.limit))
    return 0


if __name__ == "__main__":
    sys.exit(main())
