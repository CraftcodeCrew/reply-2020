import numpy as np
from inputReader import read_file
from mapReader import read_map
from readDevs import read_devs
from readPMs import read_pms
from random_placement import magic

import outputWriter;

def main():
    runIt('../a_solar.txt')
    runIt('../b_dream.txt')
    runIt('../c_soup.txt')
    runIt('../d_maelstrom.txt')
    runIt('../e_igloos.txt')
    runIt('../f_glitch.txt')

def runIt(file):
    map, devs, pms = read_file(file)

    dev_places_coords, pm_places_coords = read_map(map)
    print('\nDEV_COORDINATES')
    print(dev_places_coords)
    print('\nPM_COORDINATES')
    print(pm_places_coords)
    
    dev_list = read_devs(devs)
    print('\nDEVS')
    print(dev_list)
    pm_list = read_pms(pms)
    print('\nPMS')
    print(pm_list)

    output = magic(dev_places_coords, pm_places_coords, dev_list, pm_list)
    print("\nOUTPUT", output)
    outputWriter.write(output, file.split("/")[1])


if __name__ == "__main__":
    main()