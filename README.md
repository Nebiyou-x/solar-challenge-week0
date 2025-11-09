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




# Solar Data EDA & Cleaning

This repository contains an **end-to-end exploratory data analysis (EDA), cleaning, and profiling workflow** for solar datasets of different countries. The goal is to prepare clean and well-understood data for **comparison and region-ranking tasks**.  

The workflow includes summary statistics, missing-value analysis, outlier detection, time-series exploration, correlations, and advanced visualizations such as bubble charts and wind roses.

---

## 📂 Repository Structure

```text
├── notebooks/           # Jupyter / Colab notebooks
│   ├── togo.ipynb       # Example country EDA notebook
│   └── <country>_eda.ipynb
├── raw/                 # Raw CSV data (not committed)
├── data/                # Cleaned CSV files (not committed)
├── outputs/             # Generated plots, tables, and reports (not committed)
├── .gitignore           # Git ignore rules
└── README.md
````

> Note: `raw/` and `data/` folders are ignored in git to protect large datasets. See `.gitignore`.

---

## 🛠 Workflow

1. **Data Loading & Initial Profiling**

   * Load raw CSV files for each country.
   * Display summary statistics (`describe()`).
   * Generate missing-value reports and flag columns with >5% nulls.

2. **Outlier Detection & Cleaning**

   * Detect outliers using Z-scores for key columns (`GHI`, `DNI`, `DHI`, `ModA`, `ModB`, `WS`, `WSgust`).
   * Flag rows with |Z|>3.
   * Handle missing values with median imputation.
   * Optional clamping of physically impossible sensor readings (e.g., negative solar irradiance).

3. **Time-Series Analysis**

   * Line charts of `GHI`, `DNI`, `DHI`, `Tamb` over time.
   * Monthly and diurnal pattern analysis.

4. **Cleaning Impact**

   * Compare `ModA` and `ModB` pre- and post-cleaning.
   * Visualize averages by cleaning/outlier flag.

5. **Correlation & Relationships**

   * Correlation heatmap for key solar and meteorological variables.
   * Scatter plots to explore relationships (`WS`, `WSgust`, `WD` vs `GHI`, `RH` vs `Tamb`, etc.).

6. **Wind & Distribution Analysis**

   * Wind rose / radial bar plots for wind speed and direction.
   * Histograms for solar irradiance and wind speed distributions.

7. **Temperature & Humidity Analysis**

   * Examine influence of relative humidity (`RH`) on `Tamb` and `GHI`.
   * Bubble charts (`GHI` vs `Tamb` with bubble size = `RH` or `BP`).

---

## 📊 Example Visualizations

* **Time-Series Plot:** `GHI` over time
* **Correlation Heatmap:** relationships between irradiance, temperature, and humidity
* **Bubble Chart:** `GHI` vs `Tamb`, bubble size = `RH`
* **Wind Rose:** radial plot of wind speed by direction

All plots are saved in the `outputs/` folder.

---

## 📝 How to Use

1. Upload your raw CSV dataset for a country to the `raw/` folder (or Colab local session).
2. Open the corresponding notebook: `notebooks/<country>_eda.ipynb`.
3. Run all cells to:

   * Profile the data
   * Clean and impute missing values
   * Generate visualizations
4. Cleaned CSV files are saved to `data/<country>_clean.csv`.
5. Generated plots and reports are saved to `outputs/`.

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
  ```


---


