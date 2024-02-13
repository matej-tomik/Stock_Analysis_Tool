from classes import StockFinancials
from typing import List
import yfinance as yf


TREASURY_YLD_INDEX_TEN_YEAR: str = "^TNX"

def analyse_screen(file_name: str):
    with open(f'screens/{file_name}', 'r') as f:
        headers = f.readline()
        stocks = [stock.split(',') for stock in f.readlines()]

    result = open(f'results/{file_name[:-4]}_result.csv', 'w')
    failed = open(f'failed/{file_name[:-4]}_failed.csv', 'w')
    print('Graham number Result,DCF Advance Model Result,DDM Advance Model Result,DCF Simple Model Result,DDM Simple Model Result,Ticker symbol,Name,Market Cap, Country,Sector,Industry',file=result)
    print('Graham number Result,DCF Advance Model Result,DDM Advance Model Result,DCF Simple Model Result,DDM Simple Model Result,Ticker symbol,Name,Market Cap, Country,Sector,Industry',file=failed)

    # file_objects = {}
    # for file_type in ['result', 'failed']:
    #     with open(f'{file_type}s/{file_name[:-4]}_{file_type}.csv', 'w') as file:
    #         file_objects[file_type] = file
    #         print('Graham number Result,DCF Model Result,DDM Model Result,Ticker symbol,Name,Market Cap, Country,Sector,Industry',file=file)
    # result = file_objects['result']
    # failed = file_objects['failed']
    risk_free_rate: float = yf.Ticker(TREASURY_YLD_INDEX_TEN_YEAR).info.get('regularMarketPreviousClose',0.04) / 100  # constant 0.04 get from sqeel ; )
    for stock in stocks:
        analysed_stock = analyse_stock(stock[0], risk_free_rate)
        file = failed
        if [*analysed_stock.values()][:5].count('N/A') <= 2:
            file = result
        print(','.join([str(value) for value in [*analysed_stock.values()]]), file=file)


def get_screens() -> List[str]:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    screens_directory = os.path.join(current_directory, "screens")
    return [file for file in os.listdir(screens_directory) if os.path.isfile(os.path.join(screens_directory, file))]


def main():
    if __name__ == '__main__':
        screens_to_run = get_screens()

        for screen in screens_to_run:
            analyse_screen(screen)
main()