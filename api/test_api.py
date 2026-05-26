import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "age": 40,
    "DebtRatio": 0.3,
    "MonthlyIncome": 5000,
    "NumberOfDependents": 2
}

response = requests.post(url, json=data)

print(response.json())