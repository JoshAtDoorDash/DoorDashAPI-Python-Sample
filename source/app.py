from os import access
import jwt.utils
import time
import math
import requests
import uuid

#Credentials provided from https://developer.doordash.com/portal/integration/drive/credentials
#TODO: Replace placeholders with credential values
access_key = {
  "developer_id": "UPDATE_WITH_DEVELOPER_ID", #TODO: Update value with Developer ID
  "key_id": "UPDATE_WITH_KEY_ID", #TODO: Update value with Key ID
  "signing_secret": "UPDATE_WITH_SIGNING_SECRET" #TODO: Update value with Signing Secret 
}

#Create token, pass values needed for JWT Header, Payload, and signature
token = jwt.encode(
    {
        "aud": "doordash",
        "iss": access_key["developer_id"],
        "kid": access_key["key_id"],
        "exp": str(math.floor(time.time() + 1800)), #Set to expire in 30 minutes
        "iat": str(math.floor(time.time())),
    },
    jwt.utils.base64url_decode(access_key["signing_secret"]), #pass decoded signing secret secret
    algorithm="HS256",
    headers={"dd-ver": "DD-JWT-V1"})

print("DoorDash API JWT: " + token)

endpoint = "https://openapi.doordash.com/drive/v2/deliveries/"

headers = {
    "Accept-Encoding": "application/json", # needed to avoid gzip compression response which throws error
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

#Generate Unique ID for Delivery
delivery_id = str(uuid.uuid4()) #TODO: Replace with generated system ID

request_body = { #TODO: Modify pickup and drop off addresses below
    "external_delivery_id": delivery_id,
    "pickup_address": "901 Market Street 6th Floor San Francisco, CA 94103",
    "pickup_business_name": "Wells Fargo SF Downtown",
    "pickup_phone_number": "+16505555555",
    "pickup_instructions": "Enter gate code 1234 on the callbox.",
    "dropoff_address": "901 Market Street 6th Floor San Francisco, CA 94103",
    "dropoff_business_name": "Wells Fargo SF Downtown",
    "dropoff_phone_number": "+16505555555",
    "dropoff_instructions": "Enter gate code 1234 on the callbox.",
    "order_value": 1999
}

#Make API call
create_delivery = requests.post(endpoint, headers=headers, json=request_body) 
print("Status Code: " + str(create_delivery.status_code))
print("Text: " + create_delivery.text)
print("Reason: " + create_delivery.reason)
