from classes import StockFinancials
from typing import List
import yfinance as yf


TREASURY_YLD_INDEX_TEN_YEAR: str = "^TNX"

#

test = True
test = not test

if test:
    risk_free_rate: float = yf.Ticker(TREASURY_YLD_INDEX_TEN_YEAR).info.get('regularMarketPreviousClose',
                                                                     0.04) / 100  # constant 0.04 get from sqeel ; )
    security = StockFinancials('AACG',risk_free_rate)
    print(
        security.graham_result,
        security.dcf_result,
        security.ddm_result,
        security.ticker,
        security.name,
        security.market_capital,
        security.country,
        security.sector,
        security.industry
    )
else:
    with open('screens/data.csv', 'r') as f:
        headers = f.readline()
        stocks = [stock.split(',') for stock in f.readlines()]

    risk_free_rate: float = yf.Ticker(TREASURY_YLD_INDEX_TEN_YEAR).info.get('regularMarketPreviousClose', 0.04) / 100  # constant 0.04 get from sqeel ; )
    with open('results/result.csv', 'w') as f:
        print('Graham number Result,DCF Model Result,DDM Model Result,Ticker symbol,Name,Market Cap, Country,Sector,Industry',file=f)

        failed_stocks: List[List[str]] = []
        for stock in stocks:
            ticker = stock[0]

            try:
                security = StockFinancials(ticker,risk_free_rate)
                print(
                    ','.join(
                        [
                            str(value) for value in (
                                security.graham_result,
                                security.dcf_result,
                                security.ddm_result,
                                security.ticker,
                                security.name,
                                security.market_capital,
                                security.country,
                                security.sector,
                                security.industry
                            )
                        ]
                    ),file=f
                )
            except:
                failed_stocks.append([stock[0], stock[1]])
                print([stock[0], stock[1]])
    print('stock fail happens when there is no income statement, balance sheet, info or the ticker is invalid')
    print(failed_stocks)

# if __name__ == '__main__':
#

