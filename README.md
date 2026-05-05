Executive Summary

This project develops a leakage-controlled, multi-modal financial machine learning pipeline to evaluate whether news sentiment provides incremental predictive power over traditional price-based signals in forecasting equity returns.

Using engineered features from price, volume, and news sentiment, the system predicts forward returns at multiple horizons (1-day and 5-day) under strict time-series validation. The study emphasizes robustness, statistical validity, and signal stability, rather than naive predictive accuracy.

Key findings show that while 5-day return forecasting exhibits moderate structure (ρ ≈ 0.43), the inclusion of raw daily sentiment provides only marginal and unstable improvement (Δρ ≈ +0.028). Controlled experiments, including feature shuffling, indicate that sentiment in its raw aggregated form does not consistently contribute independent alpha.

This project demonstrates quantitative research methodology, including leakage prevention, multi-modal feature integration, hypothesis-driven modeling, and robustness testing, aligning with industry-grade financial ML practices.

📊 Problem Formulation

We test the hypothesis:

E[r
t+h
	​

∣price features,sentiment]>E[r
t+h
	​

∣price features]

Where:

r
t+h
	​

: forward return over horizon h
h∈{1,5}
Objective: evaluate incremental predictive contribution of sentiment
🏗 End-to-End Pipeline
1. Data Acquisition
Market Data
Daily OHLCV data
Cleaned and indexed with proper datetime alignment
News Sentiment Data
Source: Kaggle financial news dataset
Fields:
Date
Positive score
Negative score
Neutral score
2. Feature Engineering
Price-Based Features
Daily returns
Rolling mean returns (trend proxy)
Rolling volatility (risk proxy)
Momentum indicators
Volume-based signals
Sentiment Feature Construction
sentiment
t
	​

=positive
t
	​

−negative
t
	​

Aggregation: daily mean

Leakage control:

sentiment
t
	​

→sentiment
t−1
	​

3. Target Definition

Non-log forward return:

r
t+h
	​

=
P
t
	​

P
t+h
	​

	​

−1
Primary: h=5
Secondary: h=1
4. Data Alignment & Integrity

Critical fixes applied:

Corrected datetime index corruption (epoch issue → 1970-01-01)
Enforced strict overlap between price and sentiment datasets
Replaced faulty merge with index-aligned join
Eliminated constant-feature bug in sentiment
5. Train-Test Protocol
Chronological split:
80% train
20% test
No shuffling (time-series consistency)
Target centering:
Train mean subtraction
Re-added post-prediction
6. Modeling

Model:

XGBoost Regressor

Capabilities:

Non-linear interactions
Handles heteroskedasticity
Robust to mixed feature scales
7. Evaluation Metrics
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
Pearson Correlation (primary signal metric)
Prediction variance vs target variance
📈 Results
🔹 5-Day Horizon
Model	Correlation	Insight
Price-only	~0.431	Strong baseline signal
Price + Sentiment	~0.459	Slight improvement
Sentiment Shuffled	~0.45	Similar performance
Interpretation
Δ correlation ≈ +0.028
Improvement is not statistically robust
Likely driven by:
temporal clustering
regime interactions
noise alignment
🔹 1-Day Horizon
Metric	Value
Correlation	~0.02–0.03
Interpretation
Essentially noise floor
Confirms known property of financial markets:
short-term returns ≈ unpredictable without microstructure data
🔬 Robustness & Validation

The project includes multiple safeguards:

✔ Leakage Prevention
Sentiment shifted by 1 day
Strict temporal split
✔ Data Integrity Checks
Fixed timestamp corruption
Verified feature variability
✔ Shuffle Test
Randomized sentiment feature
Compared against real signal
✔ Variance Diagnostics
Compared prediction vs target distribution
🧠 Key Insights
Short-horizon returns are noise-dominated
→ 1-day prediction is not viable with this feature set
5-day horizon contains exploitable structure
→ Price-based signals capture majority of it
Raw sentiment is weak as a standalone signal
→ Does not consistently add independent predictive power
Signal interactions matter more than raw features
→ Suggests conditional modeling is required
Pipeline correctness is critical
→ Initial datetime bug completely invalidated sentiment
🚀 Next Research Directions

Planned high-impact extensions:

1. Smoothed Sentiment
sentiment
3d
	​

=rolling mean (3 days)

Purpose:

Reduce noise
Capture delayed information diffusion
2. Interaction Features

Examples:

Sentiment × Volatility
Sentiment × Momentum

Goal:

Model conditional alpha
3. Directional Classification
y=1(r
t+5
	​

>0)

Metric:

AUC instead of correlation
4. Regime Segmentation

Split by:

High vs low volatility regimes

Evaluate:

Whether sentiment works only in specific regimes
🧩 Technical Stack
Python
Pandas / NumPy
XGBoost
Scikit-learn
📌 What This Project Demonstrates
Financial time-series feature engineering
Multi-modal data integration
Leakage-aware ML design
Hypothesis-driven experimentation
Robust evaluation methodology
Alpha signal validation and falsification
🎯 Final Conclusion

This project does not just build a predictive model—it tests a financial hypothesis rigorously.

The findings suggest:

Daily aggregated news sentiment, in its raw form, does not provide stable incremental alpha for 5-day equity return prediction under controlled conditions.

This is a valid and meaningful result, aligning with real-world quant research where most signals fail under rigorous testing.
