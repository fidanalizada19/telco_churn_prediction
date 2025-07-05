from scipy.stats import ks_2samp
import pandas as pd

def detect_drift(reference_df: pd.DataFrame, new_df: pd.DataFrame, threshold=0.1):
    drifted_features = []
    for col in reference_df.columns:
        if reference_df[col].dtype in ['int64', 'float64']:
            stat, p_value = ks_2samp(reference_df[col], new_df[col])
            if p_value < threshold:
                drifted_features.append(col)
    return drifted_features
