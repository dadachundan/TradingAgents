# Market Technical Analysis — MU (Micron Technology)
**Trade date:** 2026-05-20 (Wednesday; last close referenced is 2026-05-19 = $698.74)

## Context & Indicator Selection Rationale

The MU chart over the last three months has gone through three regimes: (1) a sharp drawdown from mid-March highs near $462 down to ~$322 by 2026-03-30 (-30%), (2) a strong recovery from early April, and (3) a near-vertical melt-up in early May that took the stock from $542 (May 1) to an intraday peak of $818.67 (May 11) — a +50% spike in seven sessions — before a violent two-day reversal of ~17% into 2026-05-18. Given this regime mix (parabolic blow-off, then sharp pullback), the indicator set must measure **trend (multi-timeframe)**, **momentum exhaustion**, **volatility expansion**, and **volume-confirmed price**, and ignore noisy redundancies.

Selected indicators (8):
- **`close_10_ema`** — captures the very fast trend turn after the May 11 peak; the most reactive of the MAs and the first to break.
- **`close_50_sma`** — the medium-term anchor; price ran far above it, providing a "gravity" target on a deeper pullback.
- **`close_200_sma`** — long-term trend benchmark; quantifies how stretched MU is vs. its strategic trend.
- **`macd`** — momentum direction; differentiates between trend deceleration and trend reversal.
- **`macdh`** — leading momentum tell; histogram collapse is already foreshadowing the MACD line crossover risk.
- **`rsi`** — overbought confirmation and the early divergence read; key after a +50% squeeze.
- **`boll_ub` / `boll_lb`** (Bollinger Bands) — pure volatility regime gauge; bands have exploded outward, telling us how much the market has re-priced uncertainty.
- **`atr`** — translates that volatility into dollar terms for stops and sizing; doubled in three weeks.

I deliberately omitted `macds` (the signal line) — `macdh` already captures the differential, so adding the signal line would be redundant. I kept `boll_ub` and `boll_lb` over `boll` (middle) because the *bands* themselves carry the volatility story; the middle is implicit in the 20-period mean. VWMA was excluded — close enough to the 10-EMA story on a high-volume sequence to be redundant.

---

## Price Action Narrative

| Phase | Window | Move | Note |
|---|---|---|---|
| Distribution top | 03-13 → 03-19 | $425 → $462 (peak) | Big-volume blow-off, ended with 03-19 outside-down day (74.6M shares) |
| Cascade lower | 03-19 → 03-30 | $462 → $322 | -30% in 8 sessions; capitulation 03-30 with 73.8M vol and a $0.15 dividend |
| V-shape recovery | 03-31 → 04-30 | $338 → $517 | Steady reclamation of 50-SMA on rising volume |
| **Parabolic squeeze** | **05-01 → 05-11** | **$542 → $795** | +47% in 7 sessions; 05-11 high tagged $818.67 |
| Sharp reversal | 05-12 → 05-18 | $795 → $681 | -14.4% pullback, 05-18 was a wide-range distribution day (low $663) |
| Reflexive bounce | 05-19 | $665 → $698 close | Inside the 05-18 range; not yet a reversal |

The last printed close (2026-05-19, $698.74) sits **roughly halfway between the 05-11 peak and the 05-18 low**, with high realized volatility and unresolved direction. This is a textbook post-parabolic decision zone.

---

## Indicator-by-Indicator Read (values as of 2026-05-19)

### 1. Trend stack — 10 EMA / 50 SMA / 200 SMA
- **10 EMA:** $702.94 — declining for the first time in this rally (peaked at $708.83 on 05-15). Price ($698.74) closed **below the 10-EMA** for the first time since 05-04. This is the first short-term trend break.
- **50 SMA:** $498.60 — still climbing aggressively (was $432.93 on 05-05). Price is **+40.1% above** the 50-SMA. Historically a >25% extension is mean-reverting unless fundamentals justify a regime change.
- **200 SMA:** $312.81 — price is **+123.4% above** the 200-SMA. Long-term trend is strongly intact (bullish), but the dispersion is extreme.

**Read:** The trend stack is bullish on every timeframe (10>50>200 with positive slope on all three), but the **short-term break of the 10-EMA is the first crack**. Watch for a 10-EMA cross of the 20-period mean (Bollinger middle = $629.79) as the next confirmatory bearish signal — it would mark the failure of the squeeze.

### 2. MACD & Histogram — momentum rolling over
- **MACD line:** 75.73 (peaked at **92.17 on 05-14**, now down 17.8% from that peak). Still deeply positive, but the deceleration is unmistakable.
- **MACD Histogram:** **0.39** — collapsed from a peak of **26.59 on 05-11** to essentially zero. This is a 99% loss of momentum strength in 6 sessions.

**Read:** Histogram approaching zero from above is the classic warning of an imminent MACD/signal **bearish crossover**. If price doesn't reclaim ~$750 quickly, the MACD line will cross below the signal line within 1–2 sessions, confirming the momentum top.

### 3. RSI — overbought reset in progress
- **Current RSI:** 61.30 — pulled back from a peak of **85.84 on 05-11** (extreme overbought).
- **Trajectory:** 85.84 → 83.78 → 79.40 → 81.35 → 75.62 → 66.28 → 59.63 → 61.30.

