import re
from random import randint
from datetime import datetime

def get_random_int():
    return (randint(0, 9999999), randint(0, 9999999), randint(0, 9999999))

def get_person_info(note, person_id):
    person = {
        "person_id": person_id, 
        "year_of_birth": None,
        "month_of_birth": None,
        "day_of_birth": None,
        "death_date": None,
        "gender_value": None,
        "race_value": None,
        "ethnicity_value": None
    }

    # birth
    birth_date = re.search(r'(?<=Birth Date:).*(?=\nMarital Status)', note).group(0).strip()
    person["year_of_birth"], person["month_of_birth"], person["day_of_birth"] = map(int, birth_date.split("-"))

    # gender
    person["gender_value"] = re.search(r'(?<=\nGender:).*(?=\nAge:)', note).group(0).strip()

    # race_value
    person["race_value"] = re.search(r'(?<=Race:).*(?=\nEthnicity)', note).group(0).strip()

    # ethnicity_value
    person["ethnicity_value"] = re.search(r'(?<=Ethnicity:).*(?=\nGender:)', note).group(0).strip()

    # death date 관련 정보는 찾을 수 없음
    person["death_date"] = None

    return person

def get_visit_occurrence(note, person_id, visit_occurrence_id):
    visit_occurrence = {
        "visit_occurrence_id": visit_occurrence_id,
        "person_id": person_id, 
        "visit_start_date": None,
        "care_site_nm": None,
        "visit_type_value": None
        }
    
    # visit_start_date, care_site_nm
    visit_values = re.search(r'(?<=\nENCOUNTER\n).*(?=\nType)', note).group(0).split(":")
    visit_occurrence["visit_start_date"] = datetime.strptime(visit_values[0].strip(), "%Y-%m-%d")
    visit_occurrence["care_site_nm"] = visit_values[1].strip()
    
    # visit_type_value
    try:
        visit_occurrence["visit_type_value"] = visit_values[2].strip()
    except IndexError:
        pass
    
    return visit_occurrence

def get_drug_exposure(note, person_id, visit_occurrence_id, drug_exposure_id):
    drug_exposure = {
        "drug_exposure_id": drug_exposure_id,
        "person_id": person_id, 
        "drug_exposure_start_date": None,
        "drug_value": None,
        "route_value": None,
        "dose_value": None,
        "unit_value": None,
        "visit_occurrence_id": visit_occurrence_id
        }
    
    # drug_exposure_start_date, drug_value, route_value, dose_value, unit_value
    drug_values = re.findall('(?<=MEDICATIONS:\n)(.*?)(?=\n   \n   CONDITIONS)', note, flags=re.S)
    
    if drug_values:
        drug_values = drug_values[0].strip().split(" ")
        drug_exposure["drug_exposure_start_date"] = datetime.strptime(drug_values[0], "%Y-%m-%d")
        drug_exposure["drug_value"] = drug_values[2]
        drug_exposure["route_value"] = drug_values[5]
        drug_exposure["dose_value"] = drug_values[3]
        drug_exposure["unit_value"] = drug_values[4]
        return [drug_exposure]
    return []

def get_condition_occurrence(note, person_id, visit_occurrence_id):
    
    condition_occurrences = []
    conditions = re.findall('(?<=CONDITIONS:\n)(.*?)(?=\n   \n   CARE PLANS)', note, flags=re.S)
    if conditions:
        for condition in conditions[0].split("\n"):
    
            condition_occurrence = {
                "condition_occurrence_id": randint(0, 9999999),
                "person_id": person_id, 
                "condition_start_date": None,
                "condition_value": None,
                "visit_occurrence_id": visit_occurrence_id
            }
        
            condition_occurrence["condition_start_date"] = datetime.strptime(condition.split(" : ")[0].strip(), "%Y-%m-%d")
            condition_occurrence["condition_value"] = condition.split(" : ")[1].strip()
            condition_occurrences.append(condition_occurrence)
    
    return condition_occurrences