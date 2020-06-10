# get_data.py

print("REQUESTING SOME DATA FROM THE INTERNET...")

import json
import requests
import statistics
# part1 

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
response_data = json.loads(response.text)

print(response_data["name"])
print("----------")


#part2 

request2_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"

response2 = requests.get(request2_url)
response2_data = json.loads(response2.text)

for a in response2_data:
    print(a["name"],a["id"])
print("----------")



#part3


request3_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response3 = requests.get(request3_url)
response3_data = json.loads(response3.text)
grades = [s["finalGrade"] for s in response3_data["students"]]
    
#min grade
print ("MIN:", min(grades))

#max grade
print ("MAX:", max(grades))

#average grade
print ("AVE:", statistics.mean(grades))

