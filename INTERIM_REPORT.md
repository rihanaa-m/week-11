# Ethiopia Financial Inclusion Forecasting System - Interim Report

**Week 11 Challenge: 10 Academy - KAIM 9**
**Date: July 21, 2026**
**Submitted by: Devin**

---

## Executive Summary

This interim report presents the completion of Task 1 (Data Exploration and Enrichment) and Task 2 (Exploratory Data Analysis) for the Ethiopia Financial Inclusion Forecasting System. The project aims to build a forecasting system that predicts Ethiopia's progress on two core dimensions of financial inclusion: Account Ownership (Access) and Digital Payment Usage.

Our analysis reveals that Ethiopia has made significant progress in financial inclusion, with account ownership growing from 14% in 2011 to 49% in 2024. However, we identified a concerning slowdown in the 2021-2024 period (+3 percentage points) despite massive mobile money expansion. The enriched dataset now includes 51 records (up from 43) with additional infrastructure, usage, and event data to support robust forecasting.

---

## Task 1: Data Exploration and Enrichment

### 1.1 Schema Understanding

The unified data schema uses a consistent structure across all record types:
- **Observations** (30 → 36 records): Measured values from surveys, reports, and operators
- **Events** (10 → 12 records): Policies, product launches, market entries, milestones
- **Targets** (3 records): Official policy goals
- **Impact Links** (14 → 18 records): Modeled relationships between events and indicators

**Key Design Principle**: Events are categorized by type (policy, product_launch, infrastructure) but are NOT pre-assigned to pillars. Their effects on specific indicators are captured through impact_link records, keeping the data unbiased.

### 1.2 Data Exploration Findings

**Dataset Composition:**
- Total records: 51 (36 observations, 12 events, 3 targets)
- Impact links: 18
- Unique indicators: 33
- Temporal range: 2011-2030 (with most data 2020-2025)

**Record Distribution:**
- By record type: 36 observations, 12 events, 3 targets
- By pillar: ACCESS (16), USAGE (11), GENDER (5), AFFORDABILITY (1)
- By source type: operator (15), survey (10), regulator (7), research (4), policy (3), calculated (2), news (2)
- By confidence: 93% high, 7% medium

**Temporal Coverage:**
- Earliest observation: 2011-12-31 (Account Ownership)
- Latest observation: 2025-12-31 (Forecast target)
- Most indicators have sparse coverage (1-3 data points)

### 1.3 Data Enrichment

We added 12 new records to improve forecasting capability:

**New Observations (6 records):**
1. **Smartphone Penetration Rate** (ACC_SMARTPHONE): 35% (2023) - Key enabler for digital services
2. **ATM Density** (ACC_ATM_DENSITY): 12.5 per 100k adults (2023) - Physical access baseline
3. **Bank Branch Density** (ACC_BRANCH_DENSITY): 8.3 per 100k adults (2023) - Traditional banking access
4. **Mobile Money Agent Density** (ACC_AGENT_DENSITY): 45.2 per 100k adults (2024) - Critical for cash-in/cash-out
5. **Digital Payment Adoption Rate** (USG_DIGITAL_PAYMENT): 35% (2024) - Core forecasting target
6. **Account Ownership - 2011 Baseline** (ACC_OWNERSHIP): 14% (2011) - Extended historical context

**New Events (2 records):**
1. **NBE Mobile Money Regulatory Framework** (EVT_NBE_MM_REG): March 2020 - Critical enabler for Telebirr
2. **Ethio Telecom 4G Network Expansion** (EVT_4G_EXPANSION): January 2023 - Infrastructure investment

**New Impact Links (4 records):**
1. NBE MM Regulation → Mobile Money Accounts (+10%, enabling, 15-month lag)
2. 4G Expansion → Smartphone Penetration (+5%, enabling, 12-month lag)
3. 4G Expansion → Digital Payments (+8%, enabling, 6-month lag)
4. Telebirr Launch → Digital Payment Adoption (+12%, direct, 12-month lag)

**Rationale for Additions:**
- Extended temporal coverage back to 2011 for better trend analysis
- Added infrastructure enablers (smartphones, 4G, agents) critical for forecasting
- Included core usage indicator (digital payment adoption) required for forecasting
- Captured critical regulatory and infrastructure events
- Modeled event-indicator relationships based on empirical evidence and comparable country data

---

## Task 2: Exploratory Data Analysis

### 2.1 Dataset Overview

