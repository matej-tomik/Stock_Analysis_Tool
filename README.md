# Stock Analysis Tool

## Application Description
Our application provides simplified stock analysis using three popular valuation models: Discounted Cash Flow (DCF), Dividend Discount Model (DDM), and Graham Number/Model.

### Features:
1. **DCF Analysis:** Estimate the intrinsic value of a stock based on projected future cash flows. Input key financial metrics and growth assumptions, and the DCF model calculates a fair value estimate.
2. **DDM Analysis:** Evaluate a stock's worth based on expected future dividend payments. Input dividend yield, growth rate, and discount rate to obtain a valuation.
3. **Graham Number:** Assess whether a stock is undervalued based on earnings per share (EPS) and book value per share (BVPS), named after renowned investor Benjamin Graham.

## Usage
To use the application, follow these steps:
1. Clone the repository to your local machine.
2. Open the project in your preferred IDE.
3. Run the application.
4. Input the necessary parameters for the analysis you want to perform.
5. Review the valuation results.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

## Test file example
```Python
from classes import StockValuation
import yfinance as yf


TREASURY_YLD_INDEX_TEN_YEAR: str = "^TNX"


def get_risk_free_rate() -> float:
    return round(yf.Ticker(TREASURY_YLD_INDEX_TEN_YEAR).info.get('regularMarketPreviousClose', 0.04) / 100, 4)


security = StockValuation("AAPL", get_risk_free_rate())
security.fetch_data()
security.evaluate()
print(security.result_set)  # [dcf, dcf_advanced, ddm, ddm_advanced, graham_num, graham,]
```
## License
This project is licensed under the [MIT License](https://opensource.org/license/mit)).

## Contact
For any inquiries or support, please contact [Matěj Tomík](mailto:mtomik.work@gmail.com).

