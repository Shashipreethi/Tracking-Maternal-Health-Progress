from django.shortcuts import render
import requests

API_KEY = "DPuYN7AYIVXRzg99skdeV16tyak31K_B3qfMqbFdRZW1"

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

        endpoint = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/019e8715-4805-72eb-b763-8eef73b2df02/predictions?version=2021-05-01"

        payload = {
            "input_data": [
                {
                    "fields": [
                        "AreaID","AreaName","Source","Sector","Subsector",
                        "Goal","Target","Indicator","Unit",
                        "SubgroupDimension","Subgroup","SubgroupOrder",
                        "DataValue","Footnote"
                    ],
                    "values": [[
                        "ind","india","health","health","1",
                        "1.3","1.3.8","number","location",
                        "total","1",1,"345432","NA"
                    ]]
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