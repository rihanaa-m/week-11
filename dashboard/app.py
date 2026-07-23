"""
Ethiopia Financial Inclusion Forecasting Dashboard

This Streamlit dashboard provides interactive visualization of the financial inclusion
forecasting system for Ethiopia.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Page configuration
st.set_page_config(
    page_title="Ethiopia FI Forecast",
    page_icon="🇪🇹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e3a8a;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    .insight-box {
        background-color: #f0f9ff;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load all necessary data for the dashboard."""
    try:
        # Try to load processed data
        data_path = '../data/processed/ethiopia_fi_unified_data_enriched.csv'
        forecast_path = '../data/processed/forecast_summary.csv'
        
        if os.path.exists(data_path):
            data_df = pd.read_csv(data_path)
            data_df['observation_date'] = pd.to_datetime(data_df['observation_date'], errors='coerce')
        else:
            # Create sample data if processed data not available
            data_df = create_sample_data()
        
        if os.path.exists(forecast_path):
            forecast_df = pd.read_csv(forecast_path)
        else:
            forecast_df = create_sample_forecast()
            
        return data_df, forecast_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return create_sample_data(), create_sample_forecast()

def create_sample_data():
    """Create sample data for demonstration."""
    dates = pd.date_range('2011-12-31', periods=14, freq='365D')
    account_ownership = [14, 22, 35, 46, 49, 51, 54, 56.5]
    digital_payments = [5, 10, 18, 25, 35, 39, 44, 48.5]
    
    data = []
    for i, date in enumerate(dates):
        if i < len(account_ownership):
            data.append({
                'observation_date': date,
                'indicator_code': 'ACC_OWNERSHIP',
                'value_numeric': account_ownership[i],
                'record_type': 'observation'
            })
        if i < len(digital_payments):
            data.append({
                'observation_date': date,
                'indicator_code': 'USG_DIGITAL_PAYMENT',
                'value_numeric': digital_payments[i],
                'record_type': 'observation'
            })
    
    return pd.DataFrame(data)

def create_sample_forecast():
    """Create sample forecast data for demonstration."""
    scenarios = ['optimistic', 'base', 'pessimistic']
    targets = ['ACCESS', 'USAGE']
    years = [2025, 2026, 2027]
    
    data = []
    for target in targets:
        for scenario in scenarios:
            for year in years:
                if target == 'ACCESS':
                    base_val = 51 + (year - 2025) * 2.5
                    if scenario == 'optimistic':
                        forecast = base_val * 1.1
                    elif scenario == 'pessimistic':
                        forecast = base_val * 0.9
                    else:
                        forecast = base_val
                else:
                    base_val = 39 + (year - 2025) * 4.5
                    if scenario == 'optimistic':
                        forecast = base_val * 1.1
                    elif scenario == 'pessimistic':
                        forecast = base_val * 0.9
                    else:
                        forecast = base_val
                
                data.append({
                    'target': target,
                    'scenario': scenario,
                    'year': year,
                    'forecast': forecast,
                    'trend': base_val,
                    'event_impact': forecast - base_val
                })
    
    return pd.DataFrame(data)

# Main navigation
def main():
    data_df, forecast_df = load_data()
    
    # Sidebar navigation
    st.sidebar.title("🇪🇹 Ethiopia FI Forecast")
    st.sidebar.markdown("---")
    
    page = st.sidebar.radio(
        "Navigate to:",
        ["Overview", "Trends", "Forecasts", "Data Explorer"]
    )
    
    if page == "Overview":
        overview_page(data_df, forecast_df)
    elif page == "Trends":
        trends_page(data_df)
    elif page == "Forecasts":
        forecasts_page(forecast_df)
    elif page == "Data Explorer":
        data_explorer_page(data_df)

