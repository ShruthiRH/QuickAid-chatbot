import requests
from bs4 import BeautifulSoup
import json

def extract_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Scenario name
    scenario_name = 'Diabetic Coma'
    
    # Extracting symptoms
    symptoms = []
    
    symptoms_section = soup.find('h2', string='Symptoms')
    if symptoms_section:
        ul = symptoms_section.find_next('ul')
        if ul:
            symptoms = [li.get_text(strip=True) for li in ul.find_all('li')]

    

    return {
        'scenario_name': scenario_name,
        'symptoms': symptoms,
    }

with open('medicaldataset.json','r') as file:
    data = json.load(file)

# URLs from Mayo Clinic
url = ['https://www.mayoclinic.org/diseases-conditions/diabetic-coma/symptoms-causes/syc-20371475',
       'https://www.mayoclinic.org/diseases-conditions/hypothermia/symptoms-causes/syc-20352682',
       'https://www.mayoclinic.org/diseases-conditions/seizure/symptoms-causes/syc-20365711',
       'https://www.mayoclinic.org/diseases-conditions/sudden-cardiac-arrest/symptoms-causes/syc-20350634',
       '']

info = extract_info(url)
print(f"Scenario Name: {info['scenario_name']}")
print("Symptoms:")
for symptom in info['symptoms']:
    print(f" - {symptom}")


new_scenario = {
    "scenarios": [
        {
            "scenario_id": 8,
            "scenario_name": info['scenario_name'],
            "symptoms & causes" : info['symptoms'],
            "detailed_steps": [
                {"step_number": 1, "step_description": "Help them to rest."},
                {"step_number": 2, "step_description": "Reassure the person. If they respond well, give them more sugary food"},
                {"step_number": 3, "step_decription": "Give them something sugary to eat or a non-diet drink."},
                {"step_number": 4, "step_decription": "If they respond well, give them more sugary food"},
                {"step_number": 5, "step_description": "If they do not respond well, contact emergency services"},
            ]
        }
    ]
}

data['scenarios'].append(new_scenario)

with open('medicaldataset.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Scenario added to the dataset.")

