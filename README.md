Perfect! I can integrate **Task 3 (Cross-Country Comparison)** and **Task 4 (Optional Streamlit Dashboard)** into your existing README so it’s complete and structured. Here’s the updated version:

---

# 🌞 Solar Challenge Week 0

## 🧩 Environment Setup

This repository sets up the base environment for the Solar Challenge project.

### Steps to Reproduce

1. **Clone the repo**

   ```bash
   git clone https://github.com/Nebiyou-x/solar-challenge-week0.git
   cd solar-challenge-week0
   ```

2. **Create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. **Check CI**
   GitHub Actions runs automatically on every push to ensure dependencies install correctly.

---

# Solar Data EDA & Cleaning

This repository contains an **end-to-end exploratory data analysis (EDA), cleaning, and profiling workflow** for solar datasets of different countries. The goal is to prepare clean and well-understood data for **comparison and region-ranking tasks**.

The workflow includes summary statistics, missing-value analysis, outlier detection, time-series exploration, correlations, and advanced visualizations such as bubble charts and wind roses.

---


## 🛠 Workflow

### 1. Data Loading & Initial Profiling

* Load raw CSV files for each country.
* Display summary statistics (`describe()`).
* Generate missing-value reports and flag columns with >5% nulls.

### 2. Outlier Detection & Cleaning

* Detect outliers using Z-scores for key columns (`GHI`, `DNI`, `DHI`, `ModA`, `ModB`, `WS`, `WSgust`).
* Flag rows with |Z|>3.
* Handle missing values with median imputation.
* Optional clamping of physically impossible sensor readings (e.g., negative solar irradiance).

### 3. Time-Series Analysis

* Line charts of `GHI`, `DNI`, `DHI`, `Tamb` over time.
* Monthly and diurnal pattern analysis.

### 4. Cleaning Impact

* Compare `ModA` and `ModB` pre- and post-cleaning.
* Visualize averages by cleaning/outlier flag.

### 5. Correlation & Relationships

* Correlation heatmap for key solar and meteorological variables.
* Scatter plots to explore relationships (`WS`, `WSgust`, `WD` vs `GHI`, `RH` vs `Tamb`, etc.).

### 6. Wind & Distribution Analysis

* Wind rose / radial bar plots for wind speed and direction.
* Histograms for solar irradiance and wind speed distributions.

### 7. Temperature & Humidity Analysis

* Examine influence of relative humidity (`RH`) on `Tamb` and `GHI`.
* Bubble charts (`GHI` vs `Tamb` with bubble size = `RH` or `BP`).

---

## 📊 Task 3: Cross-Country Comparison

**Objective:** Compare solar potential across the three countries: **Benin, Sierra Leone, and Togo**.

### Key Steps

1. **Load cleaned CSVs locally**
   Import the cleaned datasets for each country.

2. **Metric Comparison**

   * Side-by-side boxplots of `GHI`, `DNI`, and `DHI` by country.
   * Summary table showing mean, median, and standard deviation.

3. **Statistical Testing**

   * Perform a one-way ANOVA or Kruskal-Wallis test on `GHI` values.
   * Report p-values to assess significance.

4. **Key Observations**

   * Bullet points highlighting trends, variability, and outliers.

5. **Visual Summary (Bonus)**

   * Bar chart ranking countries by average `GHI`.

---

## 🌐 Task 4 (Optional): Interactive Streamlit Dashboard

**Objective:** Build an interactive dashboard to explore insights across countries.

### Features

* Sidebar to select countries and metrics (`GHI`, `DNI`, `DHI`).
* Boxplots and summary tables for selected metrics.
* Ranking chart: countries by average `GHI`.
* Clean, interactive design for quick insights.

### Run Locally

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

### Deploy on Streamlit Cloud

https://nebiyou-x-solar-challenges-week0.streamlit.app/

---

## 📝 How to Use

1. Upload your raw CSV dataset to `raw/` (or Colab local session).
2. Open the corresponding notebook: `notebooks/<country>_eda.ipynb`.
3. Run all cells to:

   * Profile the data
   * Clean and impute missing values
   * Generate visualizations
4. Cleaned CSVs are saved to `data/<country>_clean.csv`.
5. Plots and reports are saved to `outputs/`.

---

## ⚡ Requirements

* Python 3.8+
* Libraries:

```text
pandas
numpy
matplotlib
seaborn
scipy
plotly
streamlit
pyngrok
```
