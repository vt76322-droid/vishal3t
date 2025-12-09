# conftest.py
import datetime
import json
from test_runner import RESULTS  # import the global RESULTS list

def pytest_sessionfinish(session, exitstatus):
    # Create timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"api_test_results_{timestamp}.json"

    # Save JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(RESULTS, f, indent=4)

    print(f"\n✅ Results saved to JSON: {filename}")