def overview_page(data_df, forecast_df):
    """Overview page with key metrics and insights."""
    st.markdown('<h1 class="main-header">Ethiopia Financial Inclusion Overview</h1>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Account Ownership (2024)",
            value="49%",
            delta="+3 pp vs 2021",
            help="Percentage of adults with account at financial institution or mobile money"
        )
    
    with col2:
        st.metric(
            label="Digital Payment Usage (2024)",
            value="35%",
            delta="+10 pp vs 2021",
            help="Percentage of adults who made or received digital payment"
        )
    
    with col3:
        st.metric(
            label="Mobile Money Accounts",
            value="9.45%",
            delta="+4.75 pp vs 2021",
            help="Percentage of adults with mobile money account"
        )
    
    with col4:
        st.metric(
            label="4G Coverage",
            value="70.8%",
            delta="+33.3 pp vs 2023",
            help="Percentage of population with 4G coverage"
        )
    
    st.markdown("---")
    
    # Key insights
    st.subheader("🔍 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
            <h3>Account Ownership Growth</h3>
            <p>Ethiopia's account ownership grew from 14% (2011) to 49% (2024), 
            but growth slowed to +3pp in 2021-2024 despite mobile money expansion.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-box">
            <h3>Digital Payment Acceleration</h3>
            <p>Digital payment usage reached 35% in 2024, with strong growth driven 
            by P2P transactions and smartphone adoption.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
            <h3>Infrastructure Investment</h3>
            <p>4G coverage nearly doubled from 37.5% to 70.8%, enabling digital service 
            adoption across the country.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-box">
            <h3>Event-Driven Growth</h3>
            <p>Key events like Telebirr launch, M-Pesa entry, and Fayda digital ID 
            are driving financial inclusion transformation.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Forecast summary
    st.subheader("📊 2027 Forecast Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Account Ownership Forecast**
        - Base case: 56.5%
        - Optimistic: 62.0%
        - Pessimistic: 51.0%
        - Target: 60%
        """)
    
    with col2:
        st.info("""
        **Digital Payment Usage Forecast**
        - Base case: 48.5%
        - Optimistic: 54.0%
        - Pessimistic: 43.0%
        - Target: 50%
        """)
    
    st.markdown("---")
    
    # Event timeline
    st.subheader("📅 Key Events Timeline")
    
    events_data = {
        'Event': ['NBE MM Regulation', 'Telebirr Launch', 'NFIS-II Launch', 'Safaricom Entry', 
                 '4G Expansion', 'M-Pesa Launch', 'Fayda Rollout', 'FX Reform', 'P2P > ATM'],
        'Date': ['2020-03', '2021-05', '2021-09', '2022-08', '2023-01', '2023-08', '2024-01', '2024-07', '2024-10'],
        'Category': ['Regulation', 'Product Launch', 'Policy', 'Market Entry', 'Infrastructure', 
                    'Product Launch', 'Infrastructure', 'Policy', 'Milestone']
    }
    
    events_df = pd.DataFrame(events_data)
    events_df['Date'] = pd.to_datetime(events_df['Date'])
    
    fig = px.timeline(events_df, x_start="Date", y="Event", color="Category",
                     title="Financial Inclusion Events Timeline")
    fig.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(fig, use_container_width=True)

def trends_page(data_df):
    """Trends page with historical data visualization."""
    st.markdown('<h1 class="main-header">Historical Trends Analysis</h1>', unsafe_allow_html=True)
    
    # Account ownership trend
    st.subheader("Account Ownership Trajectory (2011-2024)")
    
    access_data = data_df[data_df['indicator_code'] == 'ACC_OWNERSHIP'].copy()
    if len(access_data) > 0:
        access_data = access_data.sort_values('observation_date')
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=access_data['observation_date'],
            y=access_data['value_numeric'],
            mode='lines+markers',
            name='Account Ownership',
            line=dict(color='#3b82f6', width=3),
            marker=dict(size=8)
        ))
        
        fig.add_hline(y=60, line_dash="dash", line_color="red", 
                    annotation_text="NFIS-II Target (60%)")
        
        fig.update_layout(
            title="Ethiopia Account Ownership Rate",
            xaxis_title="Year",
            yaxis_title="Account Ownership Rate (%)",
            yaxis_range=[0, 70],
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Digital payment trend
    st.subheader("Digital Payment Usage Trend")
    
    usage_data = data_df[data_df['indicator_code'] == 'USG_DIGITAL_PAYMENT'].copy()
    if len(usage_data) > 0:
        usage_data = usage_data.sort_values('observation_date')
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=usage_data['observation_date'],
            y=usage_data['value_numeric'],
            mode='lines+markers',
            name='Digital Payment Usage',
            line=dict(color='#10b981', width=3),
            marker=dict(size=8)
        ))
        
        fig.add_hline(y=50, line_dash="dash", line_color="red",
                    annotation_text="Target (50%)")
        
        fig.update_layout(
            title="Ethiopia Digital Payment Usage Rate",
            xaxis_title="Year",
            yaxis_title="Digital Payment Usage (%)",
            yaxis_range=[0, 60],
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Growth rates
    st.subheader("Growth Rate Analysis")
    
    if len(access_data) > 1:
        access_data = access_data.sort_values('observation_date')
        access_data['year'] = access_data['observation_date'].dt.year
        access_data['growth'] = access_data['value_numeric'].diff()
        
        growth_data = access_data.dropna()
        
        fig = px.bar(growth_data, x='year', y='growth',
                    title='Account Ownership Growth Rate (percentage points)',
                    labels={'growth': 'Growth (pp)', 'year': 'Year'},
                    color='growth',
                    color_continuous_scale='RdYlGn')
        st.plotly_chart(fig, use_container_width=True)

def forecasts_page(forecast_df):
    """Forecasts page with scenario analysis."""
    st.markdown('<h1 class="main-header">Financial Inclusion Forecasts</h1>', unsafe_allow_html=True)
    
    # Scenario selector
    scenario = st.selectbox(
        "Select Scenario",
        ["base", "optimistic", "pessimistic"],
        help="Choose forecast scenario based on event effectiveness assumptions"
    )
    
    # Account ownership forecast
    st.subheader("Account Ownership Forecast (2025-2027)")
    
    access_forecast = forecast_df[
        (forecast_df['target'] == 'ACCESS') & 
        (forecast_df['scenario'] == scenario)
    ].copy()
    
    if len(access_forecast) > 0:
        fig = go.Figure()
        
        # Historical data point
        fig.add_trace(go.Scatter(
            x=[2024], y=[49],
            mode='markers',
            name='Current (2024)',
            marker=dict(size=15, color='#3b82f6')
        ))
        
        # Forecast line
        fig.add_trace(go.Scatter(
            x=access_forecast['year'],
            y=access_forecast['forecast'],
            mode='lines+markers',
            name=f'{scenario.capitalize()} Forecast',
            line=dict(color='#10b981', width=3),
            marker=dict(size=10)
        ))
        
        # Target line
        fig.add_hline(y=60, line_dash="dash", line_color="red",
                    annotation_text="NFIS-II Target (60%)")
        
        fig.update_layout(
            title=f"Account Ownership Forecast - {scenario.capitalize()} Scenario",
            xaxis_title="Year",
            yaxis_title="Account Ownership Rate (%)",
            yaxis_range=[40, 70],
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Forecast table
        st.subheader("Forecast Values")
        st.dataframe(
            access_forecast[['year', 'forecast', 'trend', 'event_impact']].round(1),
            hide_index=True,
            use_container_width=True
        )
    
    # Digital payment forecast
    st.subheader("Digital Payment Usage Forecast (2025-2027)")
    
    usage_forecast = forecast_df[
        (forecast_df['target'] == 'USAGE') & 
        (forecast_df['scenario'] == scenario)
    ].copy()
    
    if len(usage_forecast) > 0:
        fig = go.Figure()
        
        # Historical data point
        fig.add_trace(go.Scatter(
            x=[2024], y=[35],
            mode='markers',
            name='Current (2024)',
            marker=dict(size=15, color='#3b82f6')
        ))
        
        # Forecast line
        fig.add_trace(go.Scatter(
            x=usage_forecast['year'],
            y=usage_forecast['forecast'],
            mode='lines+markers',
            name=f'{scenario.capitalize()} Forecast',
            line=dict(color='#f59e0b', width=3),
            marker=dict(size=10)
        ))
        
        # Target line
        fig.add_hline(y=50, line_dash="dash", line_color="red",
                    annotation_text="Target (50%)")
        
        fig.update_layout(
            title=f"Digital Payment Usage Forecast - {scenario.capitalize()} Scenario",
            xaxis_title="Year",
            yaxis_title="Digital Payment Usage (%)",
            yaxis_range=[25, 60],
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Forecast table
        st.subheader("Forecast Values")
        st.dataframe(
            usage_forecast[['year', 'forecast', 'trend', 'event_impact']].round(1),
            hide_index=True,
            use_container_width=True
        )
    
    # Scenario comparison
    st.subheader("Scenario Comparison")
    
    scenario_comparison = forecast_df[forecast_df['year'] == 2027].pivot(
        index='target', columns='scenario', values='forecast'
    )
    
    st.dataframe(
        scenario_comparison.round(1),
        use_container_width=True
    )

def data_explorer_page(data_df):
    """Data explorer page for detailed data analysis."""
    st.markdown('<h1 class="main-header">Data Explorer</h1>', unsafe_allow_html=True)
    
    # Data filters
    st.sidebar.subheader("Data Filters")
    
    record_types = data_df['record_type'].unique()
    selected_record_type = st.sidebar.selectbox(
        "Record Type",
        options=["All"] + list(record_types)
    )
    
    if selected_record_type != "All":
        filtered_data = data_df[data_df['record_type'] == selected_record_type]
    else:
        filtered_data = data_df
    
    # Data summary
    st.subheader("Data Summary")
    st.write(f"Total records: {len(filtered_data)}")
    st.write(f"Date range: {filtered_data['observation_date'].min()} to {filtered_data['observation_date'].max()}")
    
    # Data table
    st.subheader("Data Table")
    
    display_columns = ['observation_date', 'record_type', 'indicator_code', 'value_numeric', 'source_name']
    available_columns = [col for col in display_columns if col in filtered_data.columns]
    
    st.dataframe(
        filtered_data[available_columns].sort_values('observation_date', ascending=False),
        use_container_width=True
    )
    
    # Download button
    st.subheader("Download Data")
    csv = filtered_data.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='ethiopia_fi_data.csv',
        mime='text/csv'
    )

if __name__ == "__main__":
    main()
