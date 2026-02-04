from datetime import datetime

def run(tools):
    print("🧠 Generating content...")

    results = []

    for tool in tools:
        results.append({
            "title": f"{tool['name']} vs {tool['alt']}",
            "summary": f"{tool['alt']} is an open-source alternative to {tool['name']}.",
            "generated_at": datetime.utcnow().isoformat()
        })

    return results
