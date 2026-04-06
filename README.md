\# Europe Momentum Backtest



\## Objective



This project implements a systematic momentum strategy on a fixed universe of European large-cap equities.



The objective is to test whether past winners continue to outperform, using a simple and transparent monthly backtest framework.



\---



\## Strategy Rules



\- Universe: 24 fixed European equities

\- Signal: momentum 12-1

\- Ranking frequency: monthly

\- Portfolio selection: top 30%

\- Weighting scheme: equal weight

\- Rebalancing: monthly

\- Transaction costs: 10 bps per trade



\---



\## Backtest Design



\- Data period: 2010–2025

\- Warm-up period: 2010–2011

\- In-sample period: 2012–2018

\- Out-of-sample period: 2019–2025



\---



\## Universe Description



\- AIR.PA : Airbus, aerospace (France)

\- BNP.PA : BNP Paribas, banking (France)

\- SAN.PA : Sanofi, pharmaceuticals (France)

\- MC.PA : LVMH, luxury goods (France)



\- SAP.DE : SAP, software (Germany)

\- SIE.DE : Siemens, industrial engineering (Germany)

\- ALV.DE : Allianz, insurance (Germany)

\- BAS.DE : BASF, chemicals (Germany)



\- ASML.AS : ASML, semiconductor equipment (Netherlands)

\- INGA.AS : ING, banking (Netherlands)

\- PHIA.AS : Philips, healthcare tech (Netherlands)

\- AD.AS : Ahold Delhaize, retail (Netherlands)



\- ENI.MI : ENI, oil \& gas (Italy)

\- ISP.MI : Intesa Sanpaolo, banking (Italy)

\- UCG.MI : UniCredit, banking (Italy)

\- ENEL.MI : Enel, electricity utility (Italy)



\- IBE.MC : Iberdrola, energy (Spain)

\- SAN.MC : Santander, banking (Spain)

\- BBVA.MC : BBVA, banking (Spain)

\- ITX.MC : Inditex, retail (Spain)



\- NESN.SW : Nestlé, food (Switzerland)

\- NOVN.SW : Novartis, pharmaceuticals (Switzerland)

\- ROG.SW : Roche, biotech (Switzerland)

\- UBSG.SW : UBS, investment banking (Switzerland)



\---



\## Notebook Structure



\- 01\_data.ipynb → data download and monthly returns

\- 02\_factor.ipynb → momentum signal construction

\- 03\_backtest.ipynb → portfolio construction and performance

\- 04\_risk\_costs.ipynb → drawdown, volatility, transaction costs

\- 05\_robustness\_oos.ipynb → in-sample / out-of-sample testing

\- 99\_summary.ipynb → final synthesis



\---



\## Tools



Python, pandas, numpy, matplotlib, yfinance

