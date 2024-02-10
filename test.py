from classes import StockValuation
from yfinance import Ticker


risk_free_rate: float = (
    Ticker("^TNX").info.get("regularMarketPreviousClose", 4.17) / 100
)  # TREASURY_YLD_INDEX_TEN_YEAR


stock = StockValuation("AAPL", risk_free_rate)
stock.fetch_data()
stock.evaluate()

print(stock.result_set)
