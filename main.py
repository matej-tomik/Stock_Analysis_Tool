from classes import StockValuation
from typing import List
import os

# TODO: Fix main and implement nicer logic and runners


def analyse_screen(file_name: str):
    with open(f"screens/{file_name}", "r") as f:
        headers = f.readline()
        stocks = [stock.split(",") for stock in f.readlines()]

    result = open(f"results/{file_name[:-4]}_result.csv", "w")
    failed = open(f"failed/{file_name[:-4]}_failed.csv", "w")
    print(
        "Graham number Result,DCF Advance Model Result,DDM Advance Model Result,DCF Simple Model Result,DDM Simple Model Result,Ticker symbol,Name,Market Cap, Country,Sector,Industry",
        file=result,
    )
    print(
        "Graham number Result,DCF Advance Model Result,DDM Advance Model Result,DCF Simple Model Result,DDM Simple Model Result,Ticker symbol,Name,Market Cap, Country,Sector,Industry",
        file=failed,
    )

    for stock in stocks:
        analysed_stock = StockValuation(stock[0], risk_free_rate)
        results = [
            analysed_stock.graham_result,
            analysed_stock.dcf_simple_result,
            analysed_stock.ddm_simple_result,
            analysed_stock.ddm_advance_result,
            analysed_stock.dcf_advance_result,
        ]
        file = failed if results.count("N/A") > 4 else result
        print(",".join([str(value) for value in results]), file=file)


def get_screens() -> List[str]:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    screens_directory = os.path.join(current_directory, "screens")
    return [
        file
        for file in os.listdir(screens_directory)
        if os.path.isfile(os.path.join(screens_directory, file))
    ]


def main():
    if __name__ == "__main__":
        screens_to_run = get_screens()

        for screen in screens_to_run:
            analyse_screen(screen)


main()
