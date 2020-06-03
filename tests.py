import requests
import json

def tests_for_lets_ride_apis():
    
    print("**********Login***************")
    data = {"mobile_number":"12345","password":"divyasathya"}
    headers = {"Content-Type":"application/json"}
    data = json.dumps(data)
    url = "http://127.0.0.1:8080/api/lets_ride/login/v1/"
    response = requests.post(url=url, data=data,headers=headers)

    print("response: ",response)
    response_data = json.loads(response.content)
    print("Response: ",response_data)
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
        "from_datetime":"2020-06-02 21:52:48.548978",
        "to_datetime":"2020-07-02 21:52:48.548978"
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
    
    print("\n*******************AssetTransportRequest***************************")
    data = {
        "source":"hyderabad",
        "destination":"bangloor",
        "flexible":"false", 
        "datetime":"2020-07-02 21:52:48.548978", 
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
        "datetime":"2020-05-02 21:52:48.548978",
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
        "from_datetime":"2020-04-02 21:52:48.548978",
        "to_datetime":"2020-06-02 21:52:48.548978"
    }
    data = json.dumps(data)
    url = 'http://127.0.0.1:8080/api/lets_ride/share_travel_info/v1/'
    headers={"Content-Type":"application/json",
    "Authorization": "Bearer kvGfzAX6frT4A75jjeewGtKqdQuDXK"}
    response = requests.post(
        data=data, headers=headers, url=url
    )
    print("Requestdata: ",data)
    print("Response:", response)

    print("\n*******************GetMyRideRequests***************************")
    
    url = 'http://127.0.0.1:8080/api/lets_ride/my_requests/ride/v1/'
    params = {
        "limit":3,
        "offset":1,
        "status":"Pending",
        "order": "DESC"
    }
    response = requests.get(headers=headers, url=url,params=params
    )
    print("Response:", response)
    response_data = json.loads(response.content)
    print(response_data)

    print("\n*******************GetMyAssetTranportRequests***************************")
    url = "http://127.0.0.1:8080/api/lets_ride/my_requests/asset/v1/?limit=2&offset=26"
    response = requests.get(headers=headers, url=url)
    print("Response:", response)
    response_data = json.loads(response.content)
    print("Response: ",response_data)
    
    
    print("\n*******************GetMatchingRideRequests***************************")
    url = "http://127.0.0.1:8080/api/lets_ride/matching_requests/ride/v1/?limit=10&offset=0"
    headers={"Content-Type":"application/json",
    "Authorization": f"Bearer {access_token}"}
    response = requests.get(headers=headers, url=url)
    print("Response:", response)
    response_data = json.loads(response.content)
    print("Response: ",response_data)
    
    print("\n*******************GetMatchingAssetRequests***************************")
    url = "http://127.0.0.1:8080/api/lets_ride/matching_requests/asset/v1/"
    headers={"Content-Type":"application/json",
    "Authorization": f"Bearer {access_token}"}
    response = requests.get(headers=headers, url=url)
    print("Response:", response)
    response_data = json.loads(response.content)
    print("Response: ",response_data)
    
tests_for_lets_ride_apis()