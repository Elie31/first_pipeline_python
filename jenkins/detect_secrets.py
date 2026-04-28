import json
import sys

with open(".secrets.baseline") as f:
    data = json.load(f)

results = data.get("results", {})

if any(results.values()):
    print("❌ Secrets détectés")
    sys.exit(1)

print("✅ Aucun secret")