The enriched dataset provides comprehensive coverage of Ethiopia's financial inclusion landscape:

**Data Quality:**
- 93% of records have high confidence (primary/verified sources)
- Authoritative sources: Global Findex, NBE, GSMA, operator reports
- Consistent schema with proper event-indicator separation
- No duplicate record IDs

**Data Gaps:**
- Sparse temporal coverage: Most indicators have only 1-3 data points
- Limited historical data: Most data post-2020
- No regional disaggregation (all national level)
- Limited gender-disaggregated data (only account ownership)
- Missing quarterly data for trend analysis

### 2.2 Access Analysis - Account Ownership Trajectory

**Key Findings:**

1. **Strong Historical Growth**: Account ownership grew from 14% (2011) to 49% (2024)
   - 2011-2014: +8pp (14% → 22%)
   - 2014-2017: +13pp (22% → 35%)
   - 2017-2021: +11pp (35% → 46%)
   - 2021-2024: +3pp (46% → 49%) ⚠️ **SLOWDOWN**

2. **Gender Gap**: In 2021, account ownership was 56% for males vs 36% for females (20pp gap)

3. **2021-2024 Slowdown Investigation**: Despite massive mobile money expansion:
   - Telebirr grew to 54M+ users since 2021 launch
   - M-Pesa entered in 2023 with 10M+ users
   - Yet account ownership grew only +3pp

**Potential Explanations:**
- Registered vs. Active Gap: Mobile money accounts may not translate to Findex-defined "account ownership"
- Definition Mismatch: Findex defines account ownership broadly (bank OR mobile money)
- User Overlap: Same users may have multiple mobile money accounts
- Dormant Accounts: High registration but low active usage
- Survey Timing: 2024 survey may have captured early adoption phase
- Traditional Bank Stagnation: Traditional banking may have stagnated while mobile money grew

### 2.3 Usage Analysis - Digital Payments

**Key Findings:**

1. **Mobile Money Account Penetration**: Doubled from 4.7% (2021) to 9.45% (2024)
   - Growth rate: +101% over 3 years
   - Still low relative to mobile money user numbers (suggests registered vs. active gap)

2. **Digital Payment Adoption**: 35% of adults made or received digital payments (2024)
   - This is significantly higher than mobile money account ownership (9.45%)
   - Suggests digital payments through other channels (banking apps, cards, P2P)

3. **P2P Transaction Milestone**: P2P digital transfers surpassed ATM cash withdrawals (October 2024)
   - Key milestone indicating digital payment adoption
   - Reflects Ethiopia's unique P2P-dominant market

### 2.4 Infrastructure and Enablers Analysis

**Key Findings:**

1. **4G Coverage**: Nearly doubled from 37.5% (2023) to 70.8% (2025)
   - Major infrastructure investment supporting digital services
   - Critical enabler for smartphone adoption and digital transactions

2. **Smartphone Penetration**: 35% (2023)
   - Significant enabler for mobile money and digital payment adoption
   - Room for growth compared to other African markets

3. **Agent Network Density**: 45.2 per 100k adults (2024)
   - Critical for cash-in/cash-out services in mobile money ecosystems
   - Strong agent network correlates with mobile money adoption in other markets

4. **Physical Access**: ATM density (12.5 per 100k) and branch density (8.3 per 100k)
   - Provides baseline for measuring digital disruption
   - Traditional channels still important for financial access

### 2.5 Event Timeline and Visual Analysis

**Key Events (2020-2025):**

1. **March 2020**: NBE Mobile Money Regulatory Framework (enabling regulation)
2. **May 2021**: Telebirr Launch (major product launch)
3. **September 2021**: NFIS-II Strategy Launch (policy framework)
4. **August 2022**: Safaricom Ethiopia Commercial Launch (market entry)
5. **January 2023**: Ethio Telecom 4G Network Expansion (infrastructure)
6. **August 2023**: M-Pesa Ethiopia Launch (product launch)
7. **January 2024**: Fayda Digital ID Program Rollout (infrastructure)
8. **July 2024**: Foreign Exchange Liberalization (policy reform)
9. **October 2024**: P2P Transaction Count Surpasses ATM (milestone)
10. **October 2025**: M-Pesa EthSwitch Integration (partnership - planned)
11. **December 2025**: EthioPay Instant Payment System Launch (infrastructure - planned)

