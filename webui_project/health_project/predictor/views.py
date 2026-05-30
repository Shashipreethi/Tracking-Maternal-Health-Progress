from django.shortcuts import render
import requests

API_KEY = "FKD5TVw6JKQ8lo9Gi-ci3vOUSMF41iBe5v1pl7jTpAwC"

def get_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"apikey={API_KEY}&grant_type=urn:ibm:params:oauth:grant-type:apikey"

    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]


def home(request):
    result = ""

    if request.method == "POST":
        year = request.POST.get("year")
        antenatal = request.POST.get("antenatal")
        skilled = request.POST.get("skilled")
        adolescent = request.POST.get("adolescent")
        expenditure = request.POST.get("expenditure")

        token = get_token()

        endpoint = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/019e6a09-75f8-7008-8c6c-ef071c812904/predictions?version=2021-05-01"

        payload = {
            "input_data": [
                {
                    "fields": ["year", "antenatal", "skilled", "adolescent", "expenditure"],
                    "values": [[year, antenatal, skilled, adolescent, expenditure]]
                }
            ]
        }

        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        response = requests.post(endpoint, json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
        else:
            result = "Error: " + response.text

    return render(request, "index.html", {"result": result})