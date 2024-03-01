from dataclasses import dataclass
from typing import Optional, List


@dataclass
class StockData:
    beta: Optional[float] = None
    bookValue: Optional[float] = None
    capm: Optional[float] = None
    country: Optional[str] = "N/A"
    currentPrice: Optional[float] = None
    dividendGrowthRate: Optional[float] = None
    dividendRate: Optional[float] = None
    earningsGrowth: Optional[float] = None
    ebitda: Optional[List[int]] = None
    industry: Optional[str] = "N/A"
    interestExpense: Optional[int] = None
    marketCap: Optional[int] = None
    netIncomeToCommon: Optional[int] = None
    pretaxIncome: Optional[int] = None
    riskFreeRate: Optional[float] = 0.0417
    sector: Optional[str] = "N/A"
    sharesOutstanding: Optional[int] = None
    shortName: Optional[str] = "N/A"
    taxProvision: Optional[int] = None
    totalCashPerShare: Optional[float] = None
    totalDebt: Optional[int] = None
    totalDividend: Optional[float] = None
    trailingEps: Optional[float] = None
    wacc: Optional[float] = None
    discountRate: Optional[float] = None

    def to_dict(self):
        return {
            "beta": self.beta,
            "country": self.country,
            "sector": self.sector,
            "industry": self.industry,
            "shortName": self.shortName,
            "marketCap": self.marketCap,
            "trailingEps": self.trailingEps,
            "dividendRate": self.dividendRate,
            "sharesOutstanding": self.sharesOutstanding,
            "netIncomeToCommon": self.netIncomeToCommon,
            "totalCashPerShare": self.totalCashPerShare,
            "bookValue": self.bookValue,
            "riskFreeRate": self.riskFreeRate,
            "totalDividend": self.totalDividend,
            "capm": self.capm,
            "currentPrice": self.currentPrice,
            "dividendGrowthRate": self.dividendGrowthRate,
            "ebitda": self.ebitda,
            "earningsGrowth": self.earningsGrowth,
            "interestExpense": self.interestExpense,
            "taxProvision": self.taxProvision,
            "pretaxIncome": self.pretaxIncome,
            "totalDebt": self.totalDebt,
            "wacc": self.wacc,
            "discountRate": self.discountRate,
        }

    def validate_result(self, evaluation_dataset: List[str]) -> bool:
        return all(self.to_dict()[metric] is not None for metric in evaluation_dataset)


class StockValuation:
    def __init__(self, ticker: str, risk_free_rate: float):
        self.ticker = ticker
        self.risk_free_rate = risk_free_rate

        self.data = (
            self.result_set
        ) = (
            self.dcf_advanced
        ) = (
            self.dcf
        ) = self.ddm = self.ddm_advanced = self.graham_num = self.graham = None

    def fetch_data(self):
        from data_digger import fetch_stock_data
        self.data: StockData = fetch_stock_data(self.ticker, self.risk_free_rate)

    def evaluate(self):
        from helpers import Result, validation_datasets
        from stock_evaluation_models import dcf, dcf_advanced, ddm, ddm_advanced, graham_num, graham
        evaluation_models = (
            dcf,
            dcf_advanced,
            ddm,
            ddm_advanced,
            graham_num,
            graham,
        )
        self.result_set: List[Result] = [
            evaluation_models[i](self.data)
            if self.data.validate_result(validation_datasets[i])
            else "N/A"
            for i in range(len(validation_datasets))
        ]

        (
            self.dcf,
            self.dcf_advanced,
            self.ddm,
            self.ddm_advanced,
            self.graham_num,
            self.graham,
        ) = self.result_set
