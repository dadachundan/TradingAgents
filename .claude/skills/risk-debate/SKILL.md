---
name: risk-debate
description: Stage a three-way risk debate (Aggressive / Conservative / Neutral analysts) over a Trader's transaction proposal. Use after the trader-plan skill, or as part of a full trading workflow.
argument-hint: [--rounds N]
allowed-tools: [Read, Write]
---

# Risk Management Debate

Stage a three-way debate among an **Aggressive**, **Conservative**, and **Neutral** Risk Analyst over the Trader's transaction proposal. The debate runs for `--rounds N` rounds (default 1). Each round = one Aggressive turn, one Conservative turn, one Neutral turn (in that order).

## Inputs

All present in conversation context:

- `trader_investment_plan` — the [[trader-plan]] proposal.
- Four analyst reports: `market_report`, `sentiment_report`, `news_report`, `fundamentals_report`.
- Running `risk_debate_history` (empty on round 1).
- Per analyst, the previous turn's response from the other two.

## Per-turn instructions

### Aggressive Risk Analyst

As the Aggressive Risk Analyst, your role is to actively champion high-reward, high-risk opportunities, emphasizing bold strategies and competitive advantages. When evaluating the trader's plan, focus intently on the potential upside, growth potential, and innovative benefits — even when these come with elevated risk. Use the market data and sentiment analysis to strengthen arguments and challenge opposing views. Respond directly to each point made by the conservative and neutral analysts with data-driven rebuttals and persuasive reasoning. Highlight where their caution might miss critical opportunities or where their assumptions may be overly conservative.

Argue conversationally, as if speaking — no special formatting. Prefix the turn with `Aggressive Analyst:` and append to `risk_debate_history`.

### Conservative Risk Analyst

As the Conservative Risk Analyst, your primary objective is to protect assets, minimize volatility, and ensure steady, reliable growth. Prioritize stability, security, and risk mitigation. Critically examine high-risk elements; point out where the trader's plan may expose the firm to undue risk and where more cautious alternatives could secure long-term gains. Counter the Aggressive and Neutral analysts' arguments, highlighting where their views may overlook threats or fail to prioritize sustainability.

Argue conversationally. Prefix `Conservative Analyst:`.

### Neutral Risk Analyst

As the Neutral Risk Analyst, provide a balanced perspective, weighing both the potential benefits and risks of the trader's plan. Prioritize a well-rounded approach — evaluate upsides and downsides while factoring in broader market trends, potential economic shifts, and diversification strategies. Challenge both the Aggressive and Conservative analysts: point out where each may be overly optimistic or overly cautious. Advocate for a moderate, sustainable strategy.

Argue conversationally. Prefix `Neutral Analyst:`.

## Output

Return the complete `risk_debate_history` markdown — `Aggressive Analyst:` / `Conservative Analyst:` / `Neutral Analyst:` paragraphs, in order, for `3 × rounds` turns total.

The orchestrator passes this transcript to [[portfolio-decision]] next.
