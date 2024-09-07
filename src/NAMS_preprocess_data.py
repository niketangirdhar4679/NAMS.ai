def preprocess_crash_data(df):
    # Clean and prepare crash data for modeling
    df = df.dropna()
    # More processing here
    return df

def preprocess_permit_data(df):
    # Clean and prepare permit data for modeling
    df['Year'] = pd.to_datetime(df['Date']).dt.year
    return df
