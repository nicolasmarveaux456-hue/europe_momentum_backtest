import numpy as np
import pandas as pd


def cagr(equity_curve: pd.Series) -> float:
    """
    Compound Annual Growth Rate (CAGR)

    Formula:
    CAGR = (V_final / V_initial)^(1/n) - 1
    """
    equity_curve = equity_curve.dropna()

    initial_value = equity_curve.iloc[0]
    final_value = equity_curve.iloc[-1]

    n_months = len(equity_curve) - 1
    n_years = n_months / 12

    return (final_value / initial_value) ** (1 / n_years) - 1


def annualized_volatility(returns: pd.Series) -> float:
    """
    Annualized Volatility

    Formula:
    Vol = std(monthly returns) * sqrt(12)
    """
    returns = returns.dropna()
    return returns.std() * np.sqrt(12)


def sharpe_ratio(returns: pd.Series) -> float:
    """
    Sharpe Ratio

    Formula:
    Sharpe = annualized return / annualized volatility
    """
    returns = returns.dropna()

    annual_return = returns.mean() * 12
    annual_vol = returns.std() * np.sqrt(12)

    return annual_return / annual_vol