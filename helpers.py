from typing import Union, Literal


dataset_dcf = ["trailingEps", "capm", "earningsGrowth"]
dataset_dcf_advanced = ["trailingEps", "wacc", "earningsGrowth"]
dataset_ddm = ["totalDividend", "totalDividend", "capm"]
dataset_ddm_advanced = [
    "dividendRate",
    "sharesOutstanding",
    "netIncomeToCommon",
    "dividendGrowthRate",
    "capm",
    "earningsGrowth",
]
dataset_graham = ["trailingEps", "bookValue"]
dataset_graham2 = ["trailingEps", "earningsGrowth", "riskFreeRate"]


validation_datasets = [
    dataset_dcf,
    dataset_dcf_advanced,
    dataset_ddm,
    dataset_ddm_advanced,
    dataset_graham,
    dataset_graham2,
]

Result: Union[float, Literal["N/A"]] = "N/A"
