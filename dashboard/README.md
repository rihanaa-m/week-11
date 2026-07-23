# Ethiopia Financial Inclusion Forecasting Dashboard

Interactive Streamlit dashboard for exploring Ethiopia's financial inclusion data and forecasts.

## Features

- **Overview Page**: Key metrics, insights, and event timeline
- **Trends Page**: Historical data visualization and growth analysis
- **Forecasts Page**: Scenario-based forecasting with confidence intervals
- **Data Explorer**: Detailed data exploration and download functionality

## Installation

1. Install dependencies:
```bash
pip install -r ../requirements.txt
```

2. Run the dashboard:
```bash
streamlit run app.py
```

## Usage

The dashboard will open in your web browser at `http://localhost:8501`

Navigate between pages using the sidebar:
- **Overview**: High-level summary and key insights
- **Trends**: Historical trend analysis
- **Forecasts**: Future projections with scenarios
- **Data Explorer**: Detailed data exploration

## Data

The dashboard uses processed data from `../data/processed/`:
- `ethiopia_fi_unified_data_enriched.csv`: Historical observations and events
- `forecast_summary.csv`: Forecast results with scenarios

If processed data is not available, the dashboard will use sample data for demonstration.

## Scenarios

The forecasting module includes three scenarios:
- **Optimistic**: Events are 30% more effective than expected
- **Base**: Expected event effectiveness based on historical validation
- **Pessimistic**: Events are 30% less effective than expected

## Development

To modify the dashboard:
1. Edit `app.py` for main functionality
2. Add new pages by creating functions and adding to navigation
3. Customize styling in the CSS section
4. Update data loading functions as needed

## Notes

- The dashboard is designed for demonstration and educational purposes
- Forecasts should be used as directional indicators, not precise predictions
- Data limitations are documented in the forecasting notebook
