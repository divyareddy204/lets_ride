import requests
import json

def tests_for_lets_ride_apis():
    
    print("**********Login***************")
    data = {"user_name":"divya","mobile_number":"5723890","password":"divya@123"}
    headers = {"Content-Type":"application/json"}
    data = json.dumps(data)
    url = "http://127.0.0.1:8080/api/lets_ride/login/v1/"
    response = requests.post(url=url, data=data,headers=headers)

    print("response: ",response)
    response_data = json.loads(response.content)
    access_token = response_data['access_token']
    print("access_token: ", access_token)
    
    print("\n*******************RideRequest***************************")
    data = {
        "source":"hyderabad",
        "destination":"bangloor",
        "flexible":"true",
        "no_of_seats":2,
        "luggage_quantity":2, 
        "datetime":None, 
        "from_datetime":"2020-09-04 06:00:00.000000-08:00",
        "to_datetime":"2020-09-04 06:00:00.000000-08:00"
    }
    data = json.dumps(data)
    headers = {"Content-Type":"application/json",
    "Authorization": f"Bearer {access_token}"}
    url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
    response = requests.post(
        data=data, headers=headers, url=url
    )
    print("Requestdata: ",data)
    print("Response: ", response)
    
    print("\n*******************AssetRideRequest***************************")
    data = {
        "source":"hyderabad",
        "destination":"bangloor",
        "flexible":"false", 
        "datetime":"2020-05-31 06:00:00.000000-08:00", 
        "no_of_assets":2,
        "deliver_person":"ram",
        "asset_type":"parcel",
        "sensitivity":"Sensitive",
        "from_datetime":None, 
        "to_datetime":None}
    data = json.dumps(data)

    headers = {"Content-Type":"application/json",
    "Authorization": f"Bearer {access_token}"}
    url = "http://127.0.0.1:8080/api/lets_ride/asset_transport_request/v1/"
    response = requests.post(
        data=data, headers=headers, url=url
    )
    print("Requestdata: ",data)
    print("Response: ", response)
    
    print("\n*******************ShareRide***************************")
    data ={
        "source":"hyderabad",
        "destination":"bangloor",
        "flexible":"false",
        "no_of_seats_available":2,
        "assets_quantity":2, 
        "datetime":"2020-09-04 06:00:00.000000-08:00",
        "from_datetime":None, "to_datetime":None
    }
    data = json.dumps(data)
    url = "http://127.0.0.1:8080/api/lets_ride/ride_share/v1/"
    headers={"Content-Type":"application/json",
    "Authorization": f"Bearer {access_token}"}
    response = requests.post(
        data=data, headers=headers, url=url
    )
    print("Requestdata: ",data)
    print("Response: ", response)
    print("\n*******************ShareTravelInfo***************************")
    data ={
        "source":"hyderabad",
        "destination":"bangloor",
        "flexible":"true",
        "medium":"Bus",
        "assets_quantity":2, 
        "datetime":None, 
        "from_datetime":"2020-09-04 06:00:00.000000-08:00",
        "to_datetime":"2020-09-04 06:00:00.000000-08:00"
    }
    data = json.dumps(data)
    url = 'http://127.0.0.1:8080/api/lets_ride/share_travel_info/v1/'
    headers={"Content-Type":"application/json",
    "Authorization": f"Bearer {access_token}"}
    response = requests.post(
        data=data, headers=headers, url=url
    )
    print("Requestdata: ",data)
    print("Response:", response)

    print("\n*******************GetMyRideRequests***************************")
    url = 'http://127.0.0.1:8080/api/lets_ride/my_requests/ride/v1/?limit=2&offset=1'
    response = requests.get(headers=headers, url=url
    )
    print("Response:", response)
    response_data = json.loads(response.content)
    print(response_data)
    print("\n*******************GetMyAssetTranportRequests***************************")
    """url = "http://127.0.0.1:8080/api/lets_ride/my_requests/asset/v1/?limit=2&offset=1"
    response = requests.get(headers=headers, url=url
    )
    print("Response:", response)
    response_data = json.loads(response.content)
    print("Response: ",response_data)"""
    
tests_for_lets_ride_apis()