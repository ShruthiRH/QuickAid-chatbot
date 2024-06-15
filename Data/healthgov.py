import requests
from bs4 import BeautifulSoup
import json

def extract_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Scenario name
    scenario_name = 'Fainting'
    
    # Extracting symptoms
    symptoms = []
    symptoms_section = soup.find('h2', id='symptoms')
    if symptoms_section:
        ul = symptoms_section.find_next('ul')
        if ul:
            symptoms = [li.get_text(strip=True) for li in ul.find_all('li')]
    
    # Extracting treatment steps
    detailed_steps = []
    treatment_section = soup.find('h2', id='treated')
    if treatment_section:
        for i in range(1,7):
            ol = treatment_section.find_next('ul')
            if ol:
                detailed_steps = [{"step_number": idx + 1, "step_description": li.get_text(strip=True)} for idx, li in enumerate(ol.find_all('li'))]

    

    return {
        'scenario_name': scenario_name,
        'symptoms': symptoms,
        'detailed_steps': detailed_steps
    }

# URL from Mayo Clinic
url = 'https://www.healthdirect.gov.au/fainting'

info = extract_info(url)
print(f"Scenario Name: {info['scenario_name']}")
print("Symptoms:")
for symptom in info['symptoms']:
    print(f" - {symptom}")
print("Detailed Steps:")
for step in info['detailed_steps']:
    print(f"Step {step['step_number']}: {step['step_description']}")

# Load existing data from JSON file
with open('medicaldataset.json', 'r') as file:
    data = json.load(file)

# Create new scenario data
new_scenario = {
    "scenario_id": 11,
    "scenario_name": info['scenario_name'],
    "symptoms & causes": info['symptoms'],
    "detailed_steps": info['detailed_steps']
}

# Append new scenario to the list of scenarios
data['scenarios'].append(new_scenario)

# Save updated data back to JSON file
with open('medicaldataset.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Scenario added to the dataset.")
