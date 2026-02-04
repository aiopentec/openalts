import os
import json
from datetime import datetime

OUTPUT_DIR = "data"

def run(results):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filename = f"{OUTPUT_DIR}/comparisons_{datetime.utcnow().date()}.json"

    with open(filename, "w") as f:
        json.dump(results, f, indent=2)

    print(f"💾 Saved {filename}")