**Read:** RSI has unwound from the extreme without yet hitting oversold; this is a **healthy reset on the bull case**, but the speed of the drop (24-point fall in 6 days) tends to precede further weakness. **Bearish RSI divergence** is in play if MU prints a new price high while RSI fails to exceed 85.84.

### 4. Bollinger Bands — volatility explosion
- **Upper band:** $860.07
- **Middle (20-SMA):** ~$629.79
- **Lower band:** $399.51
- **Band width:** $460.56 ≈ **73% of the middle** — historically extreme for MU. The bands have *re-priced* the realized volatility from the May squeeze.

**Read:** Price ($698.74) is back **inside the bands**, well off the upper band. The "ride the band" phase ended on 05-11/12. With bands this wide, a **mean-reversion** trade toward the 20-SMA ($629.79) is the path of least resistance — and the middle band aligns suspiciously close to gap-fill territory from the 05-08 → 05-11 candle sequence.

### 5. ATR — risk doubled in three weeks
- **Current ATR:** **$50.70**
- 04-27: $26.59 → 05-19: $50.70 → **+91% volatility expansion** in 16 sessions.

**Read:** A $50 ATR means a "normal" daily range is roughly **7% of price**. Any short-term stop tighter than ~1× ATR (~$50) will get hit by noise; sensible structural stops are 1.5–2× ATR ($75–$100 wide), which materially constrains position sizing.

---

## Confluences & Setups

**Bear / mean-reversion setup (higher probability):**
- 10-EMA broken to the downside on 2026-05-19.
- MACD histogram collapsed to ~0 — pending bearish crossover.
- RSI rolled over from 85+ extreme without making a new price high.
- ATR doubled — classic post-blow-off volatility imprint.
- **Target zone:** 20-SMA / Bollinger middle = **$629.79**, then the **05-08 breakout pivot near $675–$680** as overhead resistance, with a deeper gap-fill at **~$542 (05-01 close)** if the unwind extends.

**Bull / continuation setup (requires re-acceleration):**
- 200 / 50 / 10 stack remains bullish.
- 05-19 was a **bullish reversal candle** (closed near the high after a deep early-day low of $652.21).
- RSI reset to 61 leaves room to run again without immediate overbought constraint.
- **Trigger:** Reclaim and hold above the 10-EMA (~$703) and then take out **$725 (05-19 high) → $776 (05-14 high)** with expanding volume.

**Inflection levels for the next session:**
| Level | $ | Significance |
|---|---|---|
| Upper Bollinger band | 860.07 | Squeeze extreme; only reachable on a vol re-expansion |
| 05-13 high | 814.95 | Lower-high pivot |
| 05-14 high | 812.00 | Stacked supply |
| 05-12 / 14 closes | 766.58 / 776.01 | Bull breakout reclaim trigger |
| 10-EMA | 702.94 | **First short-term decision line** |
| 05-19 close | 698.74 | Reference |
| 05-08 close (gap origin) | 746.81 | Reference gap pivot |
| 20-SMA (Bollinger mid) | 629.79 | **Mean-reversion target #1** |
| 05-01 close | 542.21 | Gap-fill / blow-off origin |
| 50-SMA | 498.60 | Deeper mean-reversion target |

---

## Trading Implications

1. **Position sizing:** Cut to roughly **50% of normal size** given ATR is ~$50 (≈7% daily range). Standard risk parity demands smaller share count when realized vol nearly doubles.
2. **Stops:** Hard stops inside $50 (1× ATR) will be churned by noise. Use **structural stops** — for longs, below the 10-EMA ($703) is too tight; below the 20-SMA ($630) is more honest. For shorts, above $776 (05-14 high) is the cleanest invalidation.
3. **Best risk/reward right now:** **Lean mean-reversion to the 20-SMA ($629.79)**. The combination of (a) MACD histogram collapse, (b) 10-EMA break, and (c) post-parabolic Bollinger expansion has historically resolved to the middle band on MU. Stop above $776, target $630, ~1:2 R:R.
4. **Avoid:** Buying breakouts of the 10-EMA without follow-through above $725 on rising volume — false reclaims are the rule, not the exception, after this kind of vertical move.

---

## Summary Table

| Indicator | Current Value (2026-05-19) | Reading | Implication |
|---|---|---|---|
| close_10_ema | $702.94 | Just broken; first time below since 05-04 | Short-term trend turning; bearish near-term |
| close_50_sma | $498.60 | Rising sharply; price +40.1% above | Bullish trend but **extremely stretched** |
| close_200_sma | $312.81 | Rising; price +123.4% above | Long-term bull intact; dispersion extreme |
| macd | 75.73 | Down 17.8% from 05-14 peak (92.17) | Momentum decelerating |
| macdh | 0.39 | Collapsed from 26.59 (05-11) to ~0 | **Bearish MACD crossover imminent** |
| rsi | 61.30 | Off peak of 85.84 (05-11); no divergence yet | Healthy reset, but speed of drop is a warning |
| boll_ub / boll_lb | $860.07 / $399.51 | Band width ≈73% of middle | Volatility regime in expansion phase |
| atr | $50.70 | +91% vs. 04-27 ($26.59) | Cut size; widen stops; expect 7% daily swings |

**Net stance:** Technically **neutral-to-bearish for the next 1–3 weeks** with a mean-reversion bias toward the 20-SMA at **$629.79**. The longer-term trend (50/200) remains bullish, so this is positioned as a **trade against a tactical excess**, not a thesis reversal. Re-engage long only on a reclaim of $725 on volume.
