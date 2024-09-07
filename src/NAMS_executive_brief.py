from textblob import TextBlob

def create_executive_brief(model_output):
    summary = f"Based on the analysis, {model_output['high_risk_areas']} areas are identified as crash hotspots. Key contributing factors include {model_output['factors']}."
    return summary

# Example usage
model_output = {'high_risk_areas': 5, 'factors': 'road surface conditions, traffic congestion'}
brief = create_executive_brief(model_output)
print(brief)
