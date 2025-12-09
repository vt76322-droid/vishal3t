# apis.py

API_LIST = {
    "login": {
        "url": "https://3tstg-api.csdevhub.com/api/Account/login",
        "method": "POST"
    },
    "reset_password": {
        "url": "https://3tstg-api.csdevhub.com/api/Account/password/reset",
        "method": "POST"
    },
    "change_password": {
        "url": "https://3tstg-api.csdevhub.com/api/Account/password/change",
        "method": "POST"
    },
    "token_validate": {
        "url": "https://3tstg-api.csdevhub.com/api/Account/token/validate",
        "method": "POST"
    },
    "admin_employee_password_reset": {
        "url": "https://3tstg-api.csdevhub.com/api/Account/admin/employee/password/reset",
        "method": "POST"
    }
}
