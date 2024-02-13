from classes import StockData
from math import sqrt

"""""
TODO: Switch from links to screenshots of the models in the repo. You can create links to the files. It would be epic.
External sites can change over time..

sources of the model computations

dcf_advance is according to https://www.gurufocus.com/term/iv_dcf/AAPL/Intrinsic-Value:-DCF-(FCF-Based)/Apple

# TODO: Fix link and find proper model.
dcf_simple  is according to https://finbox.com/NASDAQGS:AAPL/models/ddm-sg/ without calculating cash per share and 

ddm_advance is according to https://finbox.com/NASDAQGS:AAPL/models/ddm-sg/

ddm_simple is according to https://www.investopedia.com/terms/d/ddm.asp in section Examples of the DDM

graham_number it simply according to google
""" ""


def dcf_advanced(
    data: StockData, year: int = 10, terminal_growth_rate: float = 0.04
) -> float:
    wacc = data.wacc
    growth_rate = data.earningsGrowth
    earnings_per_share = data.trailingEps

    if growth_rate < 0.05:
        growth_rate = 0.05
    x = 0
    for n in range(1, year + 1):
        x += ((1 + growth_rate) ** n) / ((1 + wacc) ** n)
    y = 0
    for n in range(1, year + 1):
        y += ((1 + terminal_growth_rate) ** n) / ((1 + wacc) ** n)

    return round(
        earnings_per_share * (x + ((1 + growth_rate) ** 10) / ((1 + wacc) ** 10) * y), 2
    )


def dcf(
    data: StockData, year: int = 10, terminal_growth_rate: float = 0.04
) -> float:
    camp = data.capm
    growth_rate = data.earningsGrowth
    earnings_per_share = data.trailingEps

    if growth_rate < 0.05:
        growth_rate = 0.05
    x = 0
    for n in range(1, year + 1):
        x += ((1 + growth_rate) ** n) / ((1 + camp) ** n)
    y = 0
    for n in range(1, year + 1):
        y += ((1 + terminal_growth_rate) ** n) / ((1 + camp) ** n)

    return round(
        earnings_per_share * (x + ((1 + growth_rate) ** 10) / ((1 + camp) ** 10) * y), 2
    )


def ddm_advanced(
    data: StockData,
) -> float:
    dividend: float = data.dividendRate
    shares_outstanding: int = data.sharesOutstanding
    net_income: int = data.netIncomeToCommon

    cash_retained = net_income - shares_outstanding * dividend
    required_retention_ratio = [
        0.2,
        0.125,
        0.075,
    ]  # % net income needed for future growth  20% LOW 12.5% MID 7.5% HIGH
    excess_retained = [
        (cash_retained - net_income * required_retention_ratio[x]) / shares_outstanding
        for x in range(3)
    ]
    adjusted_dividend = [dividend + excess_retained[x] for x in range(3)]
    ddm_results = [
        (adjusted_dividend[x] * (1 + data.dividendGrowthRate) / data.capm)
        - data.earningsGrowth
        for x in range(3)
    ]

    return round(sum(ddm_results) / len(ddm_results), 2)


def ddm(data: StockData) -> float:
    return round(
        (data.totalDividend * (1 + data.dividendGrowthRate))
        / (data.capm - data.dividendGrowthRate),
        2,
    )


def graham(data: StockData) -> float:
    return round(sqrt(max(22.5 * data.trailingEps * data.bookValue, 0)), 2)


def graham2(data: StockData) -> float:
    growth_rate = max(data.earningsGrowth, 0.05)
    return round(
        (data.trailingEps * (7 + growth_rate * 100) * 4.4) / (data.riskFreeRate * 100),
        2,
    )
