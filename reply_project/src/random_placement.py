import numpy as np
import random

# INPUT SAMPLE
# dev_coordinates: [[2, 1], [2, 2]]
# pm_coordinates: [[2, 1], [2, 2]]
# devs: [['company', 8, ['java', 'c#']], []]
# pms: [['company', 8], []]


def magic(dev_places_coords, pm_places_coords, dev_list, pms_list):
    # random placements machen (coordinate to output_array)
        # eine dev-lange array mit x füllen
        # for each dev_coordinate
            # search random dev aus der array
            # replace x mit output
            
    dev_output = coordinates_to_placements(dev_list, dev_places_coords)
    print('Devs output:', dev_output)
    
    # same for pms
    pms_output = coordinates_to_placements(pms_list, pm_places_coords)
    print('PMS output:', pms_output)

    output = generate_output(dev_output, pms_output)
    print('ANSWER:', output)
    
    return output
    
    # score davon berechnen
    # x mal wiederholen
    # bestes ergebnis zurückgeben 


# if dev >= coord
# for each coord
#   get random()
#   if random is already placed
#       try again

# if dev < coord
# for each dev
#   get random coord

#---

# if dev >= coord
# for each coord
#   get random() from dict
# place entwickler
# remove from dict

# if dev < coord
# for each dev
#   get random coord


#---


    # case 1 dev >= cords
    # amount_to_be_placed = len(cords)
    # amount_random = len(dev) - len(cords)

    # for i = 0 to amount_to_be_placed
    #       cards.extentAtRandom(with x)

    # case 2 dev < cords
    # amount_to_be_placed = len(dev)
    # amount_random = len(cords) - len(dev)

def coordinates_to_placements(employee_list, employee_type_coordinates):
    output_array = []
    for employee in employee_list:
        output_array.append('X')
    
    employee_dict = dict()
    
    for employee in range(0, len(employee_list)):
        employee_dict[employee] = employee_list[employee]
    
    
    for coordinate in employee_type_coordinates:
        if bool(employee_dict):
            employee_idx = random.choice(list(employee_dict.keys()))
            employee_dict.pop(employee_idx)
            output_array[employee_idx] = coordinate

    return output_array

def generate_output(devs, pms):
    return devs + pms

# OUTPUT SAMPLE
# [[8, 4], ['x'], [2, 1]]


# Sample
#coordinates_to_placements([['company', 8, ['java', 'c#']], []],  [[2, 1], [2, 2]])

#magic(dev_places_coords, pm_places_coords, dev_list, pms_list):
#magic([[2, 1], [2, 2]], [[3, 1], [2, 4]], [['dev'], ['dev'], ['dev']], [['pm'], ['pm']])