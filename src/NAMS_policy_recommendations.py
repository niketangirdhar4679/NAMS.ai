def recommend_policies(analysis):
    policies = []
    if analysis['night_accidents'] > 50:
        policies.append("Increase street lighting in high-risk areas.")
    if analysis['speeding_violations'] > 100:
        policies.append("Enforce stricter speed limits in identified zones.")
    return policies

# Example usage
analysis = {'night_accidents': 60, 'speeding_violations': 120}
policies = recommend_policies(analysis)
print(policies)