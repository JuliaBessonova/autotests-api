import httpx

login_payload = {
    "email": "julia@test.com",
    "password": "Tester01"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
# print(login_response_data)
# print(login_response.status_code)

user_me_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=user_me_headers)
user_me_response_data = user_me_response.json()
print(user_me_response_data)
print(user_me_response.status_code)

