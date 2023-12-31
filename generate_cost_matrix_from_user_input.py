# Generate Cost Matrix from User Input

import numpy as np
import pandas as pd

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_list_input(prompt, delimiter=','):
    user_input = input(prompt)
    items = [item.strip() for item in user_input.split(delimiter)]
    return items

def get_hospitals_with_capacities():
    hospital_data = get_list_input("Enter hospital names and capacities (name1,capacity1,name2,capacity2,...):")

    hospitals = []
    capacities = []

    # Extract hospital names and capacities from the input list
    for i in range(0, len(hospital_data), 2):
        hospital_name = hospital_data[i]
        capacity = int(hospital_data[i + 1])
        hospitals.append(hospital_name)
        capacities.append(capacity)

    return hospitals, capacities

def get_inputs():
    # Get the number of residents
    num_residents = get_integer_input("Enter the number of residents to be assigned: ")

    # Get hospitals and their capacities as separate lists
    hospital_names, hospital_capacities = get_hospitals_with_capacities()
    residents = []

    # Get rankings from each resident
    rankings = []

    for i in range(num_residents):
        resident_name = input(f"Enter the name of resident {i + 1}: ")
        residents.append(resident_name)

        resident_rankings = get_list_input(f"Enter hospital rankings for {resident_name} (comma-separated):")
        resident_rankings = [int(rank) for rank in resident_rankings]
        rankings.append(resident_rankings)

    # Create a cost matrix from the 'rankings' list
    cost_matrix = np.array(rankings)

    # Convert the NumPy matrix to a Pandas dataframe by row
    df = pd.DataFrame(cost_matrix, columns= hospital_names)
    df.index = residents

    display(df) # can comment out
    
    return df, residents, hospital_capacities
