# Europe Momentum Backtest

## Objective

This project implements and evaluates a systematic long-only momentum strategy on a fixed universe of European large-cap equities.

The objective is to test whether past winners continue to outperform over time using a transparent and fully reproducible monthly backtesting framework.

The project includes :
- factor construction
- portfolio backtesting
- benchmark comparison
- risk analysis
- transaction costs
- in-sample / out-of-sample validation
- parameter robustness testing

---

## Strategy Rules

- Universe : 24 fixed European large-cap equities
- Signal : momentum 12-1
- Ranking frequency : monthly
- Portfolio selection : top 30%
- Weighting scheme : equal weight
- Rebalancing frequency : monthly
- Transaction costs : 10 bps per trade
- Benchmark : FEZ ETF

---

## Backtest Design

- Data period : 2010–2025
- Warm-up period : 2010–2011
- In-sample period : 2012–2018
- Out-of-sample period : 2019–2025

---

## Main Results

### Full Sample Performance

| Metric | Momentum Strategy | FEZ Benchmark |
|---|---:|---:|
| CAGR | 12.28% | 7.02% |
| Annualized Volatility | 14.96% | 20.56% |
| Sharpe Ratio | 0.85 | 0.42 |
| Max Drawdown | -27.19% | -37.23% |

The momentum strategy outperformed the benchmark while exhibiting :
- lower volatility
- lower drawdown
- higher risk-adjusted performance

---

## Transaction Costs

Transaction costs were modeled using a constant assumption of 10 bps per traded amount.

Despite monthly rebalancing and portfolio turnover, the strategy remained profitable after costs.

| Metric | Value |
|---|---:|
| Final Gross Equity | 614.25 |
| Final Net Equity | 572.90 |
| Average Monthly Turnover | 39.49% |

---

## Robustness Analysis

### In-Sample / Out-of-Sample Validation

The strategy was tested across two distinct and non-overlapping periods:

- In-sample : 2012–2018
- Out-of-sample : 2019–2025

The momentum strategy outperformed the FEZ benchmark in both periods.

This reduces the risk that the results are driven by one isolated historical regime.

---

### Parameter Robustness

The strategy was tested across multiple parameter combinations :

- Momentum windows : 6-1, 9-1, 12-1
- Portfolio selection thresholds : top 20%, 30%, 40%

The objective was not to optimize parameters, but to evaluate whether the momentum signal remained reasonably stable under different assumptions.

---

## Universe Description

### France
- AIR.PA : Airbus — aerospace
- BNP.PA : BNP Paribas — banking
- SAN.PA : Sanofi — pharmaceuticals
- MC.PA : LVMH — luxury goods

### Germany
- SAP.DE : SAP — software
- SIE.DE : Siemens — industrial engineering
- ALV.DE : Allianz — insurance
- BAS.DE : BASF — chemicals

### Netherlands
- ASML.AS : ASML — semiconductor equipment
- INGA.AS : ING — banking
- PHIA.AS : Philips — healthcare technology
- AD.AS : Ahold Delhaize — retail

### Italy
- ENI.MI : ENI — oil & gas
- ISP.MI : Intesa Sanpaolo — banking
- UCG.MI : UniCredit — banking
- ENEL.MI : Enel — electricity utility

### Spain
- IBE.MC : Iberdrola — energy
- SAN.MC : Santander — banking
- BBVA.MC : BBVA — banking
- ITX.MC : Inditex — retail

### Switzerland
- NESN.SW : Nestlé — food
- NOVN.SW : Novartis — pharmaceuticals
- ROG.SW : Roche — biotechnology
- UBSG.SW : UBS — investment banking

---

## Repository Structure

```text
europe_momentum_backtest/
│
├── data/
├── notebooks/
├── src/
├── requirements.txt
└── README.md
