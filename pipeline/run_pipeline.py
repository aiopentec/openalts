import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline.tasks import discover
from pipeline.tasks import generate
from pipeline.tasks import save
import traceback

def main():
    print("🚀 OpenAlts Engine Starting...")

    try:
        tools = discover.run()
        results = generate.run(tools)
        save.run(results)

        print("✅ Engine Completed Successfully")

    except Exception as e:
        print("❌ Pipeline Failed")
        print(str(e))
        traceback.print_exc()

if __name__ == "__main__":
    main()
