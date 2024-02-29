from classes import StockData
from yfinance import Ticker
from typing import Dict, Optional, List
from pandas import Series


def get_total_dividend(
    dividend: Optional[float], cash_per_share: Optional[float]
) -> Optional[float]:
    return None if None in (dividend, cash_per_share) else dividend + cash_per_share


def get_current_price(
    daily_low: Optional[float],
    previous_close: Optional[float],
    daily_high: Optional[float],
) -> float:
    return (
        daily_low or daily_high or previous_close
        if None in {daily_low, daily_high}
        else (daily_low + daily_high) / 2
    )


def compute_growth_rate(nums: List[float]) -> Optional[float]:
    """
    Computes average growth rate of a list of numbers based on the difference between the terminal and initial value.
    For lists of 21+ value computes this using the last 20 numbers. (Last 5 years of data)
    """
    if len(nums) > 20:
        nums = nums[-21:-1]

    return None if len(nums) < 2 else (nums[-1] / nums[0]) ** (1 / len(nums)) - 1


def get_dividend_growth_rate(dividends: Series) -> Optional[float]:
    if dividends.empty:
        return None
    dividends = dividends.tail(20)
    annual_growth_rates = dividends.pct_change().resample("YE").sum().dropna()
    return round(float(annual_growth_rates.mean()), 2)


def compute_wacc(
    total_debt, market_capital, interest_expense, tax_prevision, pre_tax_income, capm
) -> float:
    weight_of_equity = market_capital / (market_capital + total_debt)
    cost_of_debt = interest_expense / total_debt
    weight_of_debt = total_debt / (market_capital + total_debt)
    tax_rate = tax_prevision / pre_tax_income
    return round(
        (weight_of_equity * capm) + ((weight_of_debt * cost_of_debt) * (1 - tax_rate)),
        4,
    )


def get_capm(beta: Optional[float], risk_free_rate: float) -> Optional[float]:
    acceptable_ror = 0.1  # Expected Rate of Return for S&P500
    return (
        None
        if None in {beta, risk_free_rate}
        else round((risk_free_rate + beta * (acceptable_ror - risk_free_rate)), 4)
    )


def fetch_stock_data(ticker: str, risk_free_rate: float) -> StockData:
    """
    Tries to fetch all the needed information and save it inside a data class
    if a metric is not found saves None instead.
    """
    stock: Ticker = Ticker(ticker)
    stock_info = stock.info

    data: Dict[str, Optional[any]] = {
        metric: stock_info.get(metric)
        for metric in [
            "beta",
            "country",
            "sector",
            "industry",
            "shortName",
            "marketCap",
            "trailingEps",
            "dividendRate",
            "sharesOutstanding",
            "netIncomeToCommon",
            "totalCashPerShare",
            "bookValue",
        ]
    }

    data["riskFreeRate"] = risk_free_rate

    data["totalDividend"] = get_total_dividend(
        data["dividendRate"], data["totalCashPerShare"]
    )

    data["capm"] = get_capm(data["beta"], data["riskFreeRate"])

    data["currentPrice"] = get_current_price(
        stock_info.get("regularMarketDayLow"),
        stock_info.get("regularMarketPreviousClose"),
        stock_info.get("regularMarketDayHigh"),
    )

    income_statement = stock.income_stmt

    data["dividendGrowthRate"] = get_dividend_growth_rate(stock.dividends)

    data["ebitda"] = (
        None
        if "EBITDA" not in income_statement.index
        else income_statement.loc["EBITDA"].tolist()
    )

    data["earningsGrowth"] = compute_growth_rate(data["ebitda"]) or stock_info.get(
        "earningsGrowth"
    )

    if not income_statement.empty:
        latest_data = income_statement.keys()[0]
        data["interestExpense"] = income_statement[latest_data].get("Interest Expense")
        data["taxProvision"] = income_statement[latest_data].get("Tax Provision")
        data["pretaxIncome"] = income_statement[latest_data].get("Pretax Income")
    else:
        data["interestExpense"] = data["taxProvision"] = data["pretaxIncome"] = None

    balance_sheet = stock.balancesheet

    if not balance_sheet.empty:
        latest_data = balance_sheet.keys()[0]
        data["totalDebt"] = balance_sheet[latest_data].get(
            "Total Debt"
        ) or balance_sheet[latest_data].get("TotalDebt")
    else:
        data["totalDebt"] = None

    data["wacc"] = compute_wacc(
        data["totalDebt"],
        data["marketCap"],
        data["interestExpense"],
        data["taxProvision"],
        data["pretaxIncome"],
        data["capm"],
    )

    return StockData(**data)
