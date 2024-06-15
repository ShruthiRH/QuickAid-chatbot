import json
import os
from bs4 import BeautifulSoup
import requests

import requests
from bs4 import BeautifulSoup

scenario_name = 'Stroke'
symptom_description =[]
cause_description=[]
url = "https://my.clevelandclinic.org/health/diseases/5601-stroke#symptoms-and-causes"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
symptoms_causes_section = soup.find("div", {"id": "symptoms-and-causes"})
if symptoms_causes_section:
    symptoms_list = symptoms_causes_section.find("ul")
    if symptoms_list:
        #print("Symptoms of stroke:")
        for symptom in symptoms_list.find_all("li"):
            symptom_description.append(symptom.text.strip())

print("Symptoms of stroke:")
for symptom in symptom_description:
    print(symptom)

data = {
    "scenarios": [
        {
            "scenario_id": 2,
            "scenario_name": scenario_name,
            "symptoms & causes" : symptom_description,
            "detailed_steps": [
                {"step_number": 1, "step_description": "Call 911 or local emergency services."},
                {"step_number": 2, "step_description": "Write down the time"},
                {"step_number": 3, "step_decription": "Keep stroke victims on their side with the head slightly elevated to promote blood flow."},
                {"step_number": 4, "step_decription": "Loosen any restrictive clothing"},
                {"step_number": 5, "step_description": "Check for pulse and breathing."},
                {"step_number": 6, "step_description": "If there is no pulse, begin CPR immediately."},
                {"step_number": 7, "step_description": "Keep doing this until an AED is available or emergency workers arrive."},
            ]
        }
    ]
}

with open('medicaldataset.json','a') as json_file:
    json.dump(data,json_file, indent=4)

print(f"JSON file saved in: {os.getcwd()}")










