import os
import json
from datetime import datetime

DATA_FILE = "data/tools.json"
OUTPUT_DIR = "content/_generated"


# -----------------------
# SAFE FILE HELPERS
# -----------------------

def ensure_dirs():
    os.makedirs("data", exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# -----------------------
# DISCOVERY ENGINE (SAFE MOCK FOR NOW)
# -----------------------

def discover_tools():
    """
    Temporary discovery engine.
    Later we will plug in:
    - GitHub API
    - Product Hunt
    - Open source directories
    """

    today = datetime.utcnow().strftime("%Y-%m-%d")

    return [
        {
            "name": "ExampleOpenTool",
            "category": "developer-tools",
            "description": "Example autonomous discovery tool.",
            "date_added": today
        }
    ]


# -----------------------
# CONTENT GENERATOR
# -----------------------

def slugify(text):
    return text.lower().replace(" ", "-")


def generate_content(tool):
    slug = slugify(tool["name"])

    filename = os.path.join(
        OUTPUT_DIR,
        f"{slug}.md"
    )

    if os.path.exists(filename):
        print(f"SKIP existing: {slug}")
        return

    content = f"""---
title: "{tool['name']}"
date: {tool['date_added']}
category: "{tool['category']}"
generated: true
---

## Overview

{tool['description']}

## Why it matters

Autonomously discovered by OpenAlts engine.
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"GENERATED: {slug}")


# -----------------------
# MAIN PIPELINE
# -----------------------

def run():
    print("Starting OpenAlts Autonomous Engine")

    ensure_dirs()

    existing = load_data()
    new_tools = discover_tools()

    combined = existing + new_tools
    save_data(combined)

    for tool in new_tools:
        generate_content(tool)

    print("Pipeline complete")


if __name__ == "__main__":
    run()
