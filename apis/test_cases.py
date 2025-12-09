from utils import get_headers
API_KEY = "4f26b02a-3888-4f1c-b922-f730d62e89d8"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImM0N2RlMWUzLWE5YjItNDUxMS1hMjNjLTcwYWY3YTUwY2UwMiIsInVuaXF1ZV9uYW1lIjoiVmlzaGFsIFRoYWt1ciIsImVtYWlsIjoidmlzaGFsLXRoYWt1ckBjc3NvZnRzb2x1dGlvbnMuY29tIiwiZGVzaWduYXRpb24iOiJRdWFsaXR5IEFuYWx5c3QiLCJkZXBhcnRtZW50SWQiOiIxIiwicm9sZSI6IkVtcGxveWVlIiwibmJmIjoxNzY1MjczMjEwLCJleHAiOjE3NjUzNTk2MTAsImlhdCI6MTc2NTI3MzIxMCwiaXNzIjoiaHR0cHM6Ly8zdHN0Zy1hcGkuY3NkZXZodWIuY29tL3N3YWdnZXIvaW5kZXguaHRtbCIsImF1ZCI6Imh0dHBzOi8vM3RzdGctYXBpLmNzZGV2aHViLmNvbS9zd2FnZ2VyL2luZGV4Lmh0bWwifQ.fS51awU-Y-0x5K7lB-9VlJUFaFl-rfqWIGz5_HifVTM"
VALID_TOKEN = TOKEN
TEST_CASES = {

    # ========================= LOGIN =========================
    "login": [
        {
            "title": "Valid Login",
            "body": {"email": "vishal-thakur@cssoftsolutions.com", "password": "Test@123#"},
            "expected_status": 200,
            "headers": get_headers()
        },
        {
            "title": "Wrong Password",
            "body": {"email": "vishal-thakur@cssoftsolutions.com", "password": "WrongPass"},
            "expected_status": 401,
            "headers": get_headers()
        },
        {
            "title": "Wrong Email",
            "body": {"email": "wrong@xyz.com", "password": "Test@123#"},
            "expected_status": 404,
            "headers": get_headers()
        },
        {
            "title": "Empty Email",
            "body": {"email": "", "password": "Test@123#"},
            "expected_status": 400,
            "headers": get_headers()
        },
        {
            "title": "Empty Password",
            "body": {"email": "vishal-thakur@cssoftsolutions.com", "password": ""},
            "expected_status": 400,
            "headers": get_headers()
        },
        {
            "title": "SQL Injection Attempt",
            "body": {"email": "admin' OR 1=1 --", "password": "test"},
            "expected_status": 401,
            "headers": get_headers()
        }
    ],

    # ====================== RESET PASSWORD ======================
    "reset_password": [
        {
            "title": "Valid Reset Token",
            "body": {"token": VALID_TOKEN, "password": "Test@123#"},
            "expected_status": 200,
            "headers": get_headers()
        },
        {
            "title": "Invalid Token",
            "body": {"token": "invalid123", "password": "Test@123#"},
            "expected_status": 401,
            "headers": get_headers()
        },
        {
            "title": "Weak Password",
            "body": {"token": VALID_TOKEN, "password": "123"},
            "expected_status": 400,
            "headers": get_headers()
        },
        {
            "title": "Empty Token",
            "body": {"token": "", "password": "Test@123#"},
            "expected_status": 400,
            "headers": get_headers()
        }
    ],

    # ====================== CHANGE PASSWORD ======================
    "change_password": [
        {
            "title": "Valid Change",
            "body": {
                "id": "c47de1e3-a9b2-4511-a23c-70af7a50ce02",
                "email": "vishal-thakur@cssoftsolutions.com",
                "oldPassword": "Test@123#",
                "newPassword": "Test@123#"
            },
            "expected_status": 200,
            "headers": get_headers()
        },
        {
            "title": "Wrong Old Password",
            "body": {
                "id": "c47de1e3-a9b2-4511-a23c-70af7a50ce02",
                "email": "vishal-thakur@cssoftsolutions.com",
                "oldPassword": "WrongPass",
                "newPassword": "Test@123#"
            },
            "expected_status": 401,
            "headers": get_headers()
        },
        {
            "title": "Empty New Password",
            "body": {
                "id": "c47de1e3-a9b2-4511-a23c-70af7a50ce02",
                "email": "vishal-thakur@cssoftsolutions.com",
                "oldPassword": "Test@123#",
                "newPassword": ""
            },
            "expected_status": 400,
            "headers": get_headers()
        }
    ],

    # ====================== TOKEN VALIDATE ======================
    "token_validate": [
        {
            "title": "Valid Token",
            "body": {"token": VALID_TOKEN},
            "expected_status": 200,
            "headers": get_headers()
        },
        {
            "title": "Expired Token",
            "body": {"token": "expired-token"},
            "expected_status": 401,
            "headers": get_headers()
        },
        {
            "title": "Invalid Token Format",
            "body": {"token": "abc"},
            "expected_status": 401,
            "headers": get_headers()
        },
        {
            "title": "Empty Token",
            "body": {"token": ""},
            "expected_status": 400,
            "headers": get_headers()
        }
    ],

    # ====================== ADMIN RESET PASSWORD ======================
    "admin_employee_password_reset": [
        {
            "title": "Valid Admin Reset",
            "body": {
                "id": "c47de1e3-a9b2-4511-a23c-70af7a50ce02",
                "email": "vishal-thakur@cssoftsolutions.com",
                "password": "Test@123#",
                "confirmPassword": "Test@123#"
            },
            "expected_status": 200,
            "headers": get_headers()
        },
        {
            "title": "Password Mismatch",
            "body": {
                "id": "c47de1e3-a9b2-4511-a23c-70af7a50ce02",
                "email": "vishal-thakur@cssoftsolutions.com",
                "password": "Test@123#",
                "confirmPassword": "Fail@123#"
            },
            "expected_status": 400,
            "headers": get_headers()
        },
        {
            "title": "Invalid User ID",
            "body": {
                "id": "123",
                "email": "vishal-thakur@cssoftsolutions.com",
                "password": "Test@123#",
                "confirmPassword": "Test@123#"
            },
            "expected_status": 400,
            "headers": get_headers()
        }
    ]
}
