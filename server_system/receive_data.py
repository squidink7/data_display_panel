from random import randint
import requests
import json


#Get data from the API handler running on client systems
def data_handler():
    
    
    #Get new data
    data = query_api_endpoint("http://localhost:8081/api")

    #Put data back into the master file.
    
    with open('server_system/data/data.json', 'w') as file:
        file.write('')
        json.dump(data, file, indent=4)
    

def query_api_endpoint(url):
    api_response = None

    #Query API endpoint.
    try:
        api_response = requests.get(url)

        print(f'{api_response.status_code} from "{url}"')

        if api_response.status_code == 200:
            data = api_response.json()
            return data
        
    except:
        if (api_response != None):  #Endpoint went down.
            if getattr(api_response, "status_code") == True:
                print(f"Error: {api_response.status_code}")
        else:
            print(f"Error: failed to retrieve data from API endpoint")

  
    
    return returnDefaultData()

def returnDefaultData():
    data = []
    return data

        



"""
#Take data and aggregate it into a single file - data.json
def data_handler():
    data = ""   
    with open('server_system/data/data.json') as file:
        data = json.load(file)

        data[0]["battery_charge"] = randint(1, 100)
        data[0]["disk_space_used"] = randint(1, 1000)
        data[0]["total_disk_space"] = randint(data[0]["disk_space_used"], 1000)
        data[0]["fan_speed"] = randint(1000, 8000)
        data[0]["gpu_load"] = randint(1, 100)
        data[0]["gpu_temp"] = randint(35, 100)
        data[0]["ram_load"] = randint(1, 100)
        data[0]["total_ram_space"] = randint(data[0]["ram_load"], 100)
        data[0]["cpu_load"] = randint(1, 100)
        data[0]["cpu_temp"] = randint(35, 100)

        
    with open('server_system/data/data.json', 'w') as file:
        json.dump(data, file, indent=4)
"""

    