import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 1000)

# Load the data
data_path = r'C:\Users\hp\Desktop\week 11\data\raw\ethiopia_fi_unified_data.xlsx'
ref_path = r'C:\Users\hp\Desktop\week 11\data\raw\reference_codes.xlsx'

# Read all sheets
data_df = pd.read_excel(data_path, sheet_name='ethiopia_fi_unified_data')
impact_links_df = pd.read_excel(data_path, sheet_name='Impact_sheet')
ref_codes_df = pd.read_excel(ref_path)

print("Data loaded successfully!")
print(f"\nData sheet shape: {data_df.shape}")
print(f"Impact links sheet shape: {impact_links_df.shape}")
print(f"Reference codes shape: {ref_codes_df.shape}")

print("\n" + "="*80)
print("DATA SHEET COLUMNS")
print("="*80)
print(data_df.columns.tolist())

print("\n" + "="*80)
print("FIRST 10 ROWS OF DATA")
print("="*80)
print(data_df.head(10))

print("\n" + "="*80)
print("IMPACT LINKS COLUMNS")
print("="*80)
print(impact_links_df.columns.tolist())

print("\n" + "="*80)
print("FIRST 10 ROWS OF IMPACT LINKS")
print("="*80)
print(impact_links_df.head(10))

print("\n" + "="*80)
print("REFERENCE CODES")
print("="*80)
print(ref_codes_df)

print("\n" + "="*80)
print("RECORDS BY RECORD_TYPE")
print("="*80)
print(data_df['record_type'].value_counts())

print("\n" + "="*80)
print("RECORDS BY PILLAR")
print("="*80)
print(data_df['pillar'].value_counts())

print("\n" + "="*80)
print("RECORDS BY SOURCE_TYPE")
print("="*80)
print(data_df['source_type'].value_counts())

print("\n" + "="*80)
print("RECORDS BY CONFIDENCE")
print("="*80)
print(data_df['confidence'].value_counts())

print("\n" + "="*80)
print("RECORD_TYPE BY PILLAR")
print("="*80)
print(pd.crosstab(data_df['record_type'], data_df['pillar']))

# Convert observation_date to datetime
data_df['observation_date'] = pd.to_datetime(data_df['observation_date'], errors='coerce')

print("\n" + "="*80)
print("TEMPORAL RANGE")
print("="*80)
print(f"Earliest date: {data_df['observation_date'].min()}")
print(f"Latest date: {data_df['observation_date'].max()}")
if pd.notna(data_df['observation_date'].min()) and pd.notna(data_df['observation_date'].max()):
    print(f"Date range: {(data_df['observation_date'].max() - data_df['observation_date'].min()).days / 365.25:.1f} years")

print("\n" + "="*80)
print("TEMPORAL RANGE BY RECORD TYPE")
print("="*80)
for record_type in data_df['record_type'].unique():
    subset = data_df[data_df['record_type'] == record_type]
    if not subset['observation_date'].isna().all():
        print(f"\n{record_type}:")
        print(f"  Earliest: {subset['observation_date'].min()}")
        print(f"  Latest: {subset['observation_date'].max()}")

print("\n" + "="*80)
print("UNIQUE INDICATORS")
print("="*80)
indicators = data_df['indicator_code'].dropna().unique()
print(f"Total unique indicators: {len(indicators)}")
print(indicators)

print("\n" + "="*80)
print("INDICATOR COVERAGE")
print("="*80)
for indicator in indicators:
    subset = data_df[data_df['indicator_code'] == indicator]
    count = len(subset)
    if not subset['observation_date'].isna().all():
        date_range = f"{subset['observation_date'].min().year} - {subset['observation_date'].max().year}"
    else:
        date_range = "N/A"
    pillar = subset['pillar'].mode()[0] if not subset['pillar'].isna().all() else "N/A"
    print(f"{indicator}: {count} records, {date_range}, pillar: {pillar}")

print("\n" + "="*80)
print("CATALOGED EVENTS")
print("="*80)
events = data_df[data_df['record_type'] == 'event']
print(f"Total events: {len(events)}")
print("\nEvent Details:")
for idx, row in events.iterrows():
    print(f"  {row['record_id']}: {row['indicator']} - {row['category']} - {row['observation_date'].date()}")

print("\n" + "="*80)
print("IMPACT LINKS SUMMARY")
print("="*80)
print(f"Total impact links: {len(impact_links_df)}")

print("\nIMPACT LINKS BY PILLAR")
print(impact_links_df['pillar'].value_counts())

print("\nIMPACT LINKS BY IMPACT DIRECTION")
print(impact_links_df['impact_direction'].value_counts())

print("\n" + "="*80)
print("EVENT-INDICATOR RELATIONSHIPS")
print("="*80)
for idx, link in impact_links_df.iterrows():
    event = events[events['record_id'] == link['parent_id']].iloc[0] if len(events[events['record_id'] == link['parent_id']]) > 0 else None
    if event is not None:
        print(f"\nEvent: {event['indicator']} ({event['category']})")
        print(f"  Affects: {link['related_indicator']} ({link['pillar']})")
        print(f"  Direction: {link['impact_direction']}, Magnitude: {link['impact_magnitude']}, Lag: {link['lag_months']} months")

print("\n" + "="*80)
print("EVENTS WITH PILLAR ASSIGNMENTS")
print("="*80)
events_with_pillar = events[events['pillar'].notna()]
if len(events_with_pillar) > 0:
    print(f"Warning: {len(events_with_pillar)} events have pillar assignments (should be empty)")
    for idx, row in events_with_pillar.iterrows():
        print(f"  {row['record_id']}: {row['indicator']} - pillar: {row['pillar']}")
else:
    print("Good: No events have pillar assignments (as expected)")

print("\n" + "="*80)
print("DATA QUALITY CHECK")
print("="*80)

# Check for missing values
print("\nMissing values by column:")
missing = data_df.isnull().sum()
print(missing[missing > 0])

# Check confidence levels
print("\nCONFIDENCE DISTRIBUTION")
confidence_dist = data_df['confidence'].value_counts(normalize=True) * 100
print(confidence_dist)

# Check for duplicate record IDs
duplicates = data_df['record_id'].duplicated().sum()
print(f"\nDuplicate record IDs: {duplicates}")
