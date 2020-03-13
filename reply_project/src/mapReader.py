def read_map(map): 
    # create two-dim array
    arrayed_map = read_rows(map)


    # create a place_list
    return create_place_list(arrayed_map)


def read_rows(map):
    arrayed_map = []
    for row in map: 
        places_in_row_list = list(row)
        arrayed_map.append(places_in_row_list)

    return arrayed_map

def create_place_list(arrayed_map):
    dev_place_list = []
    pms_place_list = []
    for x, row in enumerate(arrayed_map):
        for y, place in enumerate(row):
            if place == 'M': 
                pms_place_list.append([y, x])
            elif place == '_':
                dev_place_list.append([y, x])
    return (dev_place_list, pms_place_list)
