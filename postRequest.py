import requests
header = {
    "Accept":"text/plain",
    "Content-Type": "application/json"
}
request_payload = {
    "id": 25,
    "title": "post request by tawhid",
    "dueDate": "2024-09-10T02:33:34.484Z",
    "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net//api/v1/Activities/",headers=header,json=request_payload)
print(response.status_code)
print(response.json())
data = response.json()

assert response.status_code == 200
assert data["id"] == 25