**Event-Indicator Relationships:**
- 18 impact links model how events affect indicators
- Most impacts are positive (12 increase, 2 decrease)
- Distribution across pillars: USAGE (6), ACCESS (4), AFFORDABILITY (3), GENDER (1)
- Lag times range from 1-24 months, with most impacts materializing within 6-12 months

### 2.6 Correlation Analysis

**Key Correlations (based on available data):**
- Limited correlation analysis possible due to sparse data
- Infrastructure indicators (4G, smartphones) expected to correlate with access and usage
- Agent density expected to correlate with mobile money adoption
- More data points needed for robust correlation analysis

**Impact Link Insights:**
- Telebirr launch modeled to affect ACCESS (account ownership), USAGE (P2P transactions), and user acquisition
- Fayda digital ID modeled to reduce gender gap and increase account ownership
- 4G expansion modeled to enable smartphone adoption and digital payments
- Competition (Safaricom entry) modeled to improve 4G coverage and reduce data costs

### 2.7 Key Insights Summary

**1. Account Ownership Slowdown Despite Mobile Money Boom**
- Account ownership grew only +3pp (2021-2024) despite 65M+ mobile money accounts opened
- Suggests registered vs. active gap, definition issues, or survey timing
- Critical anomaly to address in forecasting model

**2. Infrastructure-Led Growth Phase**
- 4G coverage nearly doubled (37.5% → 70.8%) with continued expansion planned
- Smartphone penetration at 35% with room for growth
- Infrastructure improvements may accelerate future financial inclusion

**3. Digital Payment Adoption Outpaces Account Ownership**
- 35% digital payment adoption vs 9.45% mobile money account ownership
- Suggests multiple channels: banking apps, cards, P2P transfers
- Important for understanding usage patterns

**4. Gender Gap Remains Significant**
- 20pp gender gap in account ownership (56% male vs 36% female in 2021)
- Fayda digital ID expected to reduce this gap
- Critical for inclusive growth

**5. Event-Driven Market Development**
- Clear sequence: Regulation (2020) → Telebirr Launch (2021) → Competition (2022-2023) → Infrastructure (2023-2024)
- Event impacts materialize over 6-24 month lags
- Event-augmented modeling appropriate for forecasting

**6. P2P-Dominant Market Dynamics**
- P2P transfers surpassed ATM transactions (key milestone)
- Ethiopia's unique P2P usage for commerce (not just transfers)
- Different usage patterns from other markets

**7. Data Limitations Challenge Traditional Time Series**
- Sparse data (most indicators 1-3 points) limits traditional time series
- Event-driven and scenario-based approaches more appropriate
- Expert judgment and comparable country evidence critical

### 2.8 Data Quality Assessment

**Strengths:**
- High confidence data (93% high confidence)
- Authoritative sources (Global Findex, NBE, GSMA)
- Unified schema with consistent structure
- Explicit event-indicator relationships
- Proper schema compliance (events without pillar assignments)

**Weaknesses:**
- Sparse temporal coverage
- Limited historical data
- No regional disaggregation
- Limited gender-disaggregated data
- Missing infrastructure data (POS, QR merchants, literacy)
- No transaction volume data
- 3-year survey frequency (Findex)

**Forecasting Implications:**
- Limited historical data makes pure time series challenging
- Event-augmented models more appropriate
- Scenario analysis needed for uncertainty
- External data may be needed for leading indicators
- Expert judgment important for impact estimation

---

## Preliminary Observations on Event-Indicator Relationships

Based on the impact link analysis and event timeline:

1. **Regulatory Enablers Critical**: NBE's 2020 mobile money regulatory framework was a prerequisite for Telebirr's launch and subsequent market development. This suggests regulatory environment is a key driver.

2. **Infrastructure Multipliers**: 4G expansion and digital ID (Fayda) are modeled as "enabling" events with multiplier effects on multiple indicators. Infrastructure investments may have higher ROI than product launches alone.

3. **Competition Dynamics**: Safaricom's entry is modeled to improve 4G coverage and reduce data costs, suggesting competition drives infrastructure investment and affordability.

4. **Lag Effects Matter**: Event impacts materialize over 6-24 months, with regulatory and infrastructure events having longer lags than product launches. Forecasting models must account for these temporal dynamics.

5. **Gender Impact**: Fayda digital ID is specifically modeled to reduce the gender gap in account ownership, suggesting digital ID can be a tool for inclusive growth.

---

## Data Limitations Identified

1. **Temporal Sparsity**: Most indicators have only 1-3 data points, limiting trend analysis and correlation studies.

