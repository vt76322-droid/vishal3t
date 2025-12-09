import pytest
import requests
import datetime
import json
from utils import get_headers
from test_cases import TEST_CASES
from apis import API_LIST

RESULTS = []

def run_case(api_name, case):
    """Run a single API test case and return the result dict."""
    api_info = API_LIST.get(api_name)
    if not api_info:
        return {
            "title": case["title"],
            "api": api_name,
            "expected": case.get("expected_status"),
            "actual": "API_NOT_FOUND",
            "pass": False,
            "response": ""
        }

    url = api_info["url"]
    method = api_info["method"]
    headers = case.get("headers", get_headers())
    body = case.get("body", {})

    try:
        response = requests.request(method, url, json=body, headers=headers, timeout=10)
        actual_status = response.status_code
        expected_status = case.get("expected_status")

        result = {
            "title": case["title"],
            "api": api_name,
            "expected": expected_status,
            "actual": actual_status,
            "pass": actual_status == expected_status,
            "response": response.text
        }
        return result

    except Exception as e:
        return {
            "title": case["title"],
            "api": api_name,
            "expected": case.get("expected_status"),
            "actual": "ERROR",
            "pass": False,
            "response": str(e)
        }

# -----------------------------------
# PARAMETERIZE ALL TEST CASES
# -----------------------------------
@pytest.mark.parametrize("case", TEST_CASES["login"])
def test_login_cases(case):
    result = run_case("login", case)
    RESULTS.append(result)
    print(f"{result['api']} | {result['title']} | Expected: {result['expected']} | Actual: {result['actual']} | PASS={result['pass']}")

@pytest.mark.parametrize("case", TEST_CASES["reset_password"])
def test_reset_password_cases(case):
    result = run_case("reset_password", case)
    RESULTS.append(result)
    print(f"{result['api']} | {result['title']} | Expected: {result['expected']} | Actual: {result['actual']} | PASS={result['pass']}")

@pytest.mark.parametrize("case", TEST_CASES["change_password"])
def test_change_password_cases(case):
    result = run_case("change_password", case)
    RESULTS.append(result)
    print(f"{result['api']} | {result['title']} | Expected: {result['expected']} | Actual: {result['actual']} | PASS={result['pass']}")

@pytest.mark.parametrize("case", TEST_CASES["token_validate"])
def test_token_validate_cases(case):
    result = run_case("token_validate", case)
    RESULTS.append(result)
    print(f"{result['api']} | {result['title']} | Expected: {result['expected']} | Actual: {result['actual']} | PASS={result['pass']}")

@pytest.mark.parametrize("case", TEST_CASES["admin_employee_password_reset"])
def test_admin_employee_password_reset_cases(case):
    result = run_case("admin_employee_password_reset", case)
    RESULTS.append(result)
    print(f"{result['api']} | {result['title']} | Expected: {result['expected']} | Actual: {result['actual']} | PASS={result['pass']}")

# -----------------------------------
# Save results to JSON at the end
# -----------------------------------
def pytest_sessionfinish(session, exitstatus):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"api_test_results_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(RESULTS, f, indent=4)

    print(f"\n✅ Results saved to JSON: {filename}")