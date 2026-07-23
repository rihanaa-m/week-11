# Ethiopia Financial Inclusion Forecasting System

A comprehensive forecasting system that tracks Ethiopia's digital financial transformation using time series methods and event-driven modeling.

## Project Overview

This project was developed for the 10 Academy Week 11 Challenge to build a forecasting system that predicts Ethiopia's progress on two core dimensions of financial inclusion as defined by the World Bank's Global Findex:

1. **Access** — Account Ownership Rate
2. **Usage** — Digital Payment Adoption Rate

## Project Structure

```
ethiopia-fi-forecast/
├── .github/workflows/
│   └── unittests.yml          # GitHub Actions for unit testing
├── data/
│   ├── raw/                   # Original dataset files
│   └── processed/             # Analysis-ready enriched data
├── notebooks/
│   ├── task1_data_exploration.ipynb    # Data exploration and enrichment
│   ├── task2_eda.ipynb                # Exploratory data analysis
│   ├── task3_impact_modeling.ipynb    # Event impact modeling
│   └── task4_forecasting.ipynb        # Forecasting with scenarios
├── src/
│   ├── __init__.py
│   └── impact_model.py                # Event impact modeling module
├── dashboard/
│   ├── app.py                         # Streamlit dashboard
│   └── README.md                      # Dashboard documentation
├── tests/
│   └── __init__.py
├── models/                            # Saved model files
├── reports/
│   └── figures/                       # Generated visualizations
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rihanaa-m/week-11.git
cd week-11
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Dashboard

The interactive Streamlit dashboard provides visualization of the forecasting system:

```bash
cd dashboard
streamlit run app.py
```

The dashboard will open at `http://localhost:8501` with four pages:
- **Overview**: Key metrics, insights, and event timeline
- **Trends**: Historical data visualization and growth analysis
- **Forecasts**: Scenario-based forecasting with confidence intervals
- **Data Explorer**: Detailed data exploration and download functionality

### Running Analysis Notebooks

To run the Jupyter notebooks:

```bash
jupyter notebook notebooks/
```

Available notebooks:
- `task1_data_exploration.ipynb`: Data exploration and enrichment
- `task2_eda.ipynb`: Exploratory data analysis
- `task3_impact_modeling.ipynb`: Event impact modeling
- `task4_forecasting.ipynb`: Forecasting with scenarios

## Key Features

### Data Enrichment
- Extended temporal coverage from 2014 back to 2011
- Added infrastructure enablers (smartphones, 4G, agents)
- Included core usage indicators for forecasting
- Captured critical regulatory and infrastructure events

### Event Impact Modeling
- Event-indicator association matrix
- Comparable country evidence (Kenya, India, Rwanda)
- Validation against historical data
- Refined impact estimates based on empirical validation

### Forecasting
- Event-augmented modeling approach
- Scenario analysis (optimistic, base, pessimistic)
- Confidence intervals for uncertainty quantification
- Forecasts for 2025-2027

### Interactive Dashboard
- Real-time data visualization
- Scenario selection and comparison
- Historical trend analysis
- Data download functionality

## Forecast Results

### Account Ownership (Access)
- **Current (2024)**: 49%
- **Base Forecast 2027**: 56.5% (95% CI: 51.0-62.0%)
- **NFIS-II Target**: 60%
- **Status**: Below target but closing gap

### Digital Payment Usage
- **Current (2024)**: 35%
- **Base Forecast 2027**: 48.5% (95% CI: 43.0-54.0%)
- **Target**: 50%
- **Status**: On track to meet target

## Key Insights

1. **Account Ownership Slowdown**: Despite massive mobile money expansion, account ownership grew only +3pp (2021-2024), suggesting registered vs. active gaps or definition issues.

2. **Infrastructure-Led Growth**: 4G coverage nearly doubled (37.5% → 70.8%), enabling digital service adoption with strong multiplier effects.

3. **Event-Driven Development**: Clear sequence of regulatory enablers, product launches, and infrastructure investments driving market development.

4. **Gender Gap Remains**: 20pp gender gap in account ownership (56% male vs 36% female in 2021), with digital ID expected to reduce this gap.

5. **P2P-Dominant Market**: Ethiopia's unique P2P usage for commerce, not just transfers, differentiates it from other markets.

## Methodology

### Approach
- **Event-Augmented Modeling**: Combines trend analysis with event impact modeling
- **Scenario Analysis**: Optimistic, base, and pessimistic scenarios for uncertainty quantification
- **Evidence-Based**: Impact estimates based on empirical data and comparable country evidence

### Validation
- Telebirr impact validated against account ownership changes
- 4G expansion impact validated against coverage growth
- Mobile money growth compared with modeled impacts
- Estimates refined based on empirical validation

### Limitations
- Sparse historical data limits model precision
- Event effectiveness assumptions based on limited validation
- External factors (economic shocks, policy changes) not fully modeled
- Definition mismatches between data sources

## Technologies Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **Streamlit**: Dashboard development
- **Scikit-learn**: Machine learning for trend analysis
- **Statsmodels**: Statistical modeling
- **Jupyter**: Notebook development

## Data Sources

- **Global Findex Database**: World Bank financial inclusion surveys
- **GSMA**: Mobile industry data and reports
- **National Bank of Ethiopia**: Regulatory data and reports
- **Ethio Telecom**: Operator data and infrastructure metrics
- **Research Studies**: Academic and think tank reports

## Contributors

- **Devin**: AI-powered development assistant
- **10 Academy**: Challenge organizers and mentors

## License

This project was developed for educational purposes as part of the 10 Academy Week 11 Challenge.

## Acknowledgments

- 10 Academy for the challenge opportunity
- World Bank for Global Findex data
- GSMA for mobile industry insights
- National Bank of Ethiopia for regulatory context

## Contact

For questions or feedback about this project, please open an issue on GitHub.

---

**Generated with [Devin](https://devin.ai)**
