# utils.py

import json
import datetime
import random
import string
import requests

# ----------------- API keys / Token -----------------
API_KEY = "4f26b02a-3888-4f1c-b922-f730d62e89d8"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImM0N2RlMWUzLWE5YjItNDUxMS1hMjNjLTcwYWY3YTUwY2UwMiIsInVuaXF1ZV9uYW1lIjoiVmlzaGFsIFRoYWt1ciIsImVtYWlsIjoidmlzaGFsLXRoYWt1ckBjc3NvZnRzb2x1dGlvbnMuY29tIiwiZGVzaWduYXRpb24iOiJRdWFsaXR5IEFuYWx5c3QiLCJkZXBhcnRtZW50SWQiOiIxIiwicm9sZSI6IkVtcGxveWVlIiwibmJmIjoxNzY1MjczMjEwLCJleHAiOjE3NjUzNTk2MTAsImlhdCI6MTc2NTI3MzIxMCwiaXNzIjoiaHR0cHM6Ly8zdHN0Zy1hcGkuY3NkZXZodWIuY29tL3N3YWdnZXIvaW5kZXguaHRtbCIsImF1ZCI6Imh0dHBzOi8vM3RzdGctYXBpLmNzZGV2aHViLmNvbS9zd2FnZ2VyL2luZGV4Lmh0bWwifQ.fS51awU-Y-0x5K7lB-9VlJUFaFl-rfqWIGz5_HifVTM"

def get_headers():
    """Return standard headers"""
    return {
        "x-api-key": API_KEY,
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

# ----------------- JSON Save -----------------
def save_json(data, file_name=None):
    if not file_name:
        file_name = f"results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
    return file_name

# ----------------- Random Data -----------------
def random_email(domain="test.com"):
    rand = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{rand}@{domain}"

def random_password(length=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choices(chars, k=length))

# ----------------- Pretty Response -----------------
def pretty_response(resp):
    try:
        return json.loads(resp.text)
    except:
        return resp.text

# ----------------- API Request Wrapper -----------------
def make_request(method, url, body, headers, retry=1):
    for attempt in range(retry + 1):
        try:
            return requests.request(
                method=method,
                url=url,
                json=body,
                headers=headers,
                timeout=15
            )
        except Exception as e:
            if attempt == retry:
                raise e

# ----------------- Status Code Validator -----------------
def is_valid_status(code, allowed=None):
    if allowed is None:
        allowed = [200, 400, 401, 403, 404, 500]
    return code in allowed
