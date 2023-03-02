import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "<HwaC1dTU7HSw32YV-YKoEvySZE_c_IdmL6qDdO4_0YMO>"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print("mltoken",mltoken)

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["Age","SystolicBP","DiastolicBP","BS","BodyTemp","HeartRate"]], "values": [[15.0,120.0,80.0,7.9,98.0,70.0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/bae00016-e52d-4d6d-8d38-b5c526836040/predictions?version=2023-03-01', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=(response_scoring.json())
print(predictions)

