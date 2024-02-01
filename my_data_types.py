from typing import Tuple,Optional

Sector = str
Industry = str
Country = str
Name = str
MarketCapital = float
Dividend = float
SharesOutstanding = int
NetIncome = int
DividendGrowthRate = float
Capm = float
GrowthRate = float
EarningsPerShare = float
Wacc = float
BookValuePerShare = float

MainInfo = Tuple[Optional[Sector], Optional[Industry], Optional[Country], Optional[Name], Optional[MarketCapital]]
DdmData = Optional[Tuple[Dividend, SharesOutstanding, NetIncome, DividendGrowthRate, Capm, GrowthRate]]
DcfData = Optional[Tuple[EarningsPerShare, Wacc, GrowthRate]]
GrahamNumberData = Optional[Tuple[EarningsPerShare, BookValuePerShare]]
