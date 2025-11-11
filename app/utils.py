import pandas as pd
from pathlib import Path
import streamlit as st

def load_data(countries):
    """Load cleaned CSVs from data/ for selected countries."""
    files = {
        "Benin": "sample_data/benin_clean_sample.csv",
        "SierraLeone": "sample_data/sierraleone_clean_sample.csv", 
        "Togo": "sample_data/togo_clean_sample.csv",
    }

    dfs = []
    for c in countries:
        path = Path(files.get(c, ""))
        if path.exists():
            try:
                df = pd.read_csv(path)
                df["country"] = c
                dfs.append(df)
                st.success(f"✅ Successfully loaded data for {c}")
            except Exception as e:
                st.error(f"❌ Error loading {c}: {e}")
        else:
            st.error(f"❌ Missing file for {c}: {path}")
    
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        st.error("No data was successfully loaded!")
        return pd.DataFrame()

def compute_summary(df, countries, metrics):
    """Compute mean, median, std for selected metrics."""
    if df.empty:
        return pd.DataFrame()
    
    try:
        summary = (
            df[df["country"].isin(countries)]
            .groupby("country")[metrics]
            .agg(["mean", "median", "std"])
        )
        summary.columns = ["_".join(col) for col in summary.columns]
        return summary.reset_index()
    except Exception as e:
        st.error(f"Error computing summary: {e}")
        return pd.DataFrame()