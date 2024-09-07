def suggest_preventative_measures(hotspots):
    measures = []
    for hotspot in hotspots:
        if hotspot['risk_level'] > 0.7:
            measures.append(f"Improve road lighting at {hotspot['location']}")
        if hotspot['congestion_level'] > 0.8:
            measures.append(f"Adjust traffic signals at {hotspot['location']}")
    return measures

# Example usage
hotspots = [{'location': 'Main St', 'risk_level': 0.8, 'congestion_level': 0.85}]
suggestions = suggest_preventative_measures(hotspots)
print(suggestions)