2. **Survey Frequency**: Global Findex surveys every 3 years creates gaps in time series data.

3. **No Regional Data**: All data at national level; cannot analyze urban/rural or regional disparities.

4. **Limited Gender Data**: Only account ownership has gender disaggregation; other indicators lack gender breakdown.

5. **Missing Infrastructure**: No data on POS terminals, QR merchant adoption, literacy rates, electricity access.

6. **No Transaction Volumes**: Limited data on actual transaction volumes, values, and frequency.

7. **Registered vs. Active Gap**: Mobile money user numbers (54M+) far exceed survey-reported account ownership (9.45%), suggesting data definition or measurement issues.

---

## Hypotheses for Impact Modeling Phase

1. **Account Ownership Reacceleration Hypothesis**: The 2021-2024 slowdown is temporary due to survey timing, definition issues, or dormancy. Infrastructure improvements (4G, Fayda) and competition will drive reacceleration in 2025-2027.

2. **Infrastructure-Led Growth Hypothesis**: 4G expansion and digital ID will have multiplicative effects on both access and usage, with impacts materializing over 12-24 month lags.

3. **Competition-Driven Innovation Hypothesis**: Market entry by Safaricom and M-Pesa will drive product innovation, price competition, and infrastructure investment, accelerating adoption.

4. **Gender Gap Reduction Hypothesis**: Digital ID (Fayda) and agent network expansion will disproportionately benefit women, reducing the gender gap in account ownership.

5. **P2P-First Usage Hypothesis**: Ethiopia's P2P-dominant usage pattern will continue, with P2P transactions growing faster than other digital payment use cases.

---

## Methodology Approach for Forecasting

Given the data limitations identified, we recommend:

1. **Event-Augmented Modeling**: Use event indicators rather than pure time series to capture the drivers of financial inclusion.

2. **Scenario Analysis**: Develop optimistic, base, and pessimistic scenarios to account for uncertainty and sparse data.

3. **Comparable Country Evidence**: Use impact estimates from similar markets (Kenya, Rwanda, India) where Ethiopian data is insufficient.

4. **Leading Indicators**: Incorporate infrastructure metrics (4G coverage, smartphone penetration, agent density) as leading indicators for financial inclusion.

5. **Expert Judgment**: Combine quantitative analysis with expert judgment for impact estimation where data is limited.

---

## Files Delivered

### Data Files
- `data/processed/ethiopia_fi_unified_data_enriched.xlsx` (51 records)
- `data/processed/ethiopia_fi_unified_data_enriched.csv` (51 records)
- `data/processed/impact_links_enriched.csv` (18 records)

### Documentation
- `data_enrichment_log.md` - Detailed documentation of all data additions
- `INTERIM_REPORT.md` - This report

### Analysis
- `notebooks/task1_data_exploration.ipynb` - Task 1 analysis notebook
- `notebooks/task2_eda.ipynb` - Task 2 EDA notebook with visualizations

### Supporting Files
- `explore_data.py` - Data exploration script
- `enrich_data.py` - Data enrichment script
- `check_sheets.py` - Excel sheet verification script

---

## Next Steps for Final Submission

1. **Task 3 - Event Impact Modeling**: Build quantitative models of how events affect indicators, validate against historical data, and refine impact estimates.

2. **Task 4 - Forecasting**: Develop forecasts for Account Ownership and Digital Payment Usage for 2025-2027, with confidence intervals and scenario analysis.

3. **Task 5 - Dashboard Development**: Create interactive Streamlit dashboard for data exploration, event impact visualization, and forecast presentation.

4. **Final Report**: Compile comprehensive report with methodology, results, limitations, and policy implications.

---

## Conclusion

Task 1 and Task 2 have successfully established a solid foundation for the Ethiopia Financial Inclusion Forecasting System. The enriched dataset now includes critical infrastructure, usage, and event data that will support robust forecasting. The exploratory analysis has identified key trends, anomalies, and drivers that will inform the impact modeling and forecasting phases.

The 2021-2024 account ownership slowdown despite massive mobile money expansion emerges as a critical anomaly to address in the forecasting model. Our analysis suggests this may be temporary due to measurement issues, and that infrastructure improvements and competition may drive reacceleration in 2025-2027.

The event-driven nature of Ethiopia's financial inclusion transformation, combined with the sparse historical data, indicates that event-augmented modeling and scenario analysis will be more appropriate than traditional time series approaches for this forecasting challenge.
