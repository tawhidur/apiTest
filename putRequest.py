import requests
header = {
    "Accept":"text/plain",
}
response = requests.get("https://fakerestapi.azurewebsites.net//api/v1/Activities/3",headers=header)
print("Before update data")
print(response.status_code)
print(response.json())

headerPut = {
    "Accept":"text/plain",
    "Content-Type":"application/json"
}

putPayload = {
    "id": 9,
    "title": "PUT test by tawhid",
    "dueDate": "2024-09-15T03:43:19.337Z",
    "completed": True
}

print("After update data")
responsePut = requests.put("https://fakerestapi.azurewebsites.net//api/v1/Activities/3",headers=headerPut, json=putPayload)
print(responsePut,putPayload)
