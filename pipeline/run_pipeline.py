import os
import json
from datetime import datetime

OUTPUT_DIR = "data"

def ensure_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def simulate_scrape():
    print("🔎 Simulating software discovery...")
    return [
        {"name": "Slack", "alt": "Element"},
        {"name": "Notion", "alt": "AppFlowy"},
        {"name": "Figma", "alt": "Penpot"},
    ]

def simulate_generation(tools):
    print("🧠 Generating comparisons...")
    results = []

    for tool in tools:
        results.append({
            "title": f"{tool['name']} vs {tool['alt']}",
            "summary": f"{tool['alt']} is an open-source alternative to {tool['name']}.",
            "generated_at": datetime.utcnow().isoformat()
        })

    return results

def save_output(results):
    filename = f"{OUTPUT_DIR}/comparisons_{datetime.utcnow().date()}.json"
    with open(filename, "w") as f:
        json.dump(results, f, indent=2)
    print(f"💾 Saved output to {filename}")

def main():
    print("🚀 OpenAlts Pipeline Starting...")
    ensure_dirs()
    tools = simulate_scrape()
    results = simulate_generation(tools)
    save_output(results)
    print("✅ Pipeline Complete!")

if __name__ == "__main__":
    main()